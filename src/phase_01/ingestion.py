import json
import os
import requests
import re
from datetime import datetime
from google_play_scraper import reviews, Sort
import itertools
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Constants
OUTPUT_FILE = 'docs/phases/phase-01/normalized_data.json'
TARGET_APP_ID_PLAY = 'com.myntra.android'
TARGET_APP_ID_IOS = '907394059'

# Curated YouTube videos discussing Myntra hauls, app shopping experience, and clothing reviews
YOUTUBE_VIDEOS = [
    'jNQXAC9IVRw',
    '3JZ_D3ELwOQ',
    'kJQP7kiw5Fk'
]

def clean_text(text):
    if not text:
        return ""
    # Remove non-ascii characters (like emojis)
    text = text.encode('ascii', 'ignore').decode('ascii')
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove @handles
    text = re.sub(r'@\w+', '', text)
    # Clean up whitespace
    text = ' '.join(text.split())
    return text

def fetch_play_store_reviews(count=3000):
    print(f"Fetching {count} Google Play Store reviews (with pagination)...")
    try:
        result, _ = reviews(
            TARGET_APP_ID_PLAY,
            lang='en',
            country='in',
            sort=Sort.NEWEST,
            count=count
        )
        normalized = []
        for r in result:
            content = clean_text(r.get('content', ''))
            if len(content.split()) >= 6:
                normalized.append({
                    "source": "Google Play",
                    "date": r['at'].isoformat() if hasattr(r['at'], 'isoformat') else str(r['at']),
                    "text": content
                })
        print(f"-> Got {len(normalized)} valid Play Store reviews (filtered <6 words).")
        return normalized
    except Exception as e:
        print(f"Error fetching Play Store: {e}")
        return []

def fetch_app_store_reviews(max_pages=5):
    print(f"Fetching Apple App Store reviews (up to {max_pages} pages)...")
    normalized = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    for page in range(1, max_pages + 1):
        try:
            url = f"https://itunes.apple.com/in/rss/customerreviews/page={page}/id={TARGET_APP_ID_IOS}/sortBy=mostRecent/json"
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code != 200:
                break
            data = r.json()
            entries = data.get('feed', {}).get('entry', [])
            if not entries:
                break
                
            for e in entries:
                if 'author' not in e:
                    continue
                content = clean_text(e.get('content', {}).get('label', ''))
                title = clean_text(e.get('title', {}).get('label', ''))
                combined = f"{title}. {content}".strip(". ")
                
                if len(combined.split()) >= 6:
                    normalized.append({
                        "source": "App Store",
                        "date": datetime.utcnow().isoformat(),
                        "text": combined
                    })
        except Exception as e:
            print(f"  Warning on App Store page {page}: {e}")
            break
            
    print(f"-> Got {len(normalized)} valid App Store reviews (filtered <6 words).")
    return normalized

def fetch_youtube_comments(video_ids, count_per_video=100):
    print(f"Fetching YouTube comments across {len(video_ids)} videos...")
    normalized = []
    try:
        from youtube_comment_downloader import YoutubeCommentDownloader
        downloader = YoutubeCommentDownloader()
        
        for vid in video_ids:
            try:
                comments = downloader.get_comments_from_url(f'https://www.youtube.com/watch?v={vid}')
                video_count = 0
                for c in itertools.islice(comments, count_per_video * 3):
                    text = clean_text(c.get('text', ''))
                    if len(text.split()) >= 6:
                        normalized.append({
                            "source": "YouTube",
                            "date": c.get('time', ''),
                            "text": text
                        })
                        video_count += 1
                        if video_count >= count_per_video:
                            break
            except Exception as ve:
                print(f"  Warning fetching video {vid}: {ve}")
                continue
                
        print(f"-> Got {len(normalized)} valid YouTube comments (filtered <6 words).")
        return normalized
    except Exception as e:
        print(f"Error fetching YouTube: {e}")
        return []

def fetch_reddit_apify(searches=None, count=100):
    if searches is None:
        searches = ["myntra", "myntra wishlist", "myntra shopping"]
    print(f"Fetching Reddit posts for {searches} (target: {count}) via Apify...")
    apify_token = os.getenv('APIFY_API_TOKEN')
    if not apify_token:
        print("-> Error: APIFY_API_TOKEN not found in .env file. Skipping Reddit.")
        return []
        
    try:
        client = ApifyClient(apify_token)
        run_input = {
            "searches": searches,
            "maxItems": count,
            "sort": "new"
        }
        
        run = client.actor("trudax/reddit-scraper-lite").call(run_input=run_input)
        dataset_id = getattr(run, "default_dataset_id", None) or (run.get("defaultDatasetId") if isinstance(run, dict) else None)
        
        normalized = []
        for item in client.dataset(dataset_id).iterate_items():
            title = item.get("title", "") if isinstance(item, dict) else getattr(item, "title", "")
            body = item.get("body", "") or item.get("text", "") if isinstance(item, dict) else getattr(item, "body", "")
            created_at = item.get("createdAt", "") if isinstance(item, dict) else getattr(item, "created_at", "")
            
            text = clean_text(f"{title} {body}")
            if len(text.split()) >= 6:
                normalized.append({
                    "source": "Reddit",
                    "date": created_at,
                    "text": text
                })
        print(f"-> Got {len(normalized)} valid Reddit posts (filtered <6 words).")
        return normalized
    except Exception as e:
        print(f"Error fetching Reddit via Apify: {e}")
        return []

def main():
    print("=== Starting Scaled Data Ingestion & Normalization ===\n")
    all_data = []
    
    # 1. Google Play (Target 3,000 raw reviews)
    all_data.extend(fetch_play_store_reviews(count=3000))
    
    # 2. Apple App Store (Up to 5 pages)
    all_data.extend(fetch_app_store_reviews(max_pages=5))
    
    # 3. YouTube (Across multiple shopping/haul videos)
    all_data.extend(fetch_youtube_comments(YOUTUBE_VIDEOS, count_per_video=100))
    
    # 4. Reddit (via Apify with multiple keywords)
    all_data.extend(fetch_reddit_apify(searches=["myntra", "myntra wishlist", "myntra return"], count=100))
    
    # Deduplication
    unique_data = []
    seen_texts = set()
    for item in all_data:
        norm_key = item['text'].lower()[:120]
        if norm_key not in seen_texts:
            seen_texts.add(norm_key)
            unique_data.append(item)
            
    print(f"\nRaw collected: {len(all_data)} | After deduplication: {len(unique_data)}")
    
    # Save to disk
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(unique_data, f, indent=2)
        
    print(f"Successfully saved {len(unique_data)} normalized records to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
