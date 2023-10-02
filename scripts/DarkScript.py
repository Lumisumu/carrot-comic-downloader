# This script writes links for Dark Legacy Comics

def write_links(comic_number: int):

    nf = open("imagelist.txt", "a")

    if comic_number != None:
        nf.write("https://www.darklegacycomics.com/comics/" + str(comic_number) + ".jpg")
        nf.write("\n")

    else:
        print(style.RED + "Error #3: Writing to text file failed." + style.RESET)
        
    nf.close()