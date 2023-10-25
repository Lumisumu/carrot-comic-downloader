import requests as rq
import os
import time
import importlib

import scripts.CarrotScript as carrot
import scripts.DarkScript as dark

# Printed text colors
class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'

# Selections
comic_choice = ''

def generate_image_list(comic: str):

    if os.path.exists("imagelist.txt"):
        os.remove("imagelist.txt")

    match comic:
        # Pikmin chosen
        case "Pikmin4 comic":
            print(style.YELLOW + '\nAutomatic image list generation is supported up to comic #60: "Surprise Guest". You can manually input number of the most recent comic if this program is out of date.' + style.RESET)
            print("1. (Recommended) Use automatic list generation up until #60")
            print("2. Manually input number of the newest comic")
            amount_style = input()

            match amount_style:
                case "2":
                    print(style.YELLOW + "\nInput number of newest comic: " + style.RESET)
                    comic_amount = input()

                case _:
                    comic_amount = 60

            # Create text file
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
    image_name = comic
    image_name += str(" ")

    #print("\nDo you want to use default or custom file naming?")
    #print("1. (Recommended) Use default naming system")
    #print("2. Use your own naming")
    #naming_style = input()

    #match naming_style:
        #case "2":
            #print('Type your file name style (for example, typing "My comic" produces file names like "My comic 1")')
            #image_name = input()
            #image_name += str(" ")
        #case _:
            #match comic:
                #case "Pikmin4":
                    #image_name = str("Pikmin4 comic panel ")

                #case "DLC":
                    #image_name = str("Dark Legacy Comics ")
                
                #case "Custom":
                    #image_name = str("Comic ")

                #case _:
                    #image_name = comic

    #input("Task finished. Press Enter to start download...")

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

    # System call for colored printed text use in command prompt
    os.system("")

    print(style.GREEN + "Welcome!" + style.RESET + "What comic do you want to download?")
    print("1. Pikmin 4 promotional comic")
    print("2. Dark Legacy Comic")
    print("0. Use custom script")
    comic_choice = input("Type number of your choice: ")

    match comic_choice:
        case "1":
            comic_choice = "Pikmin4 comic"

        case "2":
            comic_choice = "DLC"

        case "0":
            comic_choice = "Custom"

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
            generate_image_list(comic_choice)
            download_images(comic_choice)

        case "custom settings":
            # Use custom comic name
            use_custom_name = input("Do you want to use custom naming for downloaded images? Y/n: ")
            if(use_ready_list == "Y" or use_ready_list == "y"):
                comic_custom_name = input('Input comic naming format (for example, "My comic"): ')
                comic_custom_name += str(" ")
                generate_image_list(comic_choice)
                download_images(comic_custom_name)

            # Use download only from x to y comic number
            use_custom_amount = input("Do you want to download comics from a certain range (for example, from comics #23 to #41? Y/n: ")
            if(use_custom_amount == "Y" or use_custom_amount == "y"):
                first_comic = input("Type the first comic number to download: ")
                last_comic = input("Type the last comic number to download: ")
                #To do: use input amounts

            # Use existing list
            use_ready_list = input("Do you want to use existing image list and start download now? Y/n: ")
            if(use_ready_list == "Y" or use_ready_list == "y"):
                if os.path.exists("imagelist.txt"):
                    download_images(comic_choice)
                    print(style.RESET + "Closing program...")
                    exit()
                else:
                    print(style.RED + "Error #2: imagelist.txt not found." + style.RESET)
                    exit()
            
            # Use custom script
            #use_custom_script = input("Do you want to use a custom script? Y/n: ")
            #if(use_custom_script == "Y" or use_custom_script == "y"):
                #generate_image_list(comic_choice)
                #download_images(comic_choice)
                #print(style.RESET + "Closing program...")
                #exit()









    # Choice of download method
    #print(style.YELLOW + "\nChoose method by typing the number and pressing Enter:" + style.RESET)
    #print("1. (Recommended) Automatic image list generation + download images")
    #print("2. Use existing image list + download images")
    #choose_feature = input()

    #match choose_feature:
        #case "1":
            #print("\nFor which comic would you like to generate a list:")
            #print("1. Pikmin 4 promotional comic")
            #print("2. Dark Legacy Comics")
            #print("0. Use custom script")
            #choose_comic = input()

            #match choose_comic:
                #case "1":
                    #print("Pikmin 4 chosen.")
                    #choose_comic = "Pikmin4"
                    #generate_image_list(choose_comic)

                #case "2":
                    #print("Dark Legacy Comics chosen.")
                    #choose_comic = "DLC"
                    #generate_image_list(choose_comic)

                #case "0":
                    #print("Custom script chosen.")
                    #choose_comic = "Custom"
                    #generate_image_list(choose_comic)
                
                #case _:
                    #print(style.RED + "Error #1: Invalid input." + style.RESET)
                    #exit()

            #download_images(choose_comic)

        #case "2":
            #if os.path.exists("imagelist.txt"):
                #download_images()
            #else:
                #print(style.RED + "Error #2: imagelist.txt not found." + style.RESET)

        #case _:
            #print(style.RED + "Error #1: Invalid input." + style.RESET)
            #exit()



    #print(style.RESET + "Closing program...")
    #exit()
