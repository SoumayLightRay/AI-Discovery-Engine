import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT')

if not client_id or client_id == 'your_client_id_here':
    print("ERROR: It looks like your .env file is missing or hasn't been updated with your real Client ID.")
    exit(1)
if not client_secret or client_secret == 'your_client_secret_here':
    print("ERROR: It looks like your .env file hasn't been updated with your real Client Secret.")
    exit(1)

try:
    import praw
    print("Connecting to Reddit API...")
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )
    
    # Test read-only access
    if reddit.read_only:
        print("Successfully connected in Read-Only mode!")
    
    subreddit = reddit.subreddit("IndianFashionAddicts")
    print(f"\nFetching top 3 posts from r/{subreddit.display_name}...")
    for submission in subreddit.hot(limit=3):
        print(f"- {submission.title[:80]}")
        
    print("\n✅ Reddit API is working perfectly!")
except Exception as e:
    print(f"\n❌ Reddit API Error: {e}")
