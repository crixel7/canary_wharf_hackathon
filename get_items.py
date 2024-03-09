import os
import requests

def get_latest_version():
    # Make a GET request to the data dragon API to retrieve the latest version
    response = requests.get('https://ddragon.leagueoflegends.com/api/versions.json')
    versions = response.json()

    # Get the latest version
    latest_version = versions[0]

    return latest_version

def get_items():
    # Get the latest version of the game
    latest_version = get_latest_version()

    # Make a GET request to the data dragon API to retrieve all the items
    response = requests.get(f'https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/en_US/item.json')
    data = response.json()

    # Create a folder to save the item images if it doesn't exist
    folder_path = 'item_icons'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Iterate over each item and save its image if it is purchasable
    for item_id, item_data in data['data'].items():
        item_name = item_data['name']
        image_url = f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/img/item/{item_id}.png"
        image_path = os.path.join(folder_path, f"{item_name}.png")

        # Check if the item is purchasable
        if item_data['gold']['purchasable']:
            # Check if the image already exists
            if not os.path.exists(image_path):
                # Download the image and save it to the specified path
                response = requests.get(image_url)
                with open(image_path, 'wb') as image_file:
                    image_file.write(response.content)

                print(f"Saved image for purchasable item: {item_name}")
            else:
                print(f"Skipped already saved image for item: {item_name}")
        else:
            print(f"Skipped non-purchasable item: {item_name}")

# Call the function to get the items and save their images
get_items()
