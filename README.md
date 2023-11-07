# Carrot Comic Downloader 1.3

Python program for downloading webcomics and converting them into PNG file format. It supports importing your own script, but it also has automated support for Pikmin 4 promo comics and Dark Legacy Comics. More supported comics are planned.

Originally project was started because I needed a convenient way to download all Pikmin 4 promotional comics and convert them from AVIF to PNG.

# How to use

Install Python 3.

Download this repository.

You need main.py to run the program. Scripts folder has premade download scripts if you do not want to write you own. You need at least one working script to successfully download images.

Windows: open command line, navigate to the folder with `cd` and run:

```
python main.py
```

Follow instructions. Images are saved into "comics" folder.

Custom settings include using existing image link list, custom naming format and specifying the range of downloaded comics.

If you want to change wait time between downloads, change amount of seconds in this line: `time.sleep(3)`

Custom script must be placed at the root of the project (same folder where main.py file is). Your file must have `write_links()` function where custom script code starts. You can take examples for files that are in scripts folder. CustomScript.py can be used in testing, it is in the root folder.

# Errors

Error #1: Invalid input: only use "1" or "2", do not use "." or "#", enter number and press Enter.

Error #2: Imagelist.txt not found: check if you have deleted or moved the file, check spelling in the file title.

Error #3: Writing to text file has been prevented: check if something is blocking the program from creating a text file or writing into it, check if the text file exists.

Error #4: Url does not direct to image or image can't be accessed. This can be caused by bad connection, connection blocking or image only being available for verified users. Check the url by copy-pasting it to a fresh browser.

Error #5: Custom script file import failed. Check the file name you input. Name must be written without ".py" and without quotation marks.

# Planned improvements

- Choosing target file format for the images.

# Updating newest comic numbers

If new comics have been released for supported comics, update the number in the main function in main.py.
