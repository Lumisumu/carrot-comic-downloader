import requests as rq
import os
import time


def write_links(comic_number: int):

    nf = open("imagelist.txt", "a")

    if comic_number == 19 or comic_number == 37:
        # These comic numbers might be unused, no comic are found at these numbers, they are skipped
        print("Skipping unused comic number #" + str(comic_number) +
              ". This is normal procedure and not an error. Download continues from next panel...")

    elif comic_number == 5:
        i = 1
        while i < 6:
            nf.write("https://assets.nintendo.com/image/upload/w_600,f_auto,q_auto/v1686932568/Microsites/PIKMIN-Portal/comics/00" +
                     str(comic_number) + "/pikmin-comic-00" + str(comic_number) + "_0" + str(i))
            i += 1
            nf.write("\n")

    elif comic_number < 10:
        i = 1
        while i < 6:
            nf.write("https://assets.nintendo.com/image/upload/w_600,f_auto,q_auto/v1686959530/Microsites/PIKMIN-Portal/comics/00" +
                     str(comic_number) + "/EN/nint2402-pikmin4-manga00" + str(comic_number) + "_0" + str(i))
            i += 1
            nf.write("\n")

    elif comic_number >= 10 and comic_number < 30:
        i = 1
        while i < 6:
            nf.write("https://assets.nintendo.com/image/upload/w_600,f_auto,q_auto/v1688141442/Microsites/PIKMIN-Portal/comics/0" +
                     str(comic_number) + "/EN/nint2402-pikmin4-manga0" + str(comic_number) + "_0" + str(i))
            i += 1
            nf.write("\n")

    elif comic_number >= 30:
        i = 1
        while i < 6:
            nf.write("https://assets.nintendo.com/image/upload/w_600,f_auto,q_auto/v1694014678/Microsites/PIKMIN-Portal/comics/" +
                     str(comic_number) + "/nint2402-pikmin4-manga0" + str(comic_number) + "_0" + str(i))
            i += 1
            nf.write("\n")

    else:
        print("Error: no comic link written.")

    nf.close()


def generate_image_list():

    print(style.YELLOW + 'Automatic image list generation is supported up to comic #50: "Accomplished". You can manually input number of the most recent comic if this program is out of date.' + style.RESET)
    print("1. (Recommended) Use automatic list generation up until #50")
    print("2. Manually input number of the newest comic")
    amount_style = input()

    match amount_style:
        case "1":
            print("\nStarting image link list generation...")
            comic_amount = 50

        case "2":
            print(style.YELLOW + "\nInput number of newest comic: " + style.RESET)
            comic_amount = input()

        case _:
            comic_amount = 50

    # Create text file
    nf = open("imagelist.txt", "w")

    # Generate images
    i = 1
    while i <= int(comic_amount):
        if i <= 5:
            write_links(i)
        if i == 6:
            write_links(i)
        if i > 6 and i < 10:
            write_links(i)
        if i >= 10 and i < 30:
            write_links(i)
        if i >= 30:
            write_links(i)
        i += 1

    nf.close()

    input("\nTask finished. Press Enter to start download...")


def download_images():

    current_page = 1
    image_name = str("Pik4-comic-1")
    target_folder = 'comic/'

    # Image downloading
    if os.path.exists("imagelist.txt"):
        print(style.RESET + "Image link list found. Starting download...\n")

        # Open text file
        f = open("imagelist.txt", "r")

        # Loops the times of lines in the text file, each line is single url that is passed to download_image function
        for x in f:
            # Name for next download
            print(style.RESET + "Downloading comic panel number " +
                  str(current_page) + " from link: " + str(x))

            image_link = rq.get(x.rstrip())
            file_name = image_name + '.png'

            # Create comic folder if it does not exist
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            # Save image to the folder
            with open(f'{target_folder}{file_name}', 'wb') as file:
                file.write(image_link.content)
                print(style.GREEN +
                      f'Image download finished with name "{file_name}".\n' + style.RESET)

            current_page += 1
            image_name = str("Pik4-comic-")
            image_name += str(current_page)
            # Wait time between downloads
            time.sleep(3)

        # Close text file
        f.close()
        print(style.RESET + 'Download complete, check your "comic" folder.')

    else:
        print(
            "ERROR: imagelist.txt missing, add file to this folder and run main.py again.\n")


if __name__ == '__main__':

    # System call for colored printed text use in command prompt
    os.system("")

    # Printed text colors
    class style():
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        UNDERLINE = '\033[4m'
        RESET = '\033[0m'

    # Choice of download method
    print(style.YELLOW +
          "\nChoose method by typing the number and pressing Enter:" + style.RESET)
    print("1. Automatic image list generation + download images")
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
                print("Error #2: imagelist.txt not found.")

        case _:
            print("Error #1: Invalid input.")
            print(style.RESET)
            exit()

    print(style.RESET + "Closing program...")
    exit()
