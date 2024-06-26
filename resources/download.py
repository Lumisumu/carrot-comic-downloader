import requests as rq
import os
import time
import importlib
from importlib import util

def download_images(comic: str, current_page: int, name_format: str, chosen_save_location: str, stop_event):

    target_folder = chosen_save_location
    image_name = name_format + str(" ")
    panel_number = 1
    extras_list_created = 0
    current_extra = 0
    two_part = 1
    missed_downloads = 0
    multi_panel_comics = []
    gif_comics = []
    extension_name = ""

    # DLC special comics
    if comic == "Dark Legacy Comics":
        with open('resources/dlc-multipanel.txt', 'r') as file:
            lines = file.readlines()
            multi_panel_comics = [int(num) for line in lines for num in line.split(',')]
        
        with open('resources/dlc-gifcomics.txt', 'r') as file:
            lines = file.readlines()
            gif_comics = [int(num) for line in lines for num in line.split(',')]

    # Create comic folder if it does not exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    print("Starting download...\n")

    # Image downloading
    if os.path.exists("imagelist.txt"):
        # Open text file
        f = open("imagelist.txt", "r")

        # Loops the times of lines in the text file, each line is single url that is passed to download_image function
        for x in f:
            # Wait time between downloads
            time.sleep(3)

            if stop_event.is_set():
                return

            image_link = rq.get(x.rstrip())

            # Get file extension from url or replace with user input
            extension_name = x.rsplit('.', 1)[-1]
            extension_name = "." + extension_name
            extension_name = extension_name.replace("\n", "")

            # Name resulting image
            if comic == "Pikmin 4 Promotional Comic":
                file_name = image_name + str(current_page) + " panel " + str(panel_number) + extension_name
                if panel_number == 5:
                    panel_number = 1
                    current_page += 1
                    # Unused comic numbers are not used, they are skipped
                    if current_page == 19 or current_page == 37 or current_page == 91:
                        current_page += 1
                else:
                    panel_number += 1

            elif comic == "Dark Legacy Comics" and current_page in multi_panel_comics:
                file_name = image_name + str(current_page) + " panel " + str(panel_number) + extension_name
                if panel_number == 2:
                    panel_number = 1
                    current_page += 1
                else:
                    panel_number += 1

            elif comic == "Dark Legacy Comics" and current_page in gif_comics:
                file_name = image_name + str(current_page) + ".gif"
                current_page += 1
                
            else:
                file_name = image_name + str(current_page) + extension_name
                current_page += 1

            # Save image
            if image_link.status_code == 200:
                # Save image to the folder
                with open(f'{target_folder}/{file_name}', 'wb') as file:
                    file.write(image_link.content)
                    print('Comic download created an image with file name ' + file_name + '.')

            elif image_link.status_code == 404:
                print('Error #4: No image at url, skipping "' + file_name + '": ' + x.rstrip())
                missed_downloads += 1

    else:
        return("missinglist")

    print('Download complete, images are in the output-folder.\n')
    
    if missed_downloads != 0:
        print(str(missed_downloads) + " missed downloads, see above lines for comic numbers.")
        return("missed")
