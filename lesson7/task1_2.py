import json


def get_shop_list_by_dishes(dishes, person_count):

    result = {}
    for x in dishes:
        for y in cook_book[x]:
            if y['ingredient_name'] not in result:
                result[y['ingredient_name']] = {'measure': y['measure'], 'quantity': int(y['quantity']) * person_count}
            else:
                result.update(
                    {y['ingredient_name']:
                         {'quantity': result[y['ingredient_name']]['quantity'] + (int(y['quantity']) * person_count)}})

    return result


with open('recipes.txt', 'r') as f:
    list_book = []
    for i in f.read().split(sep='\n\n'):
        list_book.append(i.split('\n'))

list_keys = ['ingredient_name', 'quantity', 'measure']
cook_book = {}
for line in list_book:
    cook_book[line[0]] = [dict(zip(list_keys, i.split(' | '))) for i in line[2:2 + int(line[1])]]

# print(json.dumps(cook_book, ensure_ascii=False, indent=4))

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(json.dumps(shop_list, ensure_ascii=False, indent=4))