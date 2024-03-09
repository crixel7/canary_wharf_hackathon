import pytesseract
from PIL import Image

# Path to Tesseract executable (change this if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract text from an image using OCR
def extract_text_from_image(image_path):
    try:
        # Open the image
        with Image.open(image_path) as img:
            # Use Tesseract to extract text
            text = pytesseract.image_to_string(img)
            return text.strip()  # Remove leading/trailing whitespace
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

# Function to compare player and enemy champion levels
def compare_champion_levels(player_level_text, enemy_level_text):
    try:
        # Extract champion levels from text (assuming levels are in the format "Lv X")
        player_level = int(player_level_text.split()[-1])
        enemy_level = int(enemy_level_text.split()[-1])

        # Compare levels
        if player_level > enemy_level:
            print("Your champion has a higher level than the enemy!")
        elif player_level < enemy_level:
            print("Your champion has a lower level than the enemy!")
        else:
            print("Your champion and the enemy champion are at the same level!")
    except Exception as e:
        print(f"Error comparing champion levels: {e}")

# Example usage
if __name__ == "__main__":
    # Example image paths (replace these with actual paths to your images)
    player_level_image_path = "player_level.png"
    enemy_level_image_path = "enemy_level.png"

    # Extract text from images
    player_level_text = extract_text_from_image(player_level_image_path)
    enemy_level_text = extract_text_from_image(enemy_level_image_path)

    # Compare champion levels
    if player_level_text and enemy_level_text:
        compare_champion_levels(player_level_text, enemy_level_text)
