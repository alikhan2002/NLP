import json

# a = json.loads('О естественных монополиях.json')

with open('О естественных монополиях.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print(data)
