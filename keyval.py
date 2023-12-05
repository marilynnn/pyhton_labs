#6.	Написать key-value хранилище.

import argparse
import json

def expand_val (old_val, new_val):
    if old_val.find(new_val) != -1:
        print('This value is already stored by this key')
        return old_val
    else:
        print ('Value updated')
        return old_val + ', ' + new_val

def add_val(key, val):
    with open('storage.json', 'r') as storage:
        try:
            stor = json.load(storage)
        except 'JSONDecodeError':
            stor = {}
        if stor.get(key):
            stor[key] = expand_val(stor[key], val)
        else:
            print('Added new pair key-value')
            stor[key] = val
    with open('storage.json', 'w') as storage:
        storage.write(json.dumps(stor))

def get_val(key):
    with open('storage.json', 'r') as storage:
        try:
            stor = json.load(storage)
        except 'JSONDecodeError':
            stor = {}
        print(stor.get(key))


parser = argparse.ArgumentParser(description='Simple key-value storage')
parser.add_argument("--key", help = "add the key_name", required = 'True')
parser.add_argument("--val", help = "add the argument stored by key")
args = parser.parse_args()
if args.val:
    add_val(args.key, args.val)
else:
    get_val(args.key)






