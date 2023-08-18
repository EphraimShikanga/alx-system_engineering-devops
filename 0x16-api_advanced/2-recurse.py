#!/usr/bin/python3
"""
Queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list containing the titles of all hot articles"""
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for post in response.json().get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        after = response.json().get('data').get('after')
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
