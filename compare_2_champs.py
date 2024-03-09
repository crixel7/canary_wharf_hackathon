import requests
from fetch_champion_data import fetch_champion_stats

def compare_champion_stats(champion1, champion2):
    # Define weights for each stat
    weights = {
        'hp': 0.2,
        'mp': 0.1,
        'attackdamage': 0.3,
        'armor': 0.15,
        'spellblock': 0.15,
        'movespeed': 0.1
        # Add more weights as needed
    }

    # Fetch the base stats for both champions
    stats1 = fetch_champion_stats(champion1)
    stats2 = fetch_champion_stats(champion2)

    # Initialize a dictionary to hold the comparison results
    comparison = {}

    # Initialize the weighted sums
    weighted_sum1 = 0
    weighted_sum2 = 0

    # Compare the base stats
    for stat in stats1.keys():
        value1 = stats1[stat]
        value2 = stats2[stat]

        # Update the weighted sums
        if stat in weights:
            weighted_sum1 += weights[stat] * value1
            weighted_sum2 += weights[stat] * value2

        # Store the comparison result in the dictionary
        comparison[stat] = {
            champion1: value1,
            champion2: value2,
            'difference': round(value1 - value2, 1)
        }

    # Determine the stronger champion
    stronger_champion = champion1 if weighted_sum1 > weighted_sum2 else champion2

    return comparison, stronger_champion

# Compare the base stats for Gangplank and Ashe
comparison, stronger_champion = compare_champion_stats('Gangplank', 'Ashe')

# Print the comparison results
for stat, data in comparison.items():
    print(f"{stat}:")
    print(f"  {data['Gangplank']}")
    print(f"  {data['Ashe']}")
    print(f"  Difference: {data['difference']}")

# Print the stronger champion
print(f"The stronger champion is {stronger_champion}")