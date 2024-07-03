import os

import resources.pyfiles.script_carrot as carrot
import resources.pyfiles.script_dark as dark
import resources.script_custom as custom

def generate_image_list(comic: str, first: int, last: int):

    print("Creating image url list...")

    # Delete existing text file to prevent mistakes in writing to file
    if os.path.exists("imagelist.txt"):
        os.remove("imagelist.txt")
    
    # Create new text file
    if not os.path.exists("imagelist.txt"):
        nf = open("imagelist.txt", "w")
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
                if i == 19 or i == 37 or i == 91 or i == 150:
                    print("Skipping unused comic number #" + str(i) + ". This is normal and not an error. No comic can be found at this number.")
                else:
                    carrot.write_links(i)
            elif comic == "Dark Legacy Comics":
                dark.write_links(i)
            i += 1