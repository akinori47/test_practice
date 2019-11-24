import os
import psutil
import time
import sys


class ListOfFiles(object):
    next_id = 0

    def __init__(self):
        self.id = ListOfFiles.next_id
        ListOfFiles.next_id += 1
        self.name = "Список файлов"

    def prep(self):
        if not int(time.time()) % 2 == 0:
            print("time since the beginning of the Unix epoch not a multiple of two")
            print("Test {} BLOCKED".format(self.name))
            sys.exit()

    @staticmethod
    def run():
        for file in os.listdir(os.getenv('HOME')):
            print(file)

    def clean_up(self):
        pass

    def execute(self):
        try:
            print('Preparing for a test {}'.format(self.name))
            self.prep()
            print('Running test {}'.format(self.name))
            self.run()
            print("Cleaning UP test {}".format(self.name))
            self.clean_up()
            print("Test {} PASSED".format(self.name))
        except OSError as error:
            print(error)
            print('Test {} FAILED'.format(self.name))


class RandomFile(object):
    next_id = 0

    def __init__(self):
        self.id = RandomFile.next_id
        RandomFile.next_id += 1
        self.name = "Cлучайный Файл"

    def prep(self):
        print('Preparing for a test')
        ram = psutil.virtual_memory().total
        ram = ram * 10 ** -9
        if ram < 1:
            print("Current RAM is lower that 1GB")
            print("{} step prep - BLOCKED".format(self.name))
            exit()
        else:
            pass

    @staticmethod
    def run():
        os.system('head -c 1MB /dev/urandom > /tmp/test')

    @staticmethod
    def clean_up():
        os.remove("/tmp/test")

    def execute(self):
        try:
            print('Preparing for a test {}'.format(self.name))
            self.prep()
            print('Running test {}'.format(self.name))
            self.run()
            print("Cleaning UP test {}".format(self.name))
            self.clean_up()
            print("Test {} PASSED".format(self.name))
        except OSError as error:
            print(error)
            print('Test {} FAILED'.format(self.name))


if __name__ == "__main__":
    list_of_files = ListOfFiles()
    random_file = RandomFile()
    ListOfFiles.execute()
    random_file.execute()
