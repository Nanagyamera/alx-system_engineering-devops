#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, hot_list=None, word_count=None):
    if hot_list is None:
        hot_list = []
    if word_count is None:
        word_count = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, params={'limit': 100})

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])

        if data['data']['after'] is not None:
            return count_words(subreddit, word_list, hot_list=hot_list, word_count=word_count)
        else:
            for title in hot_list:
                words = title.lower().split()
                for word in words:
                    if word in word_list:
                        if word not in word_count:
                            word_count[word] = 1
                        else:
                            word_count[word] += 1
            for word, count in sorted(word_count.items()):
                print(f"{word}: {count}")
    else:
        print("Error: Invalid subreddit.")

