# Carrot Comic Downloader 1.3

Python program for downloading webcomics and converting them into PNG file format. It supports importing your own script, but it also has automated support for Pikmin 4 promo comics and Dark Legacy Comics. More supported comics are planned.

Originally project was started because I needed a convenient way to download all Pikmin 4 promotional comics and convert them from AVIF to PNG.

# How to use

Install Python 3.

Windows: open command line, navigate to the folder with `cd` and run:

```
python main.py
```

Follow instructions. Images are saved into "comics" folder.

# Errors

Error #1: Invalid input: only use "1" or "2", do not use "." or "#", enter number and press Enter.

Error #2: Imagelist.txt not found: check if you have deleted or moved the file, check spelling in the file title.

Error #3: Writing to text file has been prevented: check if something is blocking the program from creating a text file or writing into it, check if the text file exists.

Error #4: Url does not direct to image or image can't be accessed. This can be caused by bad connection, connection blocking or image only being available for verified users. Check the url by copy-pasting it to a fresh browser.

# Planned improvements

- Choosing target file format.
- Choosing different file names.
- Starting from input comic number and ending in input comic number.

# Updating

If new comics have been released for supported comics, update two locations in decision tree and mention in print.
