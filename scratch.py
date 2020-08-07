import pokebase
import requests
import json


for x in range(1, 386):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{x}")
    data = json.loads(response.content)
    for temp in data['types']:
        if temp['type']['name'] == 'water':
            print('"' + data["species"]["name"] + '"' + ' ,')
            break;
# response = requests.put('http://127.0.0.1:8000/api/pokemon/level/6/', {"level": "6", "exp": "216"})
