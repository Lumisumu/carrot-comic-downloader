import requests as rq
import os
import time


def download_image(target_folder: str, name: str, image_address: str):

    image_link = rq.get(image_address)
    file_name = name + '.png'

    # Create comic folder if it does not exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Save image to the folder
    with open(f'{target_folder}{file_name}', 'wb') as file:
        file.write(image_link.content)
        print(f'Image download finished with name "{file_name}".')


if __name__ == '__main__':

    current_page = 1

    # Check for imagelist.txt in the folder
    if os.path.exists("imagelist.txt"):
        print("Image link list found. Starting download...\n")

        # Open text file
        f = open("imagelist.txt", "r")

        # Loops the times of lines in the text file, each line is single url that is passed to download_image function
        for x in f:
            # Name for next download
            image_name = str("Pik4-comic-" + current_page)
            print("\nDownloading comic panel number " +
                  current_page + " from link: " + x)
            # Call download function
            download_image('comic/', image_name, x.rstrip())
            current_page += 1
            # Wait time between downloads
            time.sleep(3)

        # Close text file
        f.close()

    else:
        print(
            "ERROR: imagelist.txt missing, add file to this folder and run main.py again.\n")
