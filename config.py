import json as Json
import os

def init():
    if not os.path.exists('config.json'): 
        with open('config.json', 'a') as json_file:
            Json.dump({}, json_file, indent=4)
            json_file.close()
init()

def dump():
    with open('config.json', 'w') as json_file:
        Json.dump(json, json_file, indent=4)

with open('config.json', 'r') as json_file:
    json = Json.load(json_file)

if not json.get("tokens"): json["tokens"] = []

dump()