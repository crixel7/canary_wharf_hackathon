import os
import requests

def fetch_summoner_id(summoner_name, api_key):
    response = requests.get(f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}')
    summoner_data = response.json()
    return summoner_data['id']

def fetch_live_game_data(summoner_id, api_key):
    response = requests.get(f'https://euw1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summoner_id}?api_key={api_key}')
    game_data = response.json()
    return game_data

# Get the API key from an environment variable
api_key = os.getenv('RIOT_API_KEY')

# Fetch the encrypted summoner ID
summoner_id = fetch_summoner_id('eden', api_key)

# Fetch live game data
game_data = fetch_live_game_data(summoner_id, api_key)

print(summoner_id)
print(game_data)