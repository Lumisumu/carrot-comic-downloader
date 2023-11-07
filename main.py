import requests as rq
import os
import time
import importlib
from importlib import util

import scripts.CarrotScript as carrot
import scripts.DarkScript as dark

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

    if(comic == "Custom"):
        script_name = input("Enter the name of the Python script (without .py file extension): ")

        find_script = util.find_spec(script_name)
        if find_script is None:
            print(style.RED + "Error #5: Custom file import failed. Check spelling.\n" + style.RESET)
            exit()
        else:
            module = importlib.import_module(script_name)
            module.write_links()

    else:
        # Determine start and finish comic numbers
        if(first != 1):
            i = first
        else:
            i = 1

        # Loop to write links in order
        while i <= last:
            if(comic == "Pikmin 4 comic"):
                carrot.write_links(i)
            elif(comic == "DLC"):
                dark.write_links(i)
            i += 1


def download_images(comic: str, current_page: int, name_format: str):

    target_folder = 'output/'
    image_name = name_format
    panel_number = 1
    image_name += str(" ")
    
    # Create comic folder if it does not exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    input("Preparation tasks finished. Press Enter to start download...")

    # Image downloading
    if os.path.exists("imagelist.txt"):
        # Open text file
        f = open("imagelist.txt", "r")

        # Loops the times of lines in the text file, each line is single url that is passed to download_image function
        for x in f:
            # Name for next download
            image_link = rq.get(x.rstrip())

            if comic == "Pikmin 4 comic":
                file_name = image_name + str(current_page) + " panel " + str(panel_number) + '.png'
                if panel_number == 5:
                    panel_number = 1
                    current_page += 1
                else:
                    panel_number += 1

            else:
                file_name = image_name + str(current_page) + '.png'
                current_page += 1

            if image_link.status_code == 200:
                # Save image to the folder
                with open(f'{target_folder}{file_name}', 'wb') as file:
                    file.write(image_link.content)
                    print(style.GREEN + f'Image download #' + str(current_page) + ' finished with file name ' + file_name + '.' + style.RESET)

            elif image_link.status_code == 404:
                print(style.RED + 'Error #4: No image at url, skipping "' + file_name + '": ' + x.rstrip() + style.RESET)

            # Wait time between downloads
            time.sleep(3)

        f.close()
        print(style.RESET + 'Download complete, images are in "comic" folder.')

    else:
        print(
            style.RED + "Error #2: imagelist.txt not found.\n" + style.RESET)


if __name__ == '__main__':

    # System call for colored printed text use in command prompt
    os.system("")

    first_comic = 1
    last_comic = 9999
    comic_name_format = ''

    print(style.GREEN + "Welcome!" + style.RESET + " What comic do you want to download?")
    print("1. Pikmin 4 promotional comic")
    print("2. Dark Legacy Comic")
    print("0. Use custom script")
    comic_choice = input("Type number of your choice: ")

    match comic_choice:
        case "1":
            comic_choice = "Pikmin 4 comic"
            comic_name_format = "Pikmin 4 comic"
            last_comic = 66

        case "2":
            comic_choice = "DLC"
            comic_name_format = "DLC"
            last_comic = 881

        case "0":
            comic_choice = "Custom"
            comic_name_format = "Custom comic "

        case _:
            print(style.RED + "Error #1: Invalid input." + style.RESET)
            exit()

    # Ask if user wants custom settings
    settings_choice = input("\nDo you want to use default download settings? Y/n: ")
    if settings_choice == "Y" or settings_choice == "y":
        print("Using default settings...")
        settings_choice = "default settings"
    elif settings_choice == "N" or settings_choice == "n":
        print("Let's configure custom settings:")
        settings_choice = "custom settings"
    else:
        print(style.RED + "Error #1: Invalid input." + style.RESET)

    match settings_choice:
        case "default settings":
            generate_image_list(comic_choice, first_comic, last_comic)
            download_images(comic_choice, first_comic, comic_name_format)

        case "custom settings":
            # Use existing list
            use_ready_list = input("Do you want to use existing image list and start download now? Y/n: ")
            if(use_ready_list == "Y" or use_ready_list == "y"):
                if os.path.exists("imagelist.txt"):
                    download_images(comic_choice, first_comic, comic_name_format)
                    print(style.RESET + "Closing program...")
                    exit()
                else:
                    print(style.RED + "Error #2: imagelist.txt not found." + style.RESET)
                    exit()

            # Use custom comic name
            use_custom_name = input("Do you want to use custom naming for downloaded images? Y/n: ")
            if(use_custom_name == "Y" or use_custom_name == "y"):
                comic_name_format = str(input("Type name: "))

            # Use download only from x to y comic number
            use_custom_amount = input("Do you want to download comics from a certain range (for example, from comics #23 to #41? Y/n: ")
            if(use_custom_amount == "Y" or use_custom_amount == "y"):
                first_comic = int(input("Type the first comic number to download: "))
                print(str(first_comic))
                last_comic = int(input("Type the last comic number to download: "))
                print(str(last_comic))
            
            generate_image_list(comic_choice, first_comic, last_comic)
            download_images(comic_choice, first_comic, comic_name_format)