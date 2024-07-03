# This writes links for Pikmin 4 promotional comic

def write_links(comic_number: int):

    nf = open("imagelist.txt", "a")

    # Url format for the images has changed multiple times, this part determines which url format to use and writes the link correctly

    if comic_number == 5:
        i = 1
        while i < 6:
            nf.write("https://assets.nintendo.com/image/upload/w_600,f_auto,q_auto/v1686932568/Microsites/PIKMIN-Portal/comics/00" + str(comic_number) + "/pikmin-comic-00" + str(comic_number) + "_0" + str(i))
            i += 1
            nf.write("\n")

    elif comic_number < 10:
        i = 1
        while i < 6:
            nf.write("https://assets.nintendo.com/image/upload/w_600,f_auto,q_auto/v1686959530/Microsites/PIKMIN-Portal/comics/00" + str(comic_number) + "/EN/nint2402-pikmin4-manga00" + str(comic_number) + "_0" + str(i))
            i += 1
            nf.write("\n")

    elif comic_number >= 10 and comic_number < 30:
        i = 1
        while i < 6:
            nf.write("https://assets.nintendo.com/image/upload/w_600,f_auto,q_auto/v1688141442/Microsites/PIKMIN-Portal/comics/0" + str(comic_number) + "/EN/nint2402-pikmin4-manga0" + str(comic_number) + "_0" + str(i))
            i += 1
            nf.write("\n")

    elif comic_number >= 100:
        i = 1
        while i < 6:
            nf.write("https://assets.nintendo.com/image/upload/w_600,f_auto,q_auto/v1694014678/Microsites/PIKMIN-Portal/comics/" + str(comic_number) + "/nint2402-pikmin4-manga" + str(comic_number) + "_0" + str(i))
            i += 1
            nf.write("\n")

    elif comic_number >= 30:
        i = 1
        while i < 6:
            nf.write("https://assets.nintendo.com/image/upload/w_600,f_auto,q_auto/v1694014678/Microsites/PIKMIN-Portal/comics/" + str(comic_number) + "/nint2402-pikmin4-manga0" + str(comic_number) + "_0" + str(i))
            i += 1
            nf.write("\n")

    else:
        print(style.RED + "Error #3: Writing to text file failed." + style.RESET)

    nf.close()
