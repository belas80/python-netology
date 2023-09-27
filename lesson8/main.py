import json
import xml.etree.ElementTree as ETr
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


def get_words_from_xml(file):

    parser = ETr.XMLParser(encoding='utf-8')
    tree = ETr.parse(file, parser)
    root = tree.getroot()
    news_words = []
    for e in root.findall('channel/item'):
        list_words = e.find('description').text.split()
        for w in list_words:
            if len(w) > 6:
                news_words += [w]

    return news_words


def count_words(words):

    count = {}
    for w in words:
        if count.get(w):
            count[w] += 1
        else:
            count[w] = 1

    count_sorted = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return count_sorted


def get_top_words(words, quantity=10):

    number_item = 1
    for i in words[0:quantity]:
        print(f"{number_item}. {i[0]}: {i[1]}")
        number_item += 1


print(f'\nТоп самых часто встречающихся слов длиннее 6 символов из JSON:')
words_from_json = get_words_from_json("newsafr.json")
get_top_words(count_words(words_from_json))

print(f'\nТоп самых часто встречающихся слов длиннее 6 символов из XML:')
words_from_xml = get_words_from_xml('newsafr.xml')
get_top_words(count_words(words_from_xml))

# Еще один вариант
print('\n')
print(Counter(words_from_xml).most_common(10))
