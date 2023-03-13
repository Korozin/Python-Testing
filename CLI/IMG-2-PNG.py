from PIL import Image
import os

def convert_to_png(image_path):
    # Open the image file and convert it to RGBA format
    with Image.open(image_path) as img:
        img_rgba = img.convert("RGBA")
        # Create a new file name with the .png extension
        new_file_name = os.path.splitext(image_path)[0] + ".png"
        # Save the image in PNG format
        img_rgba.save(new_file_name, "PNG")

# Example usage:
convert_to_png("your_file_here") # Converts user's image to PNG
