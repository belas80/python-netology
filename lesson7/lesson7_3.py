import json
import os

my_path = './sorted'
new_file = './sorted.txt'

list_files = os.listdir(my_path)
dict_files = []


for n in list_files:
    current_file = os.path.join(my_path, n)
    with open(current_file, 'r') as f:
        current_content = f.readlines()
        current_count_line = len(current_content)
        dict_files.append({'path': current_file, 'count_line': current_count_line, 'content': current_content})

sort_files = sorted(dict_files, key=lambda x: x['count_line'])

with open(new_file, 'w') as f:
    for n in sort_files:
        f.write('Файл: ' + n['path'] + '\n')
        f.write('Количество строк:  ' + str(n['count_line']) + '\n')
        f.write(''.join(n['content']) + '\n\n')

print(f'Создан файл {new_file}')
