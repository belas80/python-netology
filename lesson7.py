import json

with open('recipes_lesson7.txt', 'r') as f:
    list_book = []
    for i in f.read().split(sep='\n\n'):
        list_book.append(i.split('\n'))

list_keys = ['ingredient_name', 'quantity', 'measure']
cook_book = {}
for line in list_book:
    cook_book[line[0]] = [dict(zip(list_keys, i.split(' | '))) for i in line[2:2 + int(line[1])]]

print(json.dumps(cook_book, ensure_ascii=False, indent=4))