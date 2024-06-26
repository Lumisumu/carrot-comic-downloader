import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading as th
from pathlib import Path
import os
import threading

import resources.download as dl
import resources.generate_list as gl

stop_event = threading.Event()

def stop_process():
    print("Download process stopped.\n")
    stop_event.set()

def resize_image(event):
    global resized_tk

    # Get canvas ratio
    canvas_ratio = event.width / event.height
    
    # Check if the canvas is wider than the image
    if canvas_ratio > image_ratio:
        width = int(event.width)
        height = int(width / image_ratio)
    else:
        height = int(event.height)
        width = int(height * image_ratio)

    # Resize
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(int(event.width / 2), int(event.height / 2), anchor="center", image=resized_tk)

# Change tips label text
def show_tips(tips_selection):
    if tips_selection == "range":
        new_text = 'If both are left empty, all comics are downloaded.\n\nIf one if left empty, defaults are "1" for the first comic and the last comic number is fetched from comics.txt file in resources folder.\n\nYou can modify the latest comic number in comics.txt.'
        tips_label.configure(text=new_text)

    elif tips_selection == "naming":
        new_text = 'Example:\nWriting "funnycomic" results in files named "funnycomic 1.png", "funnycomic 2.png" and so forth.\n\nDo not use "." in the name.\n\nIf left empty, default name is used.'
        tips_label.configure(text=new_text)

    elif tips_selection == "format":
        new_text = 'Examples:\nWriting "jpg" results in .jpg files.\n\nIf left empty, .png is used.'
        tips_label.configure(text=new_text)

    elif tips_selection == "location":
        new_text = 'Examples:\nWriting "comicfolder" results in a new folder being created with this name into the programs folder.\nWriting "C:\\Users\\Public\\Pictures" downloads pictures into the Windows public images folder.\n\nSome directories cannot be saved into unless you run the program as admin.\n\nIf left empty, "output" folder is created into the same folder where Carrot Comic Downloader is.'
        tips_label.configure(text=new_text)

# Open folder where program was executed
def open_folder():
    print(Path.cwd())

    path = Path.cwd()
    os.startfile(path)

# Start download script
def start_download():
    stop_event.clear()

    file_name = ""
    first_comic = 1
    last_comic = 9999
    chosen_file_format = ".png"

    # Set file name
    if file_name_field.get() == "":
        if comic_choice.get() == 'Pikmin 4 Promotional Comic':
            file_name = "Pikmin 4 Comic"
        elif comic_choice.get() == 'Dark Legacy Comics':
            file_name = "Dark Legacy Comic"
    else:
        file_name = file_name_field.get()

    # Set first comic number to default (1) or use user input number if field is not empty
    if first_comic_field.get() == "":
        first_comic = 1
    else:
        first_comic = int(first_comic_field.get())

    # Set last comic number to comics.txt value or or use user input number if field is not empty
    if last_comic_field.get() == "":
        try:
            # Get the number of most recent comic from text file
            with open('resources/comics.txt', 'r') as file:        
                # Loop through lines in txt file
                for line in file:
                    # Split text line into comic name and number
                    comic, newest_number = line.strip().split(', ')
                    
                    if comic_choice.get() == comic:
                        last_comic = int(newest_number)
            print("\nLatest comic numbers fetched from comics.txt.")

        # In case of an error, use hardcoded values
        except:
            if comic_choice.get() == "Pikmin 4 Promotional Comic":
                last_comic = 147
            elif comic_choice.get() == "Dark Legacy Comics":
                last_comic = 902
            print('\nError #6: Failed to parse comics.txt for latest comic numbers. Program will default to hardcoded numbers. Use option "3. Download comics from a certain range" to redefine the latest comic number.')

    else:
        last_comic = int(last_comic_field.get())

    # Set file format
    if file_format_field.get() != "":
        chosen_file_format = file_format_field.get()

        # If user has not started the file format name with ".", add it to the string
        if not chosen_file_format.startswith('.'):
            chosen_file_format = '.' + chosen_file_format

    if save_location_field.get() != "":
        chosen_save_location = save_location_field.get()
    else:
        chosen_save_location = "output"

        
    # Create list and start download process
    gl.generate_image_list(comic_choice.get(), first_comic, last_comic)
    dl.download_images(comic_choice.get(), first_comic, file_name, chosen_file_format, chosen_save_location, stop_event)

