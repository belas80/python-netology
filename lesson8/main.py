import json
from pprint import pprint
from collections import Counter


def get_words_from_json(file):

    with open(file) as f:
        data = json.load(f)
        news = data['rss']['channel']['items']
        news_words = []
        for i in news:
            list_words = i['description'].split()
            for w in list_words:
                if len(w) > 6:
                    news_words += [w]

    return news_words


def get_top_words_json(words):

    count = {}
    for w in words:
        if count.get(w):
            count[w] += 1
        else:
            count[w] = 1

    count_sorted = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return count_sorted


words_from_json = get_words_from_json("newsafr.json")
top_words_json = get_top_words_json(words_from_json)

number_item = 1
for i in top_words_json[0:10]:
    print(f"{number_item}. {i[0]}: {i[1]}")
    number_item += 1

