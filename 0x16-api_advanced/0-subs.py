#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import json
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        return json_data['data']['subscribers']
    else:
        return 0