# Create window, set size and window title
window = tk.Tk()
window.title("Carrot Comic Downloader 4.0")
window.geometry("950x600")
window.iconbitmap("resources/carrot-icon.ico")

# Image
image_name = "resources/dog-image.png"
image_original = Image.open(image_name)
image_ratio = image_original.size[0] / image_original.size[1]
image_tk = ImageTk.PhotoImage(image_original)

# Main grid that slips window into two parts
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.rowconfigure(0, weight = 1)

# Grid on the right side that hold image and tips label
decoration_frame = tk.Frame(window)
decoration_frame.grid(row=0, column=1, sticky="nsew")
decoration_frame.columnconfigure(0, weight=1)
decoration_frame.rowconfigure(0, weight=1)
decoration_frame.rowconfigure(1, weight=1)

# Decoration image
canvas = tk.Canvas(decoration_frame, background="red", bd=0, highlightthickness=0, width=40)
canvas.grid(row=0, column=0, sticky="nsew")
canvas.bind("<Configure>", resize_image)

# Label area for tips
tips_label = tk.Label(decoration_frame, text='Start by selecting comic in dropdown menu.\n\nTo see tips, click on the question mark buttons.\n\nIf you want to use a custom script, edit script_custom.py file in resources folder".', font=('Arial', 13), wraplength=300, height = 12, width=30)
tips_label.grid(row=1, column=0, sticky="news", padx=20)

# Grid that holds the content area for comic selection and settings
side_frame = tk.Frame(window)
side_frame.grid(row=0, column=0, sticky="nsew")
side_frame.columnconfigure(0, weight=1)
side_frame.rowconfigure(0, weight=1)
side_frame.rowconfigure(1, weight=1)
side_frame.rowconfigure(2, weight=1)
side_frame.rowconfigure(3, weight=1)
side_frame.rowconfigure(4, weight=1)
side_frame.rowconfigure(5, weight=1)
side_frame.rowconfigure(6, weight=1)
side_frame.rowconfigure(7, weight=1)

# Comic selection dropdown
selection_frame = tk.Frame(side_frame)
selection_frame.grid(row=0, column=0, sticky="nsew", pady=20)
selection_frame.columnconfigure(0, weight=1)
selection_frame.columnconfigure(1, weight=1)
selection_frame.rowconfigure(0, weight=1)

comic_selection_label = tk.Label(selection_frame, text="Select comic from dropdown:", font=('Arial', 13), height = 1).grid(row=0, column=0, sticky="nse", padx=0)

comic_options = ["Dark Legacy Comics", "Pikmin 4 Promotional Comic", "Use custom download script"]
comic_choice = tk.StringVar()
comic_choice.set(comic_options[0])
comic_choice_dropdown = tk.OptionMenu(selection_frame, comic_choice, *comic_options).grid(row=0, column=1, sticky="nws", padx=0)

# Separator
separator1 = ttk.Separator(side_frame, orient="horizontal").grid(row=1, column=0, columnspan=1, sticky="news", padx=20)

# Range selection
range_frame = tk.Frame(side_frame)
range_frame.grid(row=2, column=0, sticky="nsew")
range_frame.columnconfigure(0, weight=1)
range_frame.columnconfigure(1, weight=1)
range_frame.columnconfigure(2, weight=1)
range_frame.columnconfigure(3, weight=1)
range_frame.columnconfigure(4, weight=1)
range_frame.columnconfigure(5, weight=1)
range_frame.rowconfigure(0, weight=1)

comic_selection_label = tk.Label(range_frame, text="Range of downloaded comics:", font=('Arial', 13), height = 1)
comic_selection_label.grid(row=0, column=0, sticky="e", padx=0)
comic_selection_tips_button = tk.Button(range_frame, text="\u2753", font=('Arial', 13), height = 1, command=lambda: show_tips("range"))
comic_selection_tips_button.grid(row=0, column=1, sticky="w", padx=5)

