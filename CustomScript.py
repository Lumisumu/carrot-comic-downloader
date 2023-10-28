# This script writes links for Dark Legacy Comics

def write_links():

    input("Custom script function called.")

    # Your custom link generation code here

    # Example:

    # Open text file for writing
    nf = open("imagelist.txt", "a")

    # Write to file
    nf.write("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Smooth_Toadfish-Tetractenos_glaber_%28mirrored%29.JPG/210px-Smooth_Toadfish-Tetractenos_glaber_%28mirrored%29.JPG")

    # Next line
    nf.write("\n")

    # Close text file
    nf.close()
