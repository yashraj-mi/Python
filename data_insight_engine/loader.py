import requests

BASE_URL = "https://dummyjson.com/posts?limit=1000&skip=0"


def fetch_posts():
    """
    Fetch raw posts data from API
    """

    try:
        response = requests.get(f"{BASE_URL}", timeout=5)

        response.raise_for_status()

        return response.json().get("posts", [])

    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return []


def load_posts():
    """
    Clean and normalize posts data
    """

    raw_posts = fetch_posts()

    processed_posts = []

    for post in raw_posts:

        processed_post = {
            "id": post.get("id"),
            "title": post.get("title"),
            "content": post.get("body"),
            "views": post.get("views", 0),
            "likes": post.get("reactions", {}).get("likes", 0),
            "dislikes": post.get("reactions", {}).get("dislikes", 0),
            "userId": post.get("userId"),
        }

        processed_posts.append(processed_post)

    return processed_posts
