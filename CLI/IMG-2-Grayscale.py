from PIL import Image

def conv_grayscale(file_name):
    original_image = Image.open(file_name)
    grayscale_image = original_image.convert('L')

    grayscale_image.save(f"grayscale-{file_name}")

conv_grayscale("your_image")
