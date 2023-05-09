#!/usr/bin/python3
"""0-subs defines a function number_of_subscribers that queries the
reddit api and returns number of subscribers for a specific subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for subreddit"""
    headers = {'user-Agent': 'marvinrequest'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(url, headers=headers)
    if req.status_code == 302 or req.status_code == 404:
        return 0
    req = req.json()
    if 'error' in req:
        return 0
    elif req.get('data', None) is not None:
        res = req.get('data').get('subscribers', None)
        if res is not None:
            return res
        else:
            return 0
