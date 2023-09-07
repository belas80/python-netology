import json

with open('recipes_lesson7.txt', 'r') as f:
    result = f.read().splitlines()

list_keys = ['ingredient_name', 'quantity', 'measure']
cook_book = [dict(zip(list_keys, i.split(' | '))) for i in result[2:2 + int(result[1])]]
cook_book = {result[0]: cook_book}

print(result)
# print(json.dumps(cook_book, ensure_ascii=False, indent=4))