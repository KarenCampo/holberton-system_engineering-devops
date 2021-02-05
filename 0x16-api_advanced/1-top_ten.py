#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    try:
        rq = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.
                          format(subreddit),
                          headers={'User-Agent': 'post'},
                          allow_redirects=False)
        for thread in rq.json().get('data').get('children'):
            print(thread.get('data').get('title'))
    except:
        print ("None")
