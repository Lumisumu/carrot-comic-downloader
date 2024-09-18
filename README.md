# Carrot Comic Downloader

Download webcomics in an easy and customizable way. You can download the exe or run it locally with Python 3.

Originally project was started because I needed a convenient way to automate saving my favourite web comics. Project was then expanded with a graphical user interface made with Tkinter and support for using custom script to easily include your favourite web comic.

## User installation and tips

Download the project and either run it locally or compile it. Sections with instructions are below.

Click "?" buttons to see tips about program features.

If new comics have been released for supported comics, update the values in "comics.txt" file in "res" folder. If DLC has new multipanel or gif comics, add them to dlc-multipanel.txt and dlc-gifcomics.txt files that are in "res/special-comics" folder.

To use a custom script, edit the "script_custom.py" file in "res" folder. Your file must have `write_links()` function where custom script code starts.

## Errors

When error occurs, error description replaces tips on the right side of the screen. Sometimes reading command-line output is needed to find the issue.

Make sure you run the program in a location where you have write permissions, otherwise both list file creation and image saving can fail.

If downloading fails with multiple Python error messages in command-line output, you have a bad connection. Try connecting to a more stable network.

## Using custom script for downloading

To use custom downloading you have to run the project on your own computer with Python 3. See the next section for installation instructions.

Edit "script_custom.py" in "res" folder, the file has commented instructions. If the comic has multiple types of comics (multiple panels, comics in different file formats), you can use "script_carrot.py" and "script_dark.py" in "res/pyfiles" folder as examples.

## Installing and running project

Install Python 3 and pip: https://www.python.org/

Install "requests" module with pip:

```
pip install requests
```

Install "Pillow" module with pip:

```
pip install Pillow
```

Navigate to the project folder and run main.py:

```
python main.py
```

## Build executable

Install PyInstaller with pip:

```
pip install pyinstaller
```

Run in project folder:

```
pyinstaller --name=Carrot --icon=res/img/carrot-icon.ico main.py --onefile
```

## Credits and learning links

Image resizing tutorial by Atlas: https://www.youtube.com/watch?v=VnwDPa9biwc

Icon image and decoration image were generated with DALL-E 3 and edited by hand afterwards, prompt is: "Icon on white background, simple cartoony golden retriever holding a carrot in it's mouth".
