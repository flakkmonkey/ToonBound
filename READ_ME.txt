# ToonBound Dress-Up App

## Description
ToonBound is a dress-up application that allows users to create and customize characters by selecting outfits, hairstyles, and accessories. This Python application utilizes the PIL (Python Imaging Library) module to load and manipulate images.

## Features
- Select a character from the available character images.
- Choose an outfit, hairstyle, and accessory to dress up the selected character.
- View the combined result of the character with the selected outfit, hairstyle, and accessory.
- Reset selections made by the user.
- Quit the application.

## Usage
1. **Character Selection**: Upon running the application, the user can select a character from the available character images. Characters are displayed with their corresponding index numbers.
2. **Outfit Selection**: After selecting a character, the user can choose an outfit for the character from the available outfit images.
3. **Hairstyle Selection**: Once an outfit is selected, the user can choose a hairstyle for the character from the available hairstyle images.
4. **Accessory Selection**: After selecting a hairstyle, the user can choose an accessory for the character from the available accessory images.
5. **View Selections**: The user can apply all selections and view the combined result of the character with the chosen outfit, hairstyle, and accessory.
6. **Reset Selections**: If desired, the user can reset all selections made and start over.
7. **Quit**: At any point, the user can choose to quit the application.

## Requirements
- Python 3.x
- PIL (Python Imaging Library)

## Installation
1. Clone the repository: `git clone https://github.com/your/repository.git`
2. Navigate to the project directory.
3. Install the required packages: `pip install -r requirements.txt`
4. Run the application: `python dress_up_app.py`

## Folder Structure
- `characters`: Contains images of characters.
- `outfits`: Contains images of outfits.
- `hairstyles`: Contains images of hairstyles.
- `accessories`: Contains images of accessories.

## Notes
- Ensure that all image files have valid extensions (e.g., `.png`, `.jpg`, `.jpeg`, `.gif`) and are placed in the corresponding folders.
- Characters, outfits, hairstyles, and accessories are displayed with their filenames (excluding extensions) for selection.
- Use the numeric keypad to enter the index numbers for selection.

## License
This project is licensed under the [MIT License](LICENSE).



