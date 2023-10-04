# Carrot Comic Downloader 1.2

Python program for downloading Pikmin 4 promotional comic panels and converting them from AVIF to PNG file format.

# How to use

Install Python 3.

Windows: open command line, navigate to the folder with `cd` and run:

```
python main.py
```

Follow instructions, recommended input's are "1". Images are saved into "comics" folder.

# Errors

Error #1: Invalid input: only use "1" or "2", do not use "." or "#", enter number and press Enter.

Error #2: Imagelist.txt not found: check if you have deleted or moved the file, check spelling in the file title.

Error #3: Writing to text file has been prevented: check if something is blocking the program from creating a text file or writing into it, check if the text file exists.

Error #4: Url does not direct to image or image can't be accessed. This can be caused by bad connection, connection blocking or image only being available for logged in users. Check the url by copy-pasting it to a browser.

# Updating

If new comics have been released:

- Update comic_amount variable in generate_image_list function (2 lines to change).
- Check if url format has been changed. If it is different from previous comic, update decision tree in write_links function (make new elif entry).
