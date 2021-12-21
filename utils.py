import json


def get_keys(path, key):
    with open(path) as f:
        keys = json.load(f)
    return keys[key]
