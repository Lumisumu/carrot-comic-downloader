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
        print(f'Image downloaded as "{file_name}".')

if __name__ == '__main__':

    current_page = 1

    print("Welcome! Ready to create a new image list? Please backup your previous one if you want to keep it.")
    input("Press Enter to generate link list...")

    if os.path.exists("imagelist.txt"):
        os.remove("imagelist.txt")
        print("Previous link list deleted.\n")

    open('imagelist.txt', 'w').close()

    nf = open("imagelist.txt", "w")

    #TO-DO: fetch image links and generate image list

    #nf.write("Link2")
    #nf.write("\n")
    #nf.write("Link2")
        
    nf.close()

    input("Task finished. Press Enter to start download...")

    # Open text file in project folder
    f = open("imagelist.txt", "r")

    # Loops the times of lines in the text file, each line is single url that is passed to download_image function
    for x in f:
        print("\nDownloading from link:")
        print(x)
        image_name = str(current_page)
        download_image('comic/', image_name, x.rstrip())
        current_page += 1
        time.sleep(3)
    
    f.close()
