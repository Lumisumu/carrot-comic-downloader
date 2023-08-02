import requests as rq
import os
import time


def download_image(target_folder: str, name: str, url: str):

    image_link = rq.get(url)
    file_name = name + '.png'

    # Make comic-folder it it doesn't exist yet
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Save image to target folder
    with open(f'{target_folder}{file_name}', 'wb') as file:
        file.write(image_link.content)
        print(f'Image downloaded as "{file_name}".')


if __name__ == '__main__':

    # Open text file in project folder
    f = open("imagelist.txt", "r")
    # Counter to name pages
    current_page = 1

    # Loops the times of lines in the text file, each line is single url that is passed to download_image function
    for x in f:
        print("\n Downloading from link:")
        print(x)
        image_name = str(current_page)
        download_image('comic/', image_name, x.rstrip())
        current_page += 1
        time.sleep(3)
    
    f.close()

    