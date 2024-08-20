import os
import time

directory = r'D:\Python\TestDir'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = root
        filetime = os.stat(root + '\\' + file).st_mtime
        formatted_time = time.strftime('%d.%m.%Y %H:%M, ', time.localtime(filetime))
        filesize = os.stat(root + '\\' + file).st_size
        parent_dir = root.split('\\')[-1]

    print(f'Обнаружен файл: {file},'
          f'\nПуть: {filepath},'
          f'\nВремя изменения: {formatted_time},'
          f'\nРазмер: {filesize} байт\n'
          f'Родительская директория: {parent_dir}\n')

aa = 10
