import requests
from pprint import pprint

url = "https://superheroapi.com/api/2619421814940190/search"
superheroes = ['Hulk', 'Captain America', 'Thanos']


def search_heroes(heroes):
    result = []
    for hero in heroes:
        response = requests.get('/'.join([url, hero]))
        response.raise_for_status()
        id_hero = response.json()['results'][0]['id']
        name = response.json()['results'][0]['name']
        intelligence = response.json()['results'][0]['powerstats']['intelligence']
        result.append({"id": id_hero, "name": name, "intelligence": intelligence})
    return result


def who_is_smart(heroes):
    smart_score = 0
    result = {}
    for hero in heroes:
        if int(hero['intelligence']) > smart_score:
            result = hero
    return result


if __name__ == "__main__":
    my_heroes = search_heroes(superheroes)
    pprint(my_heroes)
    smart_hero = who_is_smart(my_heroes)
    print(f'Самый умный {smart_hero["name"]}')
