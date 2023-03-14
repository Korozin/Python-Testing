import base64
import os

# List of filenames to scan for Base64 data
file_names = ['file_name_here.png'] # You can add to the list if you want to convert multiple files

# Path to the directory containing the image files
assets_path = './assets'
output_path = './output'

# Loop through the filenames and get the Base64 data for each file
for filename in file_names:
    file_path = os.path.join(assets_path, filename)
    with open(file_path, 'rb') as f:
        base64_data = base64.b64encode(f.read())

    # Write the Base64 data to a new file
    output_path = os.path.join(output_path, filename.replace('.png', '.b64'))
    with open(output_path, 'wb') as f:
        f.write(base64_data)
