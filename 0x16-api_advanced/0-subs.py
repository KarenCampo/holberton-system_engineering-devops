#!/usr/bin/python3
"""
Function that queries the Reddit API
and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "subscriber"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    try:
        return r.json().get("data").get("subscribers")
    except:
        return 0
