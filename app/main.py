import json


config = json.load(open("config.json"))
for key, value in config.items():
    print(key, value)
