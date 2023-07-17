import requests
import pytest

token = 'e2c324ab176df6587689c43ab946bf29' # токен аккаунта
base_url = 'https://api.pokemonbattle.me:9104/' # адрес сайта


def test_status_code():
    response = requests.get(f'{base_url}trainers', params={"trainer_id" : 1574})
    assert response.status_code == 200
    

def test_part_of_body():
    response = requests.get(f'{base_url}trainers', params={"trainer_id" : 1574})
    assert response.json()['trainer_name'] == 'Fortochka'
          
     