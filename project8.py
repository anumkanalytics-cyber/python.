from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of image paths
image_paths = [
    r"C:\Users\YuriM\Pictures\New folder (2)\Pictures\1007178.jpg",
    r"C:\Users\YuriM\Pictures\New folder (2)\Pictures\1124784.jpg",
    r"C:\Users\YuriM\Pictures\New folder (2)\Pictures\1143219.jpg",
    r"C:\Users\YuriM\Pictures\New folder (2)\Pictures\1223349.jpg",
]

# Resize images to 1080 x 1080
image_size = (1080, 1080)

images = [
    Image.open(path).resize(image_size)
    for path in image_paths
]

photo_images = [
    ImageTk.PhotoImage(img)
    for img in images
]

label = tk.Label(root)
label.pack()

slideshow = cycle(photo_images)


def update_image():
    photo = next(slideshow)
    label.config(image=photo)
    label.image = photo

    # Display the next image after 3 seconds
    root.after(3000, update_image)


def start_slideshow():
    update_image()


play_button = tk.Button(
    root,
    text="Play Slideshow",
    command=start_slideshow
)
play_button.pack()

root.mainloop()
