import json
import re

with open('recipes_lesson7.txt', 'r') as f:
    result = f.read()

result  = result.split(sep='\n\n')
result2 = []
for i in result:
    result2.append(i.split('\n'))
result = result2
# list_keys = ['ingredient_name', 'quantity', 'measure']
# cook_book = [dict(zip(list_keys, i.split(' | '))) for i in result[2:2 + int(result[1])]]
# cook_book = {result[0]: cook_book}
list_keys = ['ingredient_name', 'quantity', 'measure']
cook_book = {}
for line in result:
    cook_book_tmp = [dict(zip(list_keys, i.split(' | '))) for i in line[2:2 + int(line[1])]]
    cook_book[line[0]] = cook_book_tmp

# print(cook_book)
print(json.dumps(cook_book, ensure_ascii=False, indent=4))