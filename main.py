import requests as rq
import os
import time


def download_image(target_folder: str, name: str, url: str):

    image_link = rq.get(url)
    file_name = name + '.png'

    # Make cfolder it it does not exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Save image to target folder
    with open(f'{target_folder}{file_name}', 'wb') as file:
        file.write(image_link.content)
        print(f'Image downloaded as "{file_name}".')

if __name__ == '__main__':

    # Make link list if it does not exist
    if not os.path.exists("imagelist.txt"):
        print("\n\nHello, welcome! imagelist.txt was not found, can I make one with Pikmin 4 urls for you?")
        input("Press Enter to generate link list file...")

        nf = open("imagelist.txt", "w")
        #nf.write("url1\nurl2")
        #To-do: check how many comics
        #To-do: Loop for generating links and saving each onto new line in text file
        
        nf.close()

        print("\nTask finished. Let's try downloading the images.")
        input("Press Enter to start download...")

    # Open text file in project folder
    f = open("imagelist.txt", "r")
    # Counter to name pages
    current_page = 1

    # Loops the times of lines in the text file, each line is single url that is passed to download_image function
    for x in f:
        print("\nDownloading from link:")
        print(x)
        image_name = str(current_page)
        download_image('comic/', image_name, x.rstrip())
        current_page += 1
        time.sleep(3)
    
    f.close()

    