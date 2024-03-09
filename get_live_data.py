import requests

def fetch_summoner_id(summoner_name, api_key):
    response = requests.get(f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}')
    summoner_data = response.json()
    return summoner_data['id']

# Fetch summoner ID for a summoner
summoner_id = fetch_summoner_id('eden', 'RGAPI-66961300-3b33-434a-9718-505ac10c7b07')

def fetch_live_game_data(summoner_id, api_key):
    response = requests.get(f'https://euw1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summoner_id}?api_key={api_key}')
    game_data = response.json()
    return game_data

# Fetch live game data for a summoner
game_data = fetch_live_game_data(summoner_id, 'RGAPI-66961300-3b33-434a-9718-505ac10c7b07')

print(summoner_id)

print(game_data)