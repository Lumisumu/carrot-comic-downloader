import requests as rq
import os
import time


def generate_image_list():

    comic_amount = 45

    print('\nAutomatic image list generation is supported up to comic #45: "The Captains Treasure". If you want the automatic generation to go beyond this, you can input the number of latest comic.')

    print("\nAutomatic option: Input " + style.GREEN + "A" +
          style.RESET + " and press Enter to use automatic generation. ")
    print('Manual option: Input ' + style.YELLOW + 'latest comic number' + style.RESET +
          ', for example "52" to use manual amount generation.')
    amount_style = input()

    if amount_style == "A":
        print("Generating automatic imagelist.txt")
    else:
        print("Generating manual imagelist.txt")
        comic_amount = int(amount_style)

    nf = open("imagelist.txt", "w")

    # Generate images in a loop
    i = 1
    while i <= int(comic_amount):
        if i <= 5:
            nf.write("Link1" + "\n")
        if i == 6:
            nf.write("Link2" + "\n")
        if i > 6 and i < 10:
            nf.write("Link3" + "\n")
        if i >= 10 and i < 30:
            nf.write("Link4" + "\n")
        if i >= 30:
            nf.write("Link5" + "\n")
        i += 1

    nf.close()

    input("Task finished. Press Enter to start download...")


if __name__ == '__main__':

    current_page = 1
    image_name = str("Pik4-comic-1")
    target_folder = 'comic/'

    # System call for colored printed text use in command prompt
    os.system("")

    # Printed text colors
    class style():
        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN = '\033[36m'
        WHITE = '\033[37m'
        UNDERLINE = '\033[4m'
        RESET = '\033[0m'

    print("Do you want to use automatic image list generation?")
    print("Type " + style.GREEN + "Y" + style.RESET +
          " or " + style.RED + "N" + style.RESET)
    list_choice = input()

    if list_choice == "Y":
        if not os.path.exists("imagelist.txt"):
            generate_image_list()
        if os.path.exists("imagelist.txt"):
            input(
                "Image list file already exists. Press Enter to continue with existing file...")

    # Check for imagelist.txt in the folder
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
