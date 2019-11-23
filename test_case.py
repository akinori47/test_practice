from unittest import TestCase
import pytest
import os
import psutil

# Вывод файлов домашнего каталога Linux
for i in os.listdir(os.getenv('HOME')):
    print(i)

# Вывод кол-ва оперативной памяти
ram = psutil.virtual_memory().total
int_ram = int(ram * 10 ** -9)


# Команда для создания файла размером 1мб со случайным содержимым
os.system('head -c 1MB /dev/urandom > /tmp/test')
# Удаление файла
os.remove("/tmp/test")

class FileList(TestCase):
    next_id = 0

    def __init__(self):
        self.id = FileList.nextid
        TestCase.nextid += 1
        self.name = "Список файлов"

    def setUp(self):
        pass


