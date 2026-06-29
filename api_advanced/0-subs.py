#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    url = (f"https://www.reddit.com/r/{subreddit}/about.json")
    custom_headers = {"User-Agent": "MyApp/1.0"}
    response = requests.get(url, headers=custom_headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        count = data.get("data").get("subscribers")
        return count
    else:
        return 0
