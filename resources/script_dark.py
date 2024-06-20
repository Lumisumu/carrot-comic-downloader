# This writes links for Dark Legacy Comics

def write_links(comic_number: int, multi_panel_comics: list, gif_comics: list):

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
