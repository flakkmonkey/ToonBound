# Import necessary modules
from PIL import Image, ImageDraw
import os

# Create a class for the DressUpApp
class DressUpApp:
    def __init__(self, characters_folder_path, outfit_folder_path, hairstyle_folder_path, accessory_folder_path):
        # Initialize the paths to character, outfit, hairstyle, and accessory folders
        self.characters_folder_path = characters_folder_path
        self.outfit_folder_path = outfit_folder_path
        self.hairstyle_folder_path = hairstyle_folder_path
        self.accessory_folder_path = accessory_folder_path

        # Load images from each folder and initialize variables
        self.characters = self.load_characters()
        self.current_character = None
        self.outfits = self.load_outfits()
        self.hairstyles = self.load_hairstyles()
        self.accessories = self.load_accessories()

        # Initialize variables to keep track of selected outfit, hairstyle, and accessory
        self.selected_outfit = None
        self.selected_hairstyle = None
        self.selected_accessory = None

    # Load character images from the specified folder
    def load_characters(self):
        characters = []  # Create an empty list to store the image objects
        character_files = os.listdir(self.characters_folder_path)  # Get a list of all files in the characters folder

        for character_file in character_files:  # Iterate over each filename in the list
            # Check if the file has a valid image extension
            if character_file.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                # Construct the full path to the image
                character_path = os.path.join(self.characters_folder_path, character_file)
                # Open the image and append it to the 'characters' list
                character_image = Image.open(character_path)
                characters.append(character_image)
                # Print each filename as it is processed
                print("Processed filename:", character_file)

        # Return the list of image objects
        return characters

    # Load outfit images from the specified folder
    def load_outfits(self):
        outfits = []
        outfit_files = os.listdir(self.outfit_folder_path) # Get a list of all files in the outfits folder
        
        for outfit_file in outfit_files: # Iterate over each filename in the list
            # Check if the file has a valid file extension
            if outfit_file.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                # Construct the full path to the image
                outfit_path = os.path.join(self.outfit_folder_path, outfit_file)
                # Open the image and append it to the 'outfits' list
                outfit_image = Image.open(outfit_path)
                outfits.append(outfit_image)
                # Print each filename as it is processed
                print("Processed filename:", outfit_file)
        # Return the list of image objects
        return outfits

    # Load hairstyle images from the specified folder
    def load_hairstyles(self):
        hairstyles = [] 
        hairstyle_files = os.listdir(self.hairstyle_folder_path) # Get a list of all files in the hairstyles folder

        for hairstyle_file in hairstyle_files: # Iterate over each filename in the list
            # Check if the file has a valid file extension
            if hairstyle_file.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                # Construct the full path to the image
                hairstyle_path = os.path.join(self.hairstyle_folder_path, hairstyle_file)
                # Open the image and append it to the 'hairstyles' list
                hairstyle_image = Image.open(hairstyle_path)
                hairstyles.append(hairstyle_image)
                # Print each filename as it is processed
                print("Processed filename:", hairstyle_file)
        # Return the list of image objects
        return hairstyles #Done

    # Load accessory images from the specified folder
    def load_accessories(self):
        accessories = [] 
        accessory_files = os.listdir(self.accessory_folder_path) # Get a list of all files in the accessories folder

        for accessory_file in accessory_files: # Iterate over each filename in the list
            # Check ic the file has a valid file extension
            if accessory_file.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                # Construct the full path to the image
                accessory_path = os.path.join(self.accessory_folder_path, accessory_file)
                # Open the image and append it to the 'accessories' list
                accessory_image = Image.open(accessory_path)
                accessories.append(accessory_image)
                # Print each filename as it is processed
                print("Processed filename:", accessory_file)
        # Return the list of image objects
        return accessories #Done

    # Set the current character
    def set_character(self, character_index):
        if 0 <= character_index < len(self.characters):
            self.current_character = self.characters[character_index]
            print(f"Selected character {character_index + 1}")
        else:
            print("Invalid character index")

    # Select a character from the available character images
    def select_character(self):
        print("Select character method called")  # Print a message to confirm the method is being called
        while True:
            print("Choose a character (1-N) or enter 'q' to cancel:")
            sorted_characters = sorted(self.characters, key=lambda x: os.path.basename(x.filename))
            for i, character_image in enumerate(sorted_characters):
                character_name = os.path.basename(character_image.filename)  # Extract filename from full path
                print(f"{i + 1}. {os.path.splitext(character_name)[0]}")  # Print the filename without extension

            choice = input()

            if choice.lower() == 'q':
                break
            try:
                choice = int(choice)
                if 1 <= choice <= len(sorted_characters):
                    self.set_character(choice - 1)
                    break
                else:
                    print("Invalid input. Please enter a valid character index.")
            except ValueError:
                print("Invalid input. Please enter a valid character index.")
    
    # Select an outfit for the character
    def select_outfit(self):
        while True:
            print("Choose an outfit (1-N) or enter 'q' to cancel:")
            sorted_outfits = sorted(self.outfits, key=lambda x: os.path.basename(x.filename))
            for i, outfit_image in enumerate(sorted_outfits):
                outfit_name = os.path.basename(outfit_image.filename)
                print(f"{i + 1}. {os.path.splitext(outfit_name)[0]}")
            
            choice = input()
            
            if choice.lower() == 'q':
                break
            try:
                choice = int(choice)
                if 1 <= choice <= len(sorted_outfits):
                    self.selected_outfit = choice - 1
                    print(f"Selected outfit {self.selected_outfit + 1}")
                    break
                else:
                    print("Invalid input. Please enter a valid outfit index.")
            except ValueError:
                print("Invalid input. Please enter a valid outfit index.")

    # Select a hairstyle for the character
    def select_hairstyle(self):
        while True:
            print("Choose a hairstyle (1-N) or enter 'q' to cancel:")
            sorted_hairstyles = sorted(self.hairstyles, key=lambda x: os.path.basename(x.filename))
            for i, hairstyle_image in enumerate(sorted_hairstyles):
                hairstyle_name = os.path.basename(hairstyle_image.filename)
                print(f"{i + 1}. {os.path.splitext(hairstyle_name)[0]}")
            
            choice = input()
            
            if choice.lower() == 'q':
                break
            try:
                choice = int(choice)
                if 1 <= choice <= len(sorted_hairstyles):
                    self.selected_hairstyle = choice - 1
                    print(f"Selected hairstyle {self.selected_hairstyle + 1}")
                    break
                else:
                    print("Invalid input. Please enter a valid hairstyle index.")
            except ValueError:
                print("Invalid input. Please enter a valid hairstyle index.")

    # Select an accessory for the character
    def select_accessory(self):
        while True:
            print("Choose an accessory (1-N) or enter 'q' to cancel:")
            sorted_accessories = sorted(self.accessories, key=lambda x: os.path.basename(x.filename))
            for i, accessory_image in enumerate(sorted_accessories):
                accessory_name = os.path.basename(accessory_image.filename) # Extract filename from full path
                print(f"{i + 1}. {os.path.splitext(accessory_name)[0]}") # Print the filename without extension
            
            choice = input()
            
            if choice.lower() == 'q':
                break
            try:
                choice = int(choice)
                if 1 <= choice <= len(sorted_accessories):
                    self.selected_accessory = choice - 1
                    print(f"Selected accessory {self.selected_accessory + 1}")
                    break
                else:
                    print("Invalid input. Please enter a valid accessory index.")
            except ValueError:
                print("Invalid input. Please enter a valid accessory index.")

    # Apply the selected outfit, hairstyle, and accessory to the character and display the result
    def apply_selections(self):
        if self.current_character:
            combined_image = Image.new("RGBA", self.current_character.size, (0, 0, 0, 0))

            if self.selected_outfit is not None:
                outfit = self.outfits[self.selected_outfit]
                offset = (
                    (combined_image.width - outfit.width) // 2,
                    (combined_image.height - outfit.height) // 2
                )
                combined_image.paste(outfit, offset, outfit)

            if self.selected_accessory is not None:
                accessory = self.accessories[self.selected_accessory]
                combined_image.paste(accessory, (0, 0), accessory)

            if self.selected_hairstyle is not None:
                hairstyle = self.hairstyles[self.selected_hairstyle]
                combined_image.paste(hairstyle, (0, 0), hairstyle)

            combined_image.paste(self.current_character, (0, 0), self.current_character)
            combined_image.show()

    # Reset selections made by the user
    def reset_selections(self):
        self.current_character = None
        self.selected_outfit = None
        self.selected_hairstyle = None
        self.selected_accessory = None
        print("Selections reset!")

    # Run the DressUpApp
    def run(self):
        character_selected = False
        outfit_selected = False
        hairstyle_selected = False
        accessory_selected = False

        while True:
            print("Choose an option:")
            print("1. Select a character" if not character_selected else "\033[3;34m1. Select a character\033[0m")
            print("2. Dress up with an outfit" if not outfit_selected else "\033[3;34m2. Dress up with an outfit\033[0m")
            print("3. Choose a hairstyle" if not hairstyle_selected else "\033[3;34m3. Choose a hairstyle\033[0m")
            print("4. Choose an accessory" if not accessory_selected else "\033[3;34m4. Choose an accessory\033[0m")
            print("\033[3;33m5. Apply selections and view\033[0m")
            print("\033[1;31m6. RESET SELECTIONS\033[0m")
            print("7. Quit")

            choice = input()

            if choice == '1':
                self.select_character()
                character_selected = True
            elif choice == '2':
                if not character_selected:
                    print("Please select a character first.")
                    continue
                self.select_outfit()
                outfit_selected = True
            elif choice == '3':
                if not character_selected:
                    print("Please select a character first.")
                    continue
                self.select_hairstyle()
                hairstyle_selected = True
            elif choice == '4':
                if not character_selected:
                    print("Please select a character first.")
                    continue
                self.select_accessory()
                accessory_selected = True
            elif choice == '5':
                if not (character_selected and outfit_selected and hairstyle_selected and accessory_selected):
                    print("Please select all options first.")
                    continue
                self.apply_selections()
            elif choice == '6':
                self.reset_selections()
                character_selected = False
                outfit_selected = False
                hairstyle_selected = False
                accessory_selected = False
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    # Set default folder paths for character, outfit, hairstyle, and accessory images
    characters_folder_path = "characters"
    outfit_folder_path = "outfits"
    hairstyle_folder_path = "hairstyles"
    accessory_folder_path = "accessories"

    # Create an instance of DressUpApp and run the application
    app = DressUpApp(characters_folder_path, outfit_folder_path, hairstyle_folder_path, accessory_folder_path)
    app.run()
