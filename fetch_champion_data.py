import requests

def fetch_champion_stats(champion_name):
    # Get the current version of the game
    response = requests.get('https://ddragon.leagueoflegends.com/api/versions.json')
    versions = response.json()
    current_version = versions[0]

    # Get the champion data
    response = requests.get(f'http://ddragon.leagueoflegends.com/cdn/{current_version}/data/en_US/champion/{champion_name}.json')
    champion_data = response.json()

    # Extract base stats
    stats = champion_data['data'][champion_name]['stats']

    # Return the base stats
    return stats

# Fetch data for Gangplank
fetch_champion_stats('Gangplank')
