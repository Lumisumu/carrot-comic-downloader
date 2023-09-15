import requests as rq
import os
import time


def write_links(comic_number: int):

    nf = open("imagelist.txt", "a")

    if comic_number < 5:
        nf.write("https://assets.nintendo.com/image/upload/w_600,f_auto,q_auto/v1686959530/Microsites/PIKMIN-Portal/comics/00" +
                 str(comic_number) + "/EN/nint2402-pikmin4-manga00" + str(comic_number) + "_01" + "\n")
        nf.write("https://assets.nintendo.com/image/upload/w_600,f_auto,q_auto/v1686959530/Microsites/PIKMIN-Portal/comics/00" +
                 str(comic_number) + "/EN/nint2402-pikmin4-manga00" + str(comic_number) + "_02" + "\n")
        nf.write("https://assets.nintendo.com/image/upload/w_600,f_auto,q_auto/v1686959530/Microsites/PIKMIN-Portal/comics/00" +
                 str(comic_number) + "/EN/nint2402-pikmin4-manga00" + str(comic_number) + "_03" + "\n")
        nf.write("https://assets.nintendo.com/image/upload/w_600,f_auto,q_auto/v1686959530/Microsites/PIKMIN-Portal/comics/00" +
                 str(comic_number) + "/EN/nint2402-pikmin4-manga00" + str(comic_number) + "_04" + "\n")
        nf.write("https://assets.nintendo.com/image/upload/w_600,f_auto,q_auto/v1686959530/Microsites/PIKMIN-Portal/comics/00" +
                 str(comic_number) + "/EN/nint2402-pikmin4-manga00" + str(comic_number) + "_05")
    if comic_number == 5:
        nf.write("Link2" + "\n")
    if comic_number > 5 and comic_number < 10:
        nf.write("Link3" + "\n")
    if comic_number >= 10 and comic_number < 30:
        nf.write("Link4" + "\n")
    if comic_number >= 30:
        nf.write("Link5" + "\n")

    nf.write("" + "\n")

    nf.close()


def generate_image_list():

    print('\nAutomatic image list generation is supported up to comic #45: "The Captains Treasure". If you want the automatic generation to go beyond this, you can input the number of latest comic.')

    print("\nAutomatic option: Input " + style.GREEN + "A" +
          style.RESET + " and press Enter to use automatic generation. ")
    print('Manual option: Input ' + style.YELLOW + 'latest comic number' + style.RESET +
          ', for example "52" to use manual amount generation.')
    amount_style = input()

    if amount_style == "A":
        print("Generating automatic imagelist.txt")
        nf = open("imagelist.txt", "w")
        nf.close()
        comic_amount = 45
    else:
        print("Generating manual imagelist.txt")
        nf = open("imagelist.txt", "w")
        nf.close()
        comic_amount = int(amount_style)

    nf = open("imagelist.txt", "w")

    # Generate images in a loop
    i = 1
    while i <= int(amount_style):
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
