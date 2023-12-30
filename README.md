# Carrot Comic Downloader 2.0

Python program for downloading webcomics and converting them into PNG file format. It supports importing your own script, but it also has automated support for Pikmin 4 promotional comics and Dark Legacy Comics.

Originally project was started because I needed a convenient way to download all Pikmin 4 promotional comics and convert them from AVIF to PNG. Project was expanded with support for another comic and also for using a custom script.

# How to use

Download this repository.

Install newest Python 3 version - https://www.python.org/

Windows: open command line and navigate to the folder with this project with `cd`, run:

```
python main.py
```

Follow instructions. Images are saved into "output" folder.

Custom settings include using existing image link list, custom naming format, changing resulting file type and specifying the range of downloaded comics. Default file type for downloaded images is png.

If you want to change wait time between downloads, change amount of seconds in this line (1 at minimum is recommended): `time.sleep(3)`

Required files: You only need main.py and one script to run the program. Scripts folder has premade download scripts if you do not want to write you own. You need at least one working script to successfully download images.

Custom script must be placed at the root of the project (same folder where main.py file is) and it's name must be "CustomScript". Repository includes a sample custom script you can edit. Your file must have `write_links()` function where custom script code starts. You can take examples for files that are in scripts folder.

# Errors

Error #1: Invalid input: only use "1" or "2", do not use "." or "#". Simply enter a number and press Enter.

Error #2: Imagelist.txt not found: check if you have deleted or moved the file, check spelling in the file title.

Error #3: Writing to text file has been prevented: check if something is blocking the program from creating a text file or writing into it, check if the text file exists.

Error #4: Url does not direct to image or image can't be accessed. This can be caused by bad connection, connection blocking or image only being available for verified users. Check the url by copy-pasting it to a fresh browser.

Error #5: Custom script file import failed. Check the file name you input. Name must be written without ".py" and without quotation marks.

If downloading fails with multiple Python error messages, you have a bad connection. Try connecting to a more stable network.

# Planned improvements

- Clean and refactor code.

# Updating newest comic numbers

If new comics have been released for supported comics, update the number in the main function in main.py.
