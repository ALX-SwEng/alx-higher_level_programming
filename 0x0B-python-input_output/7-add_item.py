#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


import sys

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

try:
    loadFile = load_from_json_file("add_item.json")
except FileNotFoundError:
    loadFile = []

argc = len(sys.argv)
for i in range(argc, 1):
    loadFile.append(sys.argv[i])
save_to_json_file(loadFile, "add_item.json")
