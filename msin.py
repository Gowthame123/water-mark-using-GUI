from tkinter import *
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageDraw, ImageFont
import os

image_path = ""

def find_image_path(event):
    global image_path
    image_path = event.data
    if os.path.isfile(image_path) and image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        print(f"Image Path: {image_path}")
        add_watermark(image_path)

window = TkinterDnD.Tk()
window.title("Drag and Drop Image Finder")

frame = Frame(window, padx=20, pady=20)
frame.pack(padx=10, pady=10)

instruction_label = Label(frame, text="Drag and drop an image here:")
instruction_label.pack()

frame.drop_target_register(DND_FILES)
frame.dnd_bind('<<Drop>>', find_image_path)

def add_watermark(image_path, text="Codeblast"):
    try:
        image = Image.open(image_path)
        img_width, img_height = image.size

        draw_image = ImageDraw.Draw(image)

        font_path = "C:/Users/gowth/Downloads/jacinto_sans_6918798/Jacinto Sans.otf"
        font_img = ImageFont.truetype(font_path, 100)

        # Calculate text size
        text_h, text_w = img_height/4, img_width/4

        # Margin settings
        margin = 10
        x = img_width/1.4
        y = img_height/1.1

        # Draw the text on the image
        draw_image.text((x, y), text, font=font_img, fill=(255, 255, 255))

        # Save the watermarked image
        image.save("watermarked.jpg")
        image.show()
    except FileNotFoundError:
        print(f"Could not load image from {image_path}. Please verify the image file path.")
    except IOError:
        print(f"Could not load font from {font_path}. Please verify the font file path.")

window.mainloop()




