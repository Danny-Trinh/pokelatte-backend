import pokebase
import requests
import json


for x in range(1, 386):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{x}")
    data = json.loads(response.content)
    print('"' + data["species"]["name"] + '"' + ' ,')
