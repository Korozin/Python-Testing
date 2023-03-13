from PIL import Image, ImageSequence
import os

def gif_to_png(gif_path, png_folder):
    with Image.open(gif_path) as im:
        # Iterate over each frame in the GIF file
        for i, frame in enumerate(ImageSequence.Iterator(im)):
            # Save each frame as a PNG file with a zero-padded index
            png_path = f"{png_folder}/frame_{i:04d}.png"
            print(f"\033[95m[GIF Splitter]: \033[0mSaved frame: \033[93mframe_{i:04d}.png\033[0m")
            frame.save(png_path)

# Example usage
gif_path = "example.gif"
png_folder = "./frames/"

if not os.path.exists(png_folder):
    os.makedirs(png_folder, exist_ok=True)

gif_to_png(gif_path, png_folder)
print("\033[1m\033[92mProcess Completed\033[0m")
