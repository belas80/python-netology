import json
import os

my_path = './lesson7_sorted'
new_file = './sorted.txt'

if os.path.exists(new_file):
    os.remove(new_file)

list_files = os.listdir(my_path)
dict_files = []


for n in list_files:
    current_file = os.path.join(my_path, n)
    with open(current_file, 'r') as f:
        current_content = f.readlines()
        current_count_line = len(current_content)
        dict_files.append({'path': current_file, 'count_line': current_count_line, 'content': current_content})

sort_files = sorted(dict_files, key=lambda x: x['count_line'])

for n in sort_files:
    with open(new_file, 'a') as f:
        f.writelines('Файл: ' + n['path'] + '\n')
        f.writelines('Количество строк:  ' + str(n['count_line']) + '\n')
        f.writelines(''.join(n['content']) + '\n\n')

print(f'Создан файл {new_file}')
