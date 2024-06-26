import os

import resources.script_carrot as carrot
import resources.script_dark as dark
import resources.script_custom as custom

multi_panel_comics = [186, 209, 370, 416, 465, 467, 471, 477]
gif_comics = [751, 757, 765, 773, 777, 792, 793, 803, 806, 818, 819, 821, 840, 843, 844, 854, 868, 876]

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
                dark.write_links(i, multi_panel_comics, gif_comics)
            i += 1