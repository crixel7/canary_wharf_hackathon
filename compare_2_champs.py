import requests

def fetch_champion_data(champion_name):
    # Get the current version of the game
    response = requests.get('https://ddragon.leagueoflegends.com/api/versions.json')
    versions = response.json()
    current_version = versions[0]

    # Get the champion data
    response = requests.get(f'http://ddragon.leagueoflegends.com/cdn/{current_version}/data/en_US/champion/{champion_name}.json')
    champion_data = response.json()

    # Extract and return base stats
    base_stats = champion_data['data'][champion_name]['stats']
    return base_stats

def compare_champion_stats(champion1, champion2):
    # Fetch the base stats for both champions
    stats1 = fetch_champion_data(champion1)
    stats2 = fetch_champion_data(champion2)

    # Initialize a dictionary to hold the comparison results
    comparison = {}

    # Compare the base stats
    for stat in stats1.keys():
        value1 = stats1[stat]
        value2 = stats2[stat]

        # Store the comparison result in the dictionary
        comparison[stat] = {
            champion1: value1,
            champion2: value2,
            'difference': round(value1 - value2, 1)
        }

    return comparison

# Compare the base stats for Gangplank and Ashe
comparison = compare_champion_stats('Gangplank', 'Ashe')

# Print the comparison results
for stat, data in comparison.items():
    print(f"{stat}:")
    print(f"  {data['Gangplank']}")
    print(f"  {data['Ashe']}")
    print(f"  Difference: {data['difference']}")