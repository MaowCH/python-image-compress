from PIL import Image
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
# Open file dialog window and allow user to select JPEG files
root = Tk()
root.withdraw()
file_paths = askopenfilenames(filetypes=[("JPEG", "*.jpg;*.jpeg"), ("PNG", "*.png"), ("All Images", "*.*")])
# Convert each image to WebP and compress to less than 60kb
for i, file_path in enumerate(file_paths):
    # Open image
    im = Image.open(file_path)
    # Convert to WebP
    output_path = os.path.splitext(file_path)[0] + ".webp"
    im.save(output_path, "webp", quality=80, method=6)
    # Compress to less than 60kb
    while os.path.getsize(output_path) > 120000:
        quality = im.info.get('quality', 80) - 5
        im.save(output_path, "webp", quality=quality, method=6)
    print(f"Image {i+1} converted and compressed to less than 120kb.")