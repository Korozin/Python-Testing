import sys
from PIL import Image

## Set up graceful script exiting ##
def exit_gracefully(signum=None, frame=None):
    print("\n\nExited")
    sys.exit(0)


try:
    # Try to use signal.SIGINT on Unix-based systems
    import signal

    signal.signal(signal.SIGINT, exit_gracefully)
except (ImportError, AttributeError):
    try:
        # Try to use ctypes.windll.kernel32 on Windows
        import ctypes

        kernel32 = ctypes.windll.kernel32

        # Enable Ctrl+C handling
        kernel32.SetConsoleCtrlHandler(exit_gracefully, 1)
    except:
        print("Failed to set up signal handling. Graceful exit upon CTRL+C not supported")
## Set up graceful script exiting ##


def conv_2_grayscale(image_path):
    """
    Open the image and convert it to grayscale
    """
    img = Image.open(image_path).convert('L')
    return img


def validate_hex_code(hex_code):
    """
    Validate hex code and format it
    """
    if "#" in hex_code:
        print(f"\n{hex_code} cannot contain '#', removing it.")
        hex_code = hex_code.replace("#", "")
        print(f"datatype updated to: {hex_code}")

    if len(hex_code) < 6:
        print(f"\n{hex_code} is not required length of: 6. Padding with zero(s).")
        hex_code += "0" * (6 - len(hex_code))
        print(f"datatype updated to: {hex_code}")
    elif len(hex_code) > 6:
        print(f"\n{hex_code} exceeds required length of: 6. Formatting data.")
        hex_code = hex_code[:6]
        print(f"datatype updated to: {hex_code}")
    
    return hex_code


def hex_to_rgb(hex_code):
    """
    Convert the hex code to RGB values
    """
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))


def get_hex_code():
    """
    Get and validate the user's chosen hex code
    """
    hex_code = input("Hex code for recoloring: ")
    hex_code = validate_hex_code(hex_code)
    rgb_code = hex_to_rgb(hex_code)
    return rgb_code


def recolor_pixels(img, rgb_code):
    """
    Recolor each pixel of the image based on the grayscale value and the user's chosen color
    """
    # Create a new image with the same size and mode as the original
    new_img = Image.new('RGB', img.size)

    # Loop through each pixel of the image and recolor it
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            # Get the grayscale value of the pixel
            gray_value = img.getpixel((x, y))

            # Calculate the new color value based on the grayscale value and the user's chosen color
            new_color = tuple(int((gray_value / 255) * value) for value in rgb_code)

            # Set the new color value for the pixel in the new image
            new_img.putpixel((x, y), new_color)

    return new_img


def save_image(image, image_name):
    """
    Save the new image
    """
    image.save(image_name)
    print(f"\nSaved image to: {image_name}")


# Use the functions to run the program
def main():
    while True:
        try:
            image_path = input("File path to your image: ")
            img = conv_2_grayscale(image_path)
            rgb_code = get_hex_code()
            new_img = recolor_pixels(img, rgb_code)
            save_image(new_img, f"recolor-{image_path}")
            break
        except Exception as e:
            print(f"\nError: {e}\n")
    

if __name__ == "__main__":
    main()
