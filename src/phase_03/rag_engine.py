"""
RAG Engine for the AI Discovery Engine Dashboard.
Loads all normalized reviews, builds a vector index, and answers
questions by retrieving the most relevant reviews and synthesizing
a grounded response via Groq LLM.
"""
import json
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

REVIEWS_PATH = "docs/phases/phase-01/normalized_data.json"
ANALYSIS_PATH = "docs/phases/phase-02/analysis_results.json"
MODEL_NAME = "openai/gpt-oss-120b"
TOP_K = 8  # Number of reviews to retrieve per query


class RAGEngine:
    def __init__(self):
        self.reviews = []
        self.analysis = {}
        self.vectorizer = None
        self.tfidf_matrix = None
        self.client = None
        self._loaded = False

    def load(self):
        """Load reviews, build TF-IDF index, and initialize Groq client."""
        if self._loaded:
            return

        # Load raw reviews
        if os.path.exists(REVIEWS_PATH):
            with open(REVIEWS_PATH, "r", encoding="utf-8") as f:
                self.reviews = json.load(f)
        print(f"[RAG] Loaded {len(self.reviews)} reviews")

        # Load analysis synthesis for context
        if os.path.exists(ANALYSIS_PATH):
            with open(ANALYSIS_PATH, "r", encoding="utf-8") as f:
                self.analysis = json.load(f)
        print(f"[RAG] Loaded analysis results")

        # Build TF-IDF vector index over all review texts
        texts = [r.get("text", "") for r in self.reviews]
        self.vectorizer = TfidfVectorizer(
            max_features=5000,
            stop_words="english",
            ngram_range=(1, 2),
            min_df=2
        )
        self.tfidf_matrix = self.vectorizer.fit_transform(texts)
        print(f"[RAG] Built TF-IDF index: {self.tfidf_matrix.shape}")

        # Initialize Groq client
        api_key = os.getenv("GROQ_API_KEY")
        if api_key:
            self.client = Groq(api_key=api_key)
            print(f"[RAG] Groq client initialized with model {MODEL_NAME}")
        else:
            print("[RAG] WARNING: No GROQ_API_KEY found, will use extractive-only mode")

        self._loaded = True

    def retrieve(self, query: str, top_k: int = TOP_K) -> list[dict]:
        """Retrieve the top-K most relevant reviews for a query."""
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        top_indices = similarities.argsort()[-top_k:][::-1]

        results = []
        for idx in top_indices:
            if similarities[idx] > 0.01:  # Minimum relevance threshold
                review = self.reviews[idx].copy()
                review["relevance_score"] = float(similarities[idx])
                review["review_index"] = int(idx)
                results.append(review)

        return results

    def generate_answer(self, query: str) -> dict:
        """Full RAG pipeline: retrieve → generate grounded answer."""
        if not self._loaded:
            self.load()

        # Step 1: Retrieve relevant reviews
        retrieved = self.retrieve(query)

        if not retrieved:
            return {
                "answer": "I couldn't find relevant reviews matching your query. Try asking about specific topics like sizing, pricing, returns, or quality.",
                "citations": [],
                "review_count": 0
            }

        # Step 2: Build context from retrieved reviews
        context_parts = []
        citations = []
        for i, r in enumerate(retrieved):
            source = r.get("source", "Unknown")
            text = r.get("text", "")
            score = r.get("relevance_score", 0)
            idx = r.get("review_index", 0)
            context_parts.append(f"[Review #{idx}] (Source: {source}, Relevance: {score:.2f}) {text}")
            citations.append({
                "review_id": idx,
                "source": source,
                "text": text[:120] + "..." if len(text) > 120 else text,
                "score": round(score, 3)
            })

        context = "\n\n".join(context_parts)

        # Step 3: Generate answer via Groq (or extractive fallback)
        if self.client:
            try:
                answer = self._generate_with_groq(query, context, len(self.reviews))
            except Exception as e:
                print(f"[RAG] Groq generation failed: {e}")
                answer = self._extractive_fallback(query, retrieved)
        else:
            answer = self._extractive_fallback(query, retrieved)

        return {
            "answer": answer,
            "citations": citations[:5],
            "review_count": len(retrieved),
            "total_corpus": len(self.reviews)
        }

    def _generate_with_groq(self, query: str, context: str, total: int) -> str:
        """Generate a grounded answer using Groq LLM."""
        prompt = f"""You are the Discovery AI assistant for a Product Management research engine analyzing Myntra fashion e-commerce. 
You have access to {total} real user reviews collected from Google Play, Apple App Store, YouTube, and Reddit.

Your rules:
1. Answer ONLY based on the retrieved reviews below. Never make up information.
2. Cite specific review numbers (e.g., [Review #412]) when referencing evidence.
3. Be concise but insightful — think like a senior product analyst.
4. Quantify when possible (e.g., "3 out of 8 retrieved reviews mention...").
5. If the reviews don't contain relevant information, say so honestly.

Retrieved Reviews (ranked by relevance):
{context}

User Query: {query}

Provide a grounded, evidence-based answer:"""

        completion = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a product analytics AI that answers strictly based on retrieved user review evidence. You always cite review numbers."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )
        return completion.choices[0].message.content

    def _extractive_fallback(self, query: str, retrieved: list) -> str:
        """Simple extractive answer when LLM is unavailable."""
        if not retrieved:
            return "No relevant reviews found for your query."

        parts = [f"Based on {len(retrieved)} relevant reviews from our corpus of {len(self.reviews)}:\n"]
        for i, r in enumerate(retrieved[:3]):
            source = r.get("source", "Unknown")
            text = r.get("text", "")[:200]
            idx = r.get("review_index", 0)
            parts.append(f"• [Review #{idx}] ({source}): \"{text}\"")

        return "\n".join(parts)


# Singleton instance
_engine = None

def get_engine() -> RAGEngine:
    global _engine
    if _engine is None:
        _engine = RAGEngine()
        _engine.load()
    return _engine
