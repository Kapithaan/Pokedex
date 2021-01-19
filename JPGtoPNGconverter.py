from PIL import Image
import sys
import os


# Grab first and second arguement from the command line
image_folder = sys.argv[1]
new_folder = sys.argv[2]

# Check if new/ exists, if not create the folder
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# Loop through Pokedex to convert jpg files to png and save the files to the new folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}/{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{new_folder}/{clean_name}.png', 'png')


print('All done! JPG images have been converted to PNG!')
