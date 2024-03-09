import requests

def get_champion_info(api_key, champion_name):
    base_url = "https://na1.api.riotgames.com/lol/"
    summoner_url = f"{base_url}summoner/v4/summoners/by-name/{champion_name}?api_key={api_key}"
    
    try:
        summoner_response = requests.get(summoner_url)
        summoner_data = summoner_response.json()
        summoner_id = summoner_data["id"]
        
        champion_mastery_url = f"{base_url}champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}?api_key={api_key}"
        mastery_response = requests.get(champion_mastery_url)
        mastery_data = mastery_response.json()
        
        return mastery_data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def compare_champions(api_key, champion1, champion2):
    champion1_info = get_champion_info(api_key, champion1)
    champion2_info = get_champion_info(api_key, champion2)

    if champion1_info and champion2_info:
        print(f"Comparison of abilities between {champion1} and {champion2}:\n")

        for i in range(min(len(champion1_info), len(champion2_info))):
            mastery1 = champion1_info[i]
            mastery2 = champion2_info[i]

            print(f"Ability {i + 1}:\n")
            print(f"{champion1}'s ability: {mastery1}")
            print(f"{champion2}'s ability: {mastery2}")
            print("\n------------------------\n")

    else:
        print("Error fetching champion information.")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    champion1 = "Champion1Name"
    champion2 = "Champion2Name"

    compare_champions(api_key, champion1, champion2)
