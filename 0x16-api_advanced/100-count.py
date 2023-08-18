#!/usr/bin/python3
"""
Queries the Reddit API and
parses the title of all hot articles,
and prints a sorted count of given keywords
"""

import requests


def count_words(subreddit, word_list):
    """Prints a sorted count of given keywords"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        hot_list = []
        for post in response.json().get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        for word in word_list:
            count = 0
            for title in hot_list:
                count += title.lower().split().count(word.lower())
            if count != 0:
                print("{}: {}".format(word.lower(), count))
    else:
        print(None)
