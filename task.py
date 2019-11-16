#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import hashlib
import sys

path_to_file = sys.argv[1]
path_to_dir = sys.argv[2]
#TODO: Описание к функциям

def hasher(hash_alg: str, file):
    hash_alg.lower()
    try:
        with open(file, 'rb') as a_file:
            a = a_file.read()
            if hash_alg == "md5":
                hash = hashlib.md5(a)
            elif hash_alg == "sha1":
                hash = hashlib.sha1(a)
            elif hash_alg == "sha256":
                hash = hashlib.sha256(a)
    except FileNotFoundError:
        return "NOT FOUND"
    return hash.hexdigest()


def main():
    with open(path_to_file, "r") as source_file:
        for line in source_file:
            result = line.split(" ", maxsplit=2)
            hash_result = hasher(result[1], path_to_dir + r'\{}'.format(result[0])) #TODO Форматирование строки для OS
            if hash_result == result[2].strip():
                print(result[0] + " OK")
            elif hash_result == "NOT FOUND":
                print(result[0] + " NOT FOUND")
            else:
                print(result[0] + " FAIL")


if __name__ == "__main__":
    main()
