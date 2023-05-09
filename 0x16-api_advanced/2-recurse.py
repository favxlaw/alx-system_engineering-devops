#!/usr/bin/python3
"""Script queries the Reddit api for a list containing titles"""
import requests


def recurse(subreddit, count=0, after=None, hot_list=[]):
    """
    function queries the Reddit API recursively and returns a list
    of all hot article titles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "count": count, "after": after}
    headers = {"User-Agent": "Google Chrome Version 81.0.4044.129"}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        return None

    data_ = response.json()
    titleData = data_.get('data').get('children')
    afterData = data_.get('data').get('after')

    if afterData is not None:
        after = afterData
        recurse(subreddit, hot_list)

    titleData = data_.get("data").get("children")
    for title_ in titleData:
        hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
