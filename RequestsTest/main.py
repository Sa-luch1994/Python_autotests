import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'cbb7cc8b9afc0c5acb5342c9aee2a05c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}
body_newname = {
    "pokemon_id": "28211",
    "name": "Зефирка",
    "photo_id": 535
}
body_pokeball = {
    "pokemon_id": "28211"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

responce_newname = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_newname)
print(responce_newname.text)

responce_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball' , headers = HEADER, json = body_pokeball)
print(responce_pokeball.text)