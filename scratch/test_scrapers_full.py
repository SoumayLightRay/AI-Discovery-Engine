import requests
import itertools

def test_app_store():
    print("\n--- Testing App Store (iTunes RSS) ---")
    try:
        url = "https://itunes.apple.com/in/rss/customerreviews/id=907394059/sortBy=mostRecent/json"
        r = requests.get(url)
        data = r.json()
        entries = data.get('feed', {}).get('entry', [])
        # The first entry is usually the app metadata, reviews start after that
        reviews = [e for e in entries if 'author' in e]
        print(f"Success! Fetched {len(reviews)} reviews.")
        for e in reviews[:2]:
            title = e.get('title', {}).get('label', '')
            content = e.get('content', {}).get('label', '').replace('\n', ' ')
            print(f"- [{title}] {content[:80]}...")
    except Exception as e:
        print(f"Failed: {e}")

def test_reddit():
    print("\n--- Testing Reddit (.json API) ---")
    try:
        url = "https://www.reddit.com/r/IndianFashionAddicts/search.json?q=myntra&restrict_sr=on&sort=new"
        # Reddit requires a custom User-Agent to avoid 429 Too Many Requests
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AI-Discovery-Engine/1.0'}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            data = r.json()
            posts = data.get('data', {}).get('children', [])
            print(f"Success! Fetched {len(posts)} posts.")
            for p in posts[:2]:
                title = p['data'].get('title', '').replace('\n', ' ')
                print(f"- {title[:100]}...")
        else:
            print(f"Failed with status code {r.status_code}")
    except Exception as e:
        print(f"Failed: {e}")

def test_youtube():
    print("\n--- Testing YouTube (youtube-comment-downloader) ---")
    try:
        from youtube_comment_downloader import YoutubeCommentDownloader
        downloader = YoutubeCommentDownloader()
        # Testing on a known Myntra haul video: e.g. "Myntra Haul" 
        # Using a dummy ID if we don't have one, but let's try a real popular fashion video ID if possible, 
        # or just standard "Me at the zoo" (jNQXAC9IVRw) to prove it works
        video_id = 'jNQXAC9IVRw'
        comments = downloader.get_comments_from_url(f'https://www.youtube.com/watch?v={video_id}')
        
        print(f"Success! Fetching stream...")
        # Get first 2 comments from the generator
        first_two = list(itertools.islice(comments, 2))
        print(f"Successfully downloaded {len(first_two)} comments!")
        for c in first_two:
            text = c.get('text', '').replace('\n', ' ')
            print(f"- {text[:80]}...")
    except ImportError:
        print("Failed: youtube_comment_downloader not installed.")
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    test_app_store()
    test_reddit()
    test_youtube()
