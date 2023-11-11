import os

# This writes links for Dark Legacy Comics

def write_links(comic_number: int):

    nf = open("imagelist.txt", "a")

    if comic_number != None:
        nf.write("https://www.darklegacycomics.com/comics/" + str(comic_number) + ".jpg")
        nf.write("\n")

    else:
        print(style.RED + "Error #3: Writing to text file failed." + style.RESET)
        
    nf.close()

def download_extras(comic_number: int, list_created: int):
    multi_panel_comics = [186, 209, 370, 416, 465, 467, 471, 477]
    gif_comics = [773, 777, 792, 793, 803, 806, 818, 819, 821, 840, 843, 844, 854, 868, 876]

    if list_created == 0:
        # Delete existing text file to prevent mistakes in writing to file
        if os.path.exists("imagelist-extras.txt"):
            os.remove("imagelist-extras.txt")
        
        # Create new text file
        if not os.path.exists("imagelist-extras.txt"):
            nf = open("imagelist-extras.txt", "w")
            nf.close()

    nf = open("imagelist-extras.txt", "a")

    # Compare comic number to arrays to determine which type it is, then write to the extra link list
    if comic_number in multi_panel_comics:
        nf.write("https://www.darklegacycomics.com/comics/" + str(comic_number) + "_1" + ".jpg")
        nf.write("\n")
        nf.write("https://www.darklegacycomics.com/comics/" + str(comic_number) + "_2" + ".jpg")
        nf.write("\n")
        nf.close()
        return "twopart"

    elif comic_number in gif_comics:
        nf.write("https://www.darklegacycomics.com/comics/" + str(comic_number) + ".gif")
        nf.write("\n")
        nf.close()
        return "gif"