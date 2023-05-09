#!/usr/bin/python3
""" Script to query an API and return value """

from requests import get


def number_of_subscribers(subreddit):
    """
     function request Reddit API and returns the number of
     subscribers for a given subreddit.
     """
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    headers = {"User-Agent": "Google Chrome Version 81.0.4044.129"}
    response = get(url, headers=headers)
    data = response.json()
    resData = data.get("data").get("subscribers")

    try:
        return resData

    except Exception:
        return 0
