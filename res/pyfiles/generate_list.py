import os

import res.pyfiles.script_carrot as carrot
import res.pyfiles.script_dark as dark
import res.script_custom as custom

def generate_image_list(comic: str, first: int, last: int):

    skipped_comics = []

    try:
        with open('res/special-comics/carrot-skippedcomics.txt', 'r') as file:
            lines = file.readlines()
            skipped_comics = [int(num) for line in lines for num in line.split(',')]
    except:
        print("Reading text file failed!")

    print("Creating image url list...")

    # Delete existing text file to prevent mistakes in writing to file
    if os.path.exists("res/imagelist.txt"):
        os.remove("res/imagelist.txt")
    
    # Create new text file
    if not os.path.exists("res/imagelist.txt"):
        nf = open("res/imagelist.txt", "w")
        nf.close()

    # Use script file meant for customized list creation
    if(comic == "Use custom download script"):
        # Determine start and finish comic numbers
        if(first != 1):
            i = first
        else:
            i = 1

        # Loop to write links in order
        while i <= last:
            custom.write_links(i)
            i += 1

    # Use included, ready scripts
    else:
        # Determine start and finish comic numbers
        if(first != 1):
            i = first
        else:
            i = 1

        # Loop to write links in order
        while i <= last:
            if comic == "Pikmin 4 Promotional Comic":
                if i in skipped_comics:
                    print("Skipping unused comic number #" + str(i) + ". This is normal and not an error. No comic can be found at this number.")
                else:
                    carrot.write_links(i)
            elif comic == "Dark Legacy Comics":
                dark.write_links(i)
            i += 1