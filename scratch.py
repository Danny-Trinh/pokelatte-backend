import pokebase
import requests
import json


for x in range(1, 479):
    if 377 <= x <= 386:
        continue;
    if 144 <= x <= 146:
        continue;
    if 150 <= x <= 151:
        continue;
    if 243 <= x <= 245:
        continue;
    if 249 <= x <= 251:
        continue;
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{x}")
    data = json.loads(response.content)
    for temp in data['types']:
        if temp['type']['name'] == 'fighting':
            print('"' + data["species"]["name"] + '"' + ' ,')
            break;
# response = requests.put('http://127.0.0.1:8000/api/pokemon/level/6/', {"level": "6", "exp": "216"})
