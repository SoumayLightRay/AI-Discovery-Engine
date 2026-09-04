import sys

def test_play_store():
    print("\n--- Testing Google Play Scraper ---")
    try:
        from google_play_scraper import reviews, Sort
        result, _ = reviews(
            'com.myntra.android',
            lang='en',
            country='in',
            sort=Sort.NEWEST,
            count=3
        )
        print(f"Success! Found {len(result)} reviews.")
        for r in result:
            print(f"- {r['content'][:80]}...")
    except Exception as e:
        print(f"Failed: {e}")

def test_app_store():
    print("\n--- Testing App Store Scraper ---")
    try:
        from app_store_scraper import AppStore
        myntra = AppStore(country='in', app_name='myntra', app_id='907394059')
        myntra.review(how_many=3)
        print(f"Success! Found {len(myntra.reviews)} reviews.")
        for r in myntra.reviews:
            print(f"- {r['review'][:80]}...")
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    test_play_store()
    test_app_store()
