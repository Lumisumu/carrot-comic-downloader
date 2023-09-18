import requests as rq
import os
import time


def write_links(comic_number: int):

    nf = open("imagelist.txt", "a")

    if comic_number == 19 or comic_number == 37:
        # These comic numbers might be unused, no comic are found at these numbers, they are skipped
        print("Skipping unused comic number. This is normal procedure and not an error. Download continues from next panel...")

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

    print('\nAutomatic image list generation is supported up to comic #48: "Whats He Thinking?". If you want the automatic generation to go beyond this, you can input the number of latest comic.')

    print("\nAutomatic option: Input " + style.GREEN + "A" +
          style.RESET + " and press Enter to use automatic generation. ")
    print('Manual option: Input ' + style.YELLOW + 'latest comic number' + style.RESET +
          ', for example "52" to use manual amount generation.')
    amount_style = input()

    if amount_style == "A" or amount_style == "a":
        print("\nGenerating automatic imagelist.txt")
        nf = open("imagelist.txt", "w")
        nf.close()
        comic_amount = 48
    else:
        print("\nGenerating manual imagelist.txt")
        nf = open("imagelist.txt", "w")
        nf.close()
        comic_amount = int(amount_style)

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


if __name__ == '__main__':

    current_page = 1
    image_name = str("Pik4-comic-1")
    target_folder = 'comic/'

    # System call for colored printed text use in command prompt
    os.system("")

    # Printed text colors
    class style():
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        UNDERLINE = '\033[4m'
        RESET = '\033[0m'

    print("Do you want to use automatic image list generation?")
    print("Type " + style.GREEN + "Y" + style.RESET +
          " or " + style.RED + "N" + style.RESET)
    list_choice = input()

    if list_choice == "N" or list_choice == "n":
        if os.path.exists("imagelist.txt"):
            input(
                "Image list file found. Press Enter to start downloading process...")
        if not os.path.exists("imagelist.txt"):
            print(style.RED + "\nImage list file not found." + style.RESET)
            print("\nDo you want to use automatic image list generation?")
            print("Type " + style.GREEN + "Y" + style.RESET +
                  " or " + style.RED + "N" + style.RESET)
            list_choice = input()

            if list_choice == "N" or list_choice == "n":
                print("\nN chosen. Run main.py to try again. Closing program...")
                exit()

    if list_choice == "Y" or list_choice == "y":
        if os.path.exists("imagelist.txt"):
            input(
                "Image list file already exists. Press Enter to continue with existing file...")

        if not os.path.exists("imagelist.txt"):
            generate_image_list()

        else:
            print("\nInvalid option chosen. Run main.py to try again. Closing program...")
            exit()

    # To do: if chosen "N"

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
