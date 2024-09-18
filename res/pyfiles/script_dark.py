# This writes links for Dark Legacy Comics

def write_links(comic_number: int):

    multi_panel_comics = []
    gif_comics = []

    # DLC special comics
    with open('res/special-comics/dlc-multipanel.txt', 'r') as file:
        lines = file.readlines()
        multi_panel_comics = [int(num) for line in lines for num in line.split(',')]

    with open('res/special-comics/dlc-gifcomics.txt', 'r') as file:
        lines = file.readlines()
        gif_comics = [int(num) for line in lines for num in line.split(',')]

    nf = open("res/imagelist.txt", "a")

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
