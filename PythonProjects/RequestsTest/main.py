import requests


token = 'e2c324ab176df6587689c43ab946bf29' # токен аккаунта
base_url = 'https://api.pokemonbattle.me:9104/' # адрес сайта


response_add_pokemon = requests.post(f'{base_url}pokemons', headers={'trainer_token' : token}, json={
    "name": "Бульбулька",
    "photo": "https://dolnikov.ru/pokemons/albums/004.png"
})
print(response_add_pokemon.text)


response_izm_imy = requests.put(f'{base_url}pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": "3447",
    "name": "Булька",
    "photo": "https://dolnikov.ru/pokemons/albums/007.png"
})    
print(response_izm_imy.text)


response_poimat_v_poketboll = requests.post(f'{base_url}trainers/add_pokeball', headers={'trainer_token' : token}, json={
    "pokemon_id": "3447"
})    
print(response_poimat_v_poketboll.text)


