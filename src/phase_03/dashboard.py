import streamlit as st
import json
import os
import pandas as pd
import plotly.express as px
import google.generativeai as genai
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(
    page_title="AI Discovery Engine",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Premium CSS (Dark Mode & Glassmorphism)
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #0A0A0B;
        color: #E2E8F0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Metrics Header */
    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        color: #FFFFFF !important;
        font-weight: 700;
    }
    [data-testid="stMetricLabel"] {
        color: #94A3B8 !important;
        font-size: 0.9rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Custom Opportunity Cards */
    .opp-card {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
    }
    .opp-card h3 {
        color: #A78BFA;
        margin-top: 0;
        font-size: 1.25rem;
    }
    .opp-problem {
        color: #F1F5F9;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    .opp-quote {
        background: rgba(15, 23, 42, 0.6);
        border-left: 3px solid #38BDF8;
        padding: 10px 15px;
        font-style: italic;
        color: #cbd5e1;
        font-size: 0.9rem;
        border-radius: 4px;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

DATA_PATH = "docs/phases/phase-02/analysis_results.json"

@st.cache_data
def load_data():
    if not os.path.exists(DATA_PATH):
        return None
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

data = load_data()

st.title("💎 AI Discovery Engine: Pulse Dashboard")
st.markdown("*Product Intelligence for Wishlist Conversion (Apparel & Intimates)*")
st.markdown("---")

if not data:
    st.error(f"Data file not found at {DATA_PATH}. Please run the Phase 2 analysis first.")
    st.stop()

# Layout: Metrics
col1, col2, col3 = st.columns(3)
meta = data.get("metadata", {})
with col1:
    st.metric("Total Touches Analyzed", meta.get("total_dataset_size", 0))
with col2:
    st.metric("Friction Rate", f"{meta.get('friction_rate_percentage', 0)}%")
with col3:
    st.metric("Dominant Theme", "Price / Quality")

st.markdown("---")

# Layout: Main Content
left_col, right_col = st.columns([1.2, 1])

with left_col:
    st.subheader("Top Friction Themes (% of Analyzed Sample)")
    
    # Process theme distribution for chart
    themes = meta.get("theme_distribution", {})
    df = pd.DataFrame(list(themes.items()), columns=["Theme", "Count"])
    df = df.sort_values(by="Count", ascending=True) # Ascending for horizontal bar
    
    # Plotly Bar Chart
    fig = px.bar(
        df, x="Count", y="Theme", orientation='h',
        color="Count", color_continuous_scale="Purples"
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#E2E8F0",
        margin=dict(l=0, r=0, t=0, b=0),
        height=400,
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

with right_col:
    st.subheader("Synthesized Opportunity Formulations")
    st.markdown("<br>", unsafe_allow_html=True)
    
    synthesis = data.get("synthesis", {})
    opportunities = synthesis.get("opportunities", [])
    
    for opp in opportunities[:3]:
        theme = opp.get("theme", "Theme")
        problem = opp.get("rigorous_problem_statement", "")
        quote = opp.get("grounded_quote", "")
        
        st.markdown(f"""
        <div class="opp-card">
            <h3>💡 Opportunity: {theme}</h3>
            <div class="opp-problem">{problem}</div>
            <div class="opp-quote">"{quote}"</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.subheader("🤖 Discovery AI (RAG Chatbot)")
st.markdown("Query the raw dataset of 1,367 reviews directly.")

# Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask about sizing complaints, intimate wear, etc..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        if not GEMINI_API_KEY:
            response = "Error: GEMINI_API_KEY is missing from environment."
        else:
            try:
                genai.configure(api_key=GEMINI_API_KEY)
                model = genai.GenerativeModel("gemini-1.5-flash")
                
                # Naive Context Injection for MVP Chatbot
                context = json.dumps(data.get("synthesis", {}))
                sys_prompt = f"You are a helpful product analytics AI. Answer the user's question using only this data synthesis: {context}. Be concise and cite specific quotes if available."
                
                full_prompt = f"{sys_prompt}\n\nUser: {prompt}"
                res = model.generate_content(full_prompt)
                response = res.text
            except Exception as e:
                response = f"AI Error: {str(e)}"
                
        message_placeholder.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
