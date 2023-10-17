import requests as rq
import os
import time
import importlib

import scripts.CarrotScript as carrot
import scripts.DarkScript as dark


def generate_image_list(comic: str):

    match comic:
        # Pikmin chosen
        case "Pikmin4":
            print(style.YELLOW + '\nAutomatic image list generation is supported up to comic #57: "Love Seat". You can manually input number of the most recent comic if this program is out of date.' + style.RESET)
            print("1. (Recommended) Use automatic list generation up until #57")
            print("2. Manually input number of the newest comic")
            amount_style = input()

            match amount_style:
                case "1":
                    print("\nStarting image link list generation...")
                    comic_amount = 57

                case "2":
                    print(style.YELLOW + "\nInput number of newest comic: " + style.RESET)
                    comic_amount = input()

                case _:
                    comic_amount = 57

            # Create text file if it does not exist
            if not os.path.exists("imagelist.txt"):
                nf = open("imagelist.txt", "w")
                nf.close()

            # Loop through panel numbers and send them one by one to write_links function
            i = 1
            while i <= int(comic_amount):
                carrot.write_links(i)
                i += 1

            input("Task finished. Press Enter to start download...")

        # Dark Legacy Comics chosen
        case "DLC":
            print(style.YELLOW + '\nAutomatic image list generation is supported up to comic #879: "A Snail´s Pace". You can manually input number of the most recent comic if this program is out of date.' + style.RESET)
            print("1. (Recommended) Use automatic list generation up until #879")
            print("2. Manually input number of the newest comic")
            amount_style = input()

            match amount_style:
                case "1":
                    print("\nStarting image link list generation...")
                    comic_amount = 879

                case "2":
                    print(style.YELLOW + "\nInput number of newest comic: " + style.RESET)
                    comic_amount = input()

                case _:
                    comic_amount = 879

            # Create text file if it does not exist
            if not os.path.exists("imagelist.txt"):
                nf = open("imagelist.txt", "w")
                nf.close()

            # Loop through panel numbers and send them one by one to write_links function
            i = 1
            while i <= int(comic_amount):
                dark.write_links(i)
                i += 1


        # Custom script chosen
        case "Custom":
            script_name = input("Enter the name of the Python script (without .py file extension): ")
            module = importlib.import_module(script_name)
            module.write_links()


def download_images(comic: str):

    target_folder = 'output/'
    current_page = 1

    print("\nDo you want to use default or custom file naming?")
    print("1. (Recommended) Use default naming system")
    print("2. Use your own naming")
    naming_style = input()

    match naming_style:
        case "2":
            print('Type your file name style (for example, typing "My comic" produces file names like "My comic 1")')
            image_name = input()
            image_name += str(" ")
        case _:
            match comic:
                case "Pikmin4":
                    image_name = str("Pikmin4 comic panel ")

                case "DLC":
                    image_name = str("Dark Legacy Comics ")
                
                case "Custom":
                    image_name = str("Comic ")

    input("Task finished. Press Enter to start download...")

    # Create comic folder if it does not exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Image downloading
    if os.path.exists("imagelist.txt"):
        print(style.RESET + "Image link list found. Starting download...")

        # Open text file
        f = open("imagelist.txt", "r")

        # Loops the times of lines in the text file, each line is single url that is passed to download_image function
        for x in f:
            # Name for next download
            image_link = rq.get(x.rstrip())
            image_file_name = image_name
            image_file_name += str(current_page)
            file_name = image_file_name + '.png'

            if image_link.status_code == 200:
                # Save image to the folder
                with open(f'{target_folder}{file_name}', 'wb') as file:
                    file.write(image_link.content)
                    print(style.GREEN + f'Image download #' + str(current_page) + ' finished with file name ' + file_name + '.' + style.RESET)

            elif image_link.status_code == 404:
                print(style.RED + 'Error #4: No image at url, skipping "' + file_name + '": ' + x.rstrip() + style.RESET)

            current_page += 1
            # Wait time between downloads
            time.sleep(3)

        # Close text file
        f.close()
        print(style.RESET + 'Download complete, images are in "comic" folder.')

    else:
        print(
            style.RED + "Error #2: imagelist.txt not found.\n" + style.RESET)


if __name__ == '__main__':

    chosen_comic = "";

    # System call for colored printed text use in command prompt
    os.system("")

    # Printed text colors
    class style():
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        RESET = '\033[0m'

    # Choice of download method
    print(style.YELLOW + "\nChoose method by typing the number and pressing Enter:" + style.RESET)
    print("1. (Recommended) Automatic image list generation + download images")
    print("2. Use existing image list + download images")
    choose_feature = input()

    match choose_feature:
        case "1":
            print("\nFor which comic would you like to generate a list:")
            print("1. Pikmin 4 promotional comic")
            print("2. Dark Legacy Comics")
            print("0. Use custom script")
            choose_comic = input()

            match choose_comic:
                case "1":
                    print("Pikmin 4 chosen.")
                    choose_comic = "Pikmin4"
                    generate_image_list(choose_comic)

                case "2":
                    print("Dark Legacy Comics chosen.")
                    choose_comic = "DLC"
                    generate_image_list(choose_comic)

                case "0":
                    print("Custom script chosen.")
                    choose_comic = "Custom"
                    generate_image_list(choose_comic)
                
                case _:
                    print(style.RED + "Error #1: Invalid input." + style.RESET)

            download_images(choose_comic)

        case "2":
            if os.path.exists("imagelist.txt"):
                download_images()
            else:
                print(style.RED + "Error #2: imagelist.txt not found." + style.RESET)

        case _:
            print(style.RED + "Error #1: Invalid input." + style.RESET)
            exit()

    print(style.RESET + "Closing program...")
    exit()