first_comic_label = tk.Label(range_frame, text="First #:", font=('Arial', 13)).grid(row=0, column=2, sticky="e")
first_comic_field = tk.Entry(range_frame, justify="center", font=('Arial', 13), width=7)
first_comic_field.grid(row=0, column=3, sticky="w")
last_comic_label = tk.Label(range_frame, text="Last #:", font=('Arial', 13)).grid(row=0, column=4, sticky="e")
last_comic_field = tk.Entry(range_frame, justify="center", font=('Arial', 13), width=7)
last_comic_field.grid(row=0, column=5, sticky="w")

# Separator
separator2 = ttk.Separator(side_frame, orient="horizontal").grid(row=3, column=0, columnspan=1, sticky="news", padx=20, pady=5)

# Image name and save location
names_frame = tk.Frame(side_frame)
names_frame.grid(row=4, column=0, sticky="nsew", pady=20)
names_frame.columnconfigure(0, weight=1)
names_frame.columnconfigure(1, weight=1)
names_frame.columnconfigure(2, weight=1)
names_frame.rowconfigure(0, weight=1)
names_frame.rowconfigure(1, weight=1)
names_frame.rowconfigure(2, weight=1)

file_name_label = tk.Label(names_frame, text="Image naming format: ", font=('Arial', 13), height = 1).grid(row=0, column=0, sticky="e", padx=0)
file_name_field = tk.Entry(names_frame, justify="center", font=('Arial', 13))
file_name_field.grid(row=0, column=1, sticky="we", padx=0)
file_name_tips_button = tk.Button(names_frame, text="\u2753", font=('Arial', 13), height = 1, command=lambda: show_tips("naming"))
file_name_tips_button.grid(row=0, column=2, sticky="w", padx=10)

file_format_label = tk.Label(names_frame, text="File format: ", font=('Arial', 13), height = 1).grid(row=1, column=0, sticky="e", padx=0)
file_format_field = tk.Entry(names_frame, justify="center", font=('Arial', 13))
file_format_field.grid(row=1, column=1, sticky="we", padx=0)
file_format_tips_button = tk.Button(names_frame, text="\u2753", font=('Arial', 13), height = 1, command=lambda: show_tips("format"))
file_format_tips_button.grid(row=1, column=2, sticky="w", padx=10)

save_location_label = tk.Label(names_frame, text="Save location: ", font=('Arial', 13), height = 1).grid(row=2, column=0, sticky="e", padx=0)
save_location_field = tk.Entry(names_frame, justify="center", font=('Arial', 13))
save_location_field.grid(row=2, column=1, sticky="we", padx=0)
save_location_tips_button = tk.Button(names_frame, text="\u2753", font=('Arial', 13), height = 1, command=lambda: show_tips("location"))
save_location_tips_button.grid(row=2, column=2, sticky="w", padx=10)

# Separator
separator3 = ttk.Separator(side_frame, orient="horizontal").grid(row=5, column=0, columnspan=1, sticky="news", padx=20, pady=5)

# Grid for buttons
button_frame = tk.Frame(side_frame)
button_frame.grid(row=6, column=0, sticky="nsew")
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.rowconfigure(0, weight=1)

# Show folder button
folder_button = tk.Button(button_frame, text="Show folder", font=('Arial', 11), command=lambda: th.Thread(target=open_folder).start(), height = 1, width = 13)
folder_button.grid(row=0, column=0, sticky="news", padx=10, pady=20)

# Cancel button
cancel_button = tk.Button(button_frame, text="Cancel", font=('Arial', 11), height = 1, width = 13, command=stop_process, bg="#FF0000")
cancel_button.grid(row=0, column=1, sticky="news", padx=10, pady=20)

# Start button
start_button = tk.Button(button_frame, text="Start Download", font=('Arial', 14), command=lambda: th.Thread(target=start_download).start(), height = 1, width = 15, bg="#00FF00")
start_button.grid(row=0, column=2, sticky="news", padx=10)

# Start process
window.mainloop()