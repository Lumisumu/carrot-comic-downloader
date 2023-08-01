import requests as rq
import os
import time


def download_image(target_folder: str, name: str, url: str):

    image_link = rq.get(url)
    file_name = name + '.png'

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    with open(f'{target_folder}{file_name}', 'wb') as file:
        file.write(image_link.content)
        print(f'Image downloaded as "{file_name}".')


if __name__ == '__main__':

    f = open("imagelist.txt", "r")
    current_page = 1

    for x in f:
        print("\n Downloading from link:")
        print(x)
        image_name = str(current_page)
        download_image('comic/', image_name, x.rstrip())
        current_page += 1
        time.sleep(3)
     
    f.close()

    