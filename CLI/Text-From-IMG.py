import pytesseract
from PIL import Image

''' Using a library for this feels like cheating TwT '''

# Path of the image file to be processed
image_path = 'file.png'

# Open the image file using PIL's Image module
with Image.open(image_path) as img:
    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(img)

# Print the extracted text to the console
print(text, end='')
