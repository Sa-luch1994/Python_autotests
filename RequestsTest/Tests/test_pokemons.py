import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'cbb7cc8b9afc0c5acb5342c9aee2a05c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 4294

def test_status_code():
    response = requests.get(url =f'{URL}/trainers', params = {'level' : '5'})
    assert response.status_code == 200
    
def test_part_of_response():
    response_get = requests.get(url =f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID},)
    assert response_get.json()['data'][0]['trainer_name'] == 'Aleksandra'
