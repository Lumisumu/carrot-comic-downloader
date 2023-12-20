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
            # Determine start and finish comic numbers
            if(first != 1):
                i = first
            else:
                i = 1

            # Loop to write links in order
            while i <= last:
                module.write_links(i)
                i += 1

    else:
        # Determine start and finish comic numbers
        if(first != 1):
            i = first
        else:
            i = 1

        # Loop to write links in order
        while i <= last:
            if comic == "Pikmin 4 comic":
                if i == 19 or i == 37:
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
    extra_type = 'twopart'
    two_part = 1
    
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
                else:
                    panel_number += 1
                
            else:
                file_name = image_name + str(current_page) + file_format
                current_page += 1

            if image_link.status_code == 200:
                # Save image to the folder
                with open(f'{target_folder}{file_name}', 'wb') as file:
                    file.write(image_link.content)
                    print(style.GREEN + f'Comic download #' + str(current_page) + ' created an image with file name ' + file_name + '.' + style.RESET)

            elif image_link.status_code == 404:
                if comic == "DLC":
                    print(style.YELLOW + "Non-standard Dark Legacy Comic reached, using alternative function to download. This is normal and not an error. Comic is now downloaded in corrected format..." + style.RESET)
                    extra_type = dark.download_extras(current_page, extras_list_created)
                    extras_list_created = 1
                    extra_comics.append(current_page)
                else:
                    print(style.RED + 'Error #4: No image at url, skipping "' + file_name + '": ' + x.rstrip() + style.RESET)

            # Wait time between downloads
            time.sleep(3)

    else:
        print(style.RED + "Error #2: imagelist.txt not found.\n" + style.RESET)
    
    # DLC comic extra downloads for 2-part comics and gif comics
    if os.path.exists("imagelist-extras.txt") and extras_list_created == 1:
        # Open text file
        f = open("imagelist-extras.txt", "r")
        
        for x in f:
            # Name for next download
            image_link = rq.get(x.rstrip())

            if extra_type == "twopart" and two_part == 1:
                file_name = image_name + str(extra_comics[current_extra]) + '_1' + file_format
                two_part = 2

            elif extra_type == "twopart" and two_part == 2:
                file_name = image_name + str(extra_comics[current_extra]) + '_2' + file_format
                two_part = 1
                current_extra += 1

            elif extra_type == "gif":
                file_name = image_name + str(extra_comics[current_extra]) + ".gif"
                current_extra += 1

            if image_link.status_code == 200:
                # Save image to the folder
                with open(f'{target_folder}{file_name}', 'wb') as file:
                    file.write(image_link.content)
                    print(style.GREEN + f'Image download #' + str(current_extra) + ' finished.' + style.RESET)

            elif image_link.status_code == 404:
                print(style.RED + 'Error #4: No image at url, skipping "' + file_name + '": ' + x.rstrip() + style.RESET)

            current_page += 1

        f.close()
    
    print(style.RESET + 'Download complete, images are in the output-folder.')


if __name__ == '__main__':

    # System call for colored printed text use in command prompt
    os.system("")

    first_comic = 1
    last_comic = 9999
    comic_name_format = ''
    settings_choice = 9999
    times_asked = 2
    file_format = ".png"
    

    print(style.GREEN + "Welcome!" + style.RESET + " What comic do you want to download?")
    print("1. Pikmin 4 promotional comic")
    print("2. Dark Legacy Comic")
    print("0. Use custom script")
    comic_choice = input("Type number of your choice: ")

    match comic_choice:
        case "1":
            comic_choice = "Pikmin 4 comic"
            comic_name_format = "Pikmin 4 comic"
            last_comic = 84

        case "2":
            comic_choice = "DLC"
            comic_name_format = "DLC"
            last_comic = 886

        case "0":
            comic_choice = "Custom"
            comic_name_format = "Custom comic "

        case _:
            print(style.RED + "Error #1: Invalid input." + style.RESET)
            exit()

    # Settings choices
    while not settings_choice == "1":
        print("\nDo you want to change any settings?")
        if not times_asked == 1:
            print("1. Use default settings and continue. (Recommended)")
            times_asked = 1
        else:
            print("1. All done, continue to link list creation")
        print("2. Change image file naming format")
        print("3. Download comics from a certain range (for example, from comics #23 to #41)")
        print('4. Change filename extension (default is ".png")')
        print("0. Use existing image list")
        settings_choice = input("\nType number of your choice: ")
        
        match settings_choice:
            case "1":
                generate_image_list(comic_choice, first_comic, last_comic)
                download_images(comic_choice, first_comic, comic_name_format, file_format)

            case "2":
                comic_name_format = str(input("Type name: "))

            case "3":
                first_comic = int(input("Type the first comic number to download: "))
                print(str(first_comic))
                last_comic = int(input("Type the last comic number to download: "))
                print(str(last_comic))

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
                print(style.RED + "Error #1: Invalid input. Try again and only input a number and press Enter." + style.RESET)
