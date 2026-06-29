#!/usr/bin/python3
"""Returns the top ten hot posts."""
import requests


def top_ten(subreddit):
    """Query Reddit API and return the top ten hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    custom_headers = {"User-Agent": "MyApp/1.0"}
    params = {"limit": 10}
    response = requests.get(url, headers=custom_headers, allow_redirects=False, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data").get("children")
        for post in posts:
            titles = post.get("data").get("title")
            print(titles)
    else:
        print(None)
