#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import hashlib
import sys
import os

path_to_file = sys.argv[1]
path_to_dir = sys.argv[2]


def hasher(hash_alg: str, file):
    """
    Function return hash of the input file for a given algorithm
    """
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
            item = line.split(" ", maxsplit=2)
            path = os.path.normpath(path_to_dir + r'\{}'.format(item[0]))
            hash_result = hasher(item[1], path)
            if hash_result == item[2].strip():
                print(item[0] + " OK")
            elif hash_result == "NOT FOUND":
                print(item[0] + " NOT FOUND")
            else:
                print(item[0] + " FAIL")


if __name__ == "__main__":
    main()
