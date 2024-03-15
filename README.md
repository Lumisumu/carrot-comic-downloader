# Carrot Comic Downloader

Download webcomics in an easy and customizable way. You can download the exe or run it locally with Python 3.

Originally project was started because I needed a convenient way to download all Pikmin 4 promotional comics and save them as png instead of avif. Project was then expanded with support for Dark Legacy Comics and also for using custom scripts.

Icon was generated by DALL-E 3 with prompt: "Icon on white background, simple cartoony golden retriever holding a carrot in it's mouth"

## Installing and running program

Install Python 3 and pip: https://www.python.org/.

Install "requests" module with pip:

```
pip install requests
```

Navigate to the project folder and run main.py:

```
python main.py
```

Follow instructions. Images are saved into "output" folder.

## Build executable

Install PyInstaller with pip:

```
pip install pyinstaller
```

Run in project folder:

```
pyinstaller --icon=carrot.ico main.py --onefile
```

## Tips for user

Custom settings include using existing image link list, custom naming format, changing resulting file type and specifying the range of downloaded comics. Default file type for downloaded images is png.

If you want to use a custom script, it must be placed at the root of the project (same folder where main.py file is). Repository includes a sample custom script you can edit. Your file must have `write_links()` function where custom script code starts. You can use CustomScript.py as a template.

If you want to download only one specific comic, use custom download option number 3 and type the comic you want as both first and last comic number.

If new comics have been released for supported comics, update the number in the "comics" dictionary in main.py. You can see the comic number in the url if you open the image in a browser tab.

## Errors

Error #1: Invalid input: only use "1" or "2", do not use "." or "#". Simply enter a number and press Enter.

Error #2: Imagelist.txt not found: check if you have deleted or moved the file, check spelling in the file title.

Error #3: Writing to text file has been prevented: check if something is blocking the program from creating a text file or writing into it, check if the text file exists.

Error #4: Url does not direct to image or image can't be accessed. This can be caused by bad connection, connection blocking or image only being available for verified users. Check the url by copy-pasting it to a fresh browser.

Error #5: Custom script file import failed. Check the file name you input. Name must be written without ".py" and without quotation marks. Check that your custom script is in project root folder.

If downloading fails with multiple Python error messages, you have a bad connection. Try connecting to a more stable network.
