# This writes links for Dark Legacy Comics

def write_links(comic_number: int):

    multi_panel_comics = [186, 209, 370, 416, 465, 467, 471, 477]
    gif_comics = [773, 777, 792, 793, 803, 806, 818, 819, 821, 840, 843, 844, 854, 868, 876]

    nf = open("imagelist.txt", "a")

    if comic_number != None:
        if comic_number in multi_panel_comics:
            nf.write("https://www.darklegacycomics.com/comics/" + str(comic_number) + "_1" + ".jpg")
            nf.write("\n")
            nf.write("https://www.darklegacycomics.com/comics/" + str(comic_number) + "_2" + ".jpg")
            nf.write("\n")

        elif comic_number in gif_comics:
            nf.write("https://www.darklegacycomics.com/comics/" + str(comic_number) + ".gif")
            nf.write("\n")

        else:
            nf.write("https://www.darklegacycomics.com/comics/" + str(comic_number) + ".jpg")
            nf.write("\n")

    else:
        print(style.RED + "Error #3: Writing to text file failed." + style.RESET)
        
    nf.close()
