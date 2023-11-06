# This script writes links for Dark Legacy Comics

def write_links(comic_number: int):

    nf = open("imagelist.txt", "a")

    if comic_number != None:
        nf.write("https://www.darklegacycomics.com/comics/" + str(comic_number) + ".jpg")
        nf.write("\n")

    else:
        print(style.RED + "Error #3: Writing to text file failed." + style.RESET)
        
    nf.close()

def download_extras():
    multi_panel_comics = [186, 209, 370, 416, 465, 467, 471, 477]
    gif_comics = [773, 777, 792, 793, 803, 806, 818, 819, 821, 840, 843, 844, 854, 868, 876]

    if 370 in multi_panel_comics:
        print("Found 1")

    if 818 in gif_comics:
        print("Found 2")
