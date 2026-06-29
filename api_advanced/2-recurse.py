#!/usr/bin/python3
"""Returns a list of titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively query Reddit API and return all hot post titles."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyBot/0.0.1"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=params)
    if response.status_code == 200:
        data = response.json().get("data")
        posts = data.get("children")
        after = data.get("after")
        for post in posts:
            hot_list.append(post.get("data").get("title"))
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        if hot_list:
            return hot_list
        return None
