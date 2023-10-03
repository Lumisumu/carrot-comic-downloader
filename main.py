import requests as rq
import os
import time

import scripts.CarrotScript as carrot
import scripts.DarkScript as dark


def generate_image_list():

    print(style.YELLOW + '\nAutomatic image list generation is supported up to comic #51: "Ride Quality". You can manually input number of the most recent comic if this program is out of date.' + style.RESET)
    print("1. (Recommended) Use automatic list generation up until #50")
    print("2. Manually input number of the newest comic")
    amount_style = input()

    match amount_style:
        case "1":
            print("\nStarting image link list generation...")
            comic_amount = 51

        case "2":
            print(style.YELLOW + "\nInput number of newest comic: " + style.RESET)
            comic_amount = input()

        case _:
            comic_amount = 51

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


def download_images():

    target_folder = 'output/'
    current_page = 1
    image_name = str("Pik4-comic-1")

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
            file_name = image_name + '.png'

            # Save image to the folder
            with open(f'{target_folder}{file_name}', 'wb') as file:
                file.write(image_link.content)
                print(style.GREEN + f'Image download #' + str(current_page) + ' finished with file name ' + file_name + '.' + style.RESET)

            current_page += 1
            image_name = str("Pik4-comic-")
            image_name += str(current_page)
            # Wait time between downloads
            time.sleep(3)

        # Close text file
        f.close()
        print(style.RESET + 'Download complete, images are in "comic" folder.')

    else:
        print(
            style.RED + "Error #2: imagelist.txt not found.\n" + style.RESET)


if __name__ == '__main__':

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
    list_choice = input()

    match list_choice:
        case "1":
            generate_image_list()
            download_images()

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
