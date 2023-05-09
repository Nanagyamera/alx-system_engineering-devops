#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, params={'limit': 100})

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        if data['data']['after'] is not None:
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list
    else:
        return None

