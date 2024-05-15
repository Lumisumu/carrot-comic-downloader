import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading as th

import resources.download as dl

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

# Start download script
def start_download():
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
                        print("eka" + str(last_comic))
            print("\nLatest comic numbers fetched from comics.txt.")

        # In case of an error, use hardcoded values
        except:
            if comic_choice.get() == "Pikmin 4 Promotional Comic":
                last_comic = 145
            elif comic_choice.get() == "Dark Legacy Comics":
                last_comic = 902
            print('\nError #6: Failed to parse comics.txt for latest comic numbers. Program will default to hardcoded numbers. Use option "3. Download comics from a certain range" to redefine the latest comic number.')

    else:
        last_comic = int(last_comic_field.get())
        print("last" + str(last_comic))

    # Set file format
    if file_format_field.get() != "":
        chosen_file_format = file_format_field.get()

    # Create list and start download process
    dl.generate_image_list(comic_choice.get(), first_comic, last_comic)
    dl.download_images(comic_choice.get(), first_comic, file_name, chosen_file_format)

# Create window, set size and window title
window = tk.Tk()
window.title("Carrot Comic Downloader 4.0")
window.geometry("900x600")
window.iconbitmap("resources/carrot-icon.ico")

# Image
image_name = "resources/dog-image.png"
image_original = Image.open(image_name)
image_ratio = image_original.size[0] / image_original.size[1]
image_tk = ImageTk.PhotoImage(image_original)

# Main grid that slips window into two parts
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 3)
window.rowconfigure(0, weight = 1)

# Content, right side: decoration image
canvas = tk.Canvas(window, background="red", bd=0, highlightthickness=0, width=40)
canvas.grid(row=0, column=1, sticky="nsew")
canvas.bind("<Configure>", resize_image)

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
side_frame.rowconfigure(8, weight=1)
side_frame.rowconfigure(9, weight=1)
side_frame.rowconfigure(10, weight=1)

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
separator1 = ttk.Separator(side_frame, orient="horizontal").grid(row=1, column=0, columnspan=1, sticky="news", padx=20, pady=5)

# Label
comic_selection_label = tk.Label(side_frame, text="Range of downloaded comics:*", font=('Arial', 13), height = 1).grid(row=2, column=0, sticky="news", padx=0)

# Range of downloaded comics
range_frame = tk.Frame(side_frame)
range_frame.grid(row=3, column=0, sticky="news")
range_frame.columnconfigure(0, weight=1)
range_frame.columnconfigure(1, weight=1)
range_frame.columnconfigure(2, weight=1)
range_frame.columnconfigure(3, weight=1)
range_frame.rowconfigure(0, weight=1)

first_comic_label = tk.Label(range_frame, text="First #:", font=('Arial', 13)).grid(row=0, column=0, sticky="ew")
first_comic_field = tk.Entry(range_frame, justify="center", font=('Arial', 13)).grid(row=0, column=1, sticky="w")
last_comic_label = tk.Label(range_frame, text="Last #:", font=('Arial', 13)).grid(row=0, column=2, sticky="ew")
last_comic_field = tk.Entry(range_frame, justify="center", font=('Arial', 13)).grid(row=0, column=3, sticky="w")

# Label
range_note_label = tk.Label(side_frame, text="*If both left empty, all comics are downloaded.", font=('Arial', 11), wraplength=300).grid(row=4, column=0, sticky="news", padx=0)

# Separator
separator2 = ttk.Separator(side_frame, orient="horizontal").grid(row=5, column=0, columnspan=1, sticky="news", padx=20, pady=5)

# Image name and save location
names_frame = tk.Frame(side_frame)
names_frame.grid(row=6, column=0, sticky="nsew", pady=20)
names_frame.columnconfigure(0, weight=1)
names_frame.columnconfigure(1, weight=1)
names_frame.rowconfigure(0, weight=1)
names_frame.rowconfigure(1, weight=1)

file_name_label = tk.Label(names_frame, text="Image naming format:*", font=('Arial', 13), height = 1).grid(row=0, column=0, sticky="e", padx=0)
file_name_field = tk.Entry(names_frame, justify="center", font=('Arial', 13)).grid(row=0, column=1, sticky="w", padx=0)
file_format_label = tk.Label(names_frame, text="File format:*", font=('Arial', 13), height = 1).grid(row=1, column=0, sticky="e", padx=0)
file_format_field = tk.Entry(names_frame, justify="center", font=('Arial', 13)).grid(row=1, column=1, sticky="w", padx=0)

# Labels
name_note_label = tk.Label(side_frame, text="*If name is left empty, default naming is used.", font=('Arial', 11), wraplength=300).grid(row=7, column=0, sticky="news", padx=0)
save_note_label = tk.Label(side_frame, text="*If file format is left empty, .png is used.", font=('Arial', 11), wraplength=300).grid(row=8, column=0, sticky="news", padx=0)

# Separator
separator3 = ttk.Separator(side_frame, orient="horizontal").grid(row=9, column=0, columnspan=1, sticky="news", padx=20, pady=5)

# Start button
start_button = tk.Button(side_frame, text="Start Download", font=('Arial', 15), command=lambda: th.Thread(target=start_download).start(), height = 1, width = 15).grid(row=10, column=0, sticky="news", padx=80, pady=30)

# Start process
window.mainloop()