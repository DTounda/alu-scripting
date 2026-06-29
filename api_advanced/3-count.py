#!/usr/bin/python3
"""Parses titles of hot articles and prints sorted count of keywords."""
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    """Recursively count keyword occurrences in hot post titles."""
    if not counts:
        for word in word_list:
            word = word.lower()
            counts[word] = counts.get(word, 0)
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyBot/0.0.1"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=params)
    if response.status_code != 200:
        return
    data = response.json().get("data")
    posts = data.get("children")
    after = data.get("after")
    for post in posts:
        title = post.get("data").get("title").lower().split()
        for word in title:
            if word in counts:
                counts[word] += 1
    if after is not None:
        return count_words(subreddit, word_list, counts, after)
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        if count > 0:
            print("{}: {}".format(word, count))
