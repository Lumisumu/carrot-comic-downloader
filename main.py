import requests as rq
import os
import time
import importlib
from importlib import util

import resources.script_carrot as carrot
import resources.script_dark as dark
import resources.script_custom as custom

# Printed text colors
class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'


def generate_image_list(comic: str, first: int, last: int):

    # Delete existing text file to prevent mistakes in writing to file
    if os.path.exists("imagelist.txt"):
        os.remove("imagelist.txt")
    
    # Create new text file
    if not os.path.exists("imagelist.txt"):
        nf = open("imagelist.txt", "w")
        nf.close()

    # Use script file meant for customized list creation
    if(comic == "Custom"):
        # Determine start and finish comic numbers
        if(first != 1):
            i = first
        else:
            i = 1

        # Loop to write links in order
        while i <= last:
            custom.write_links(i)
            i += 1

    # Use included, ready scripts
    else:
        # Determine start and finish comic numbers
        if(first != 1):
            i = first
        else:
            i = 1

        # Loop to write links in order
        while i <= last:
            if comic == "Pikmin 4 comic":
                if i == 19 or i == 37 or i == 91:
                    print("Skipping unused comic number #" + str(i) + ". This is normal and not an error. No comic can be found at this number.")
                else:
                    carrot.write_links(i)
            elif comic == "DLC":
                dark.write_links(i)
            i += 1


def download_images(comic: str, current_page: int, name_format: str, file_format: str):

    target_folder = 'output/'
    image_name = name_format + str(" ")
    panel_number = 1
    extras_list_created = 0
    extra_comics = []
    current_extra = 0
    two_part = 1
    multi_panel_comics = [186, 209, 370, 416, 465, 467, 471, 477]
    gif_comics = [773, 777, 792, 793, 803, 806, 818, 819, 821, 840, 843, 844, 854, 868, 876]
    
    # Create comic folder if it does not exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    input("\nPreparation tasks finished. Press Enter to start download...")

    # Image downloading
    if os.path.exists("imagelist.txt"):
        # Open text file
        f = open("imagelist.txt", "r")

        # Loops the times of lines in the text file, each line is single url that is passed to download_image function
        for x in f:
            # Name for next download
            image_link = rq.get(x.rstrip())

            if comic == "Pikmin 4 comic":
                file_name = image_name + str(current_page) + " panel " + str(panel_number) + file_format
                if panel_number == 5:
                    panel_number = 1
                    current_page += 1
                    # Unused comic numbers are not used, they are skipped
                    if current_page == 19 or current_page == 37 or current_page == 91:
                        current_page += 1
                else:
                    panel_number += 1

            elif comic == "DLC" and current_page in multi_panel_comics:
                print(style.YELLOW + "Non-standard Dark Legacy Comic reached, downloading the comic in two parts..." + style.RESET)
                file_name = image_name + str(current_page) + " panel " + str(panel_number) + file_format
                if panel_number == 2:
                    panel_number = 1
                    current_page += 1
                else:
                    panel_number += 1

            elif comic == "DLC" and current_page in gif_comics:
                print(style.YELLOW + "Non-standard Dark Legacy Comic reached, downloading the comic in gif format..." + style.RESET)
                file_name = image_name + str(current_page) + ".gif"
                current_page += 1
                
            else:
                file_name = image_name + str(current_page) + file_format
                current_page += 1

            if image_link.status_code == 200:
                # Save image to the folder
                with open(f'{target_folder}{file_name}', 'wb') as file:
                    file.write(image_link.content)
                    print(style.GREEN + f'Comic download created an image with file name ' + file_name + '.' + style.RESET)

            elif image_link.status_code == 404:
                print(style.RED + 'Error #4: No image at url, skipping "' + file_name + '": ' + x.rstrip() + style.RESET)

            # Wait time between downloads
            time.sleep(3)

    else:
        print(style.RED + "Error #2: imagelist.txt not found.\n" + style.RESET)
    
    print(style.RESET + 'Download complete, images are in the output-folder.')


if __name__ == '__main__':

    # System call for colored printed text use in command prompt
    os.system("")

    # Comic default options, update newest comic number here
    comics = {
    "1": ("Pikmin 4 comic", "Pikmin 4 comic" , 137),
    "2": ("DLC", "DLC", 900),
    "0": ("Custom", "Custom comic", None)
    }

    first_comic = 1
    last_comic = 9999
    comic_name_format = ''
    settings_choice = 9999
    times_asked = 2
    file_format = ".png"
    
    # Comic choice
    print(style.GREEN + '''\nWelcome!''' + style.RESET + 
''' What comic do you want to download?
    1. Pikmin 4 promotional comic
    2. Dark Legacy Comic
    0. Use custom script''')

    while True:
        comic_choice = input("Choose action by typing the number: ")

        if comic_choice in comics:
            comic_choice, comic_name_format, last_comic = comics[comic_choice]
            break
        else:
            print(style.RED + "Error #1: Invalid input." + style.RESET)

    # Settings choice
    print('''
Do you want to change any settings?
    1. All done, continue to link list creation
    2. Change image file naming format
    3. Download comics from a certain range (for example, from comics #23 to #41)
    4. Change filename extension (default is ".png")
    0. Use existing image list''')

    while True:
        settings_choice = input("Choose action by typing the number: ")
        
        match settings_choice:
            case "1":
                generate_image_list(comic_choice, first_comic, last_comic)
                download_images(comic_choice, first_comic, comic_name_format, file_format)
                break

            case "2":
                comic_name_format = str(input("Type name: "))

            case "3":
                first_comic = int(input("Type the first comic number to download: "))
                last_comic = int(input("Type the last comic number to download: "))

            case "4":
                print(style.YELLOW + '\nNote! Some file extension formats may not work or may produce unexpected results. Check the first generated images in output-folder when download starts to confirm you are receiving working image files.' + style.RESET)
                file_format = input('\nType filename extension with period (".") inculded, for example ".jpg" or ".gif": ')

            case "0":
                if os.path.exists("imagelist.txt"):
                    download_images(comic_choice, first_comic, comic_name_format, file_format)
                    print(style.RESET + "Closing program...")
                    exit()
                else:
                    print(style.RED + "Error #2: imagelist.txt not found." + style.RESET)

            case _:
                print(style.RED + "Error #1: Invalid input." + style.RESET)
