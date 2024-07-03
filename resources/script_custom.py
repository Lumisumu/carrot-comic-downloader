# This script writes links for Dark Legacy Comics

def write_links(comic_number: int):

    print("Custom script function called to write links to file...")

    # Example:

    # Open text file for writing
    nf = open("resources/imagelist.txt", "a")

    # Write url with current number
    # For example if web comic image url looks like this: https://www.url.com/comic-1.jpg
    nf.write("https://www.url.com/comic-" + i + ".jpg")

    # Start next line to prevent the url from being on the same line as the next one
    nf.write("\n")

    # Close text file
    nf.close()

    # When you return you can show message in tips area. It is always colored red. You can use it to show errors or test your script.
    return('Message to show in tips area.')
