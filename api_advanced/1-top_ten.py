#!/usr/bin/python3
"""Returns the top ten hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Query Reddit API and print top ten hot post titles."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyBot/0.0.1"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data").get("children")
        for post in posts:
            print(post.get("data").get("title"))
    else:
        print(None)
