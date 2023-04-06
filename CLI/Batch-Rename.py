import os
import hashlib

def get_script_hash():
    # Get the hash value of the script file
    with open(__file__, 'rb') as f:
        file_contents = f.read()
        file_hash = hashlib.sha256(file_contents).hexdigest()
        
    # Exclude the script file name and path from the hash calculation
    script_name = os.path.basename(__file__)
    file_hash = hashlib.sha256(file_hash.encode('utf-8') + script_name.encode('utf-8') + file_contents).hexdigest()

    return file_hash

def rename_files():
    # Get the hash value of the script file
    original_hash = get_script_hash()

    # get the directory path and user input for renaming
    directory = input("Enter the directory path where your files are located: ")
    rename_type = input("Enter the renaming type - prefix, suffix, or replace: ")
    if rename_type == "prefix" or rename_type == "suffix":
        rename_text = input("Enter the text to add as " + rename_type + ": ")
    elif rename_type == "replace":
        replace_text = input("Enter the text to replace: ")
        new_text = input("Enter the new text to replace with: ")

    # iterate over the files in the directory and rename them
    for filename in os.listdir(directory):
        # check if the file is the script file being run
        if filename == os.path.basename(__file__):
            continue

        # create the new filename based on the user's input
        if rename_type == "prefix":
            new_filename = rename_text + filename
        elif rename_type == "suffix":
            file_parts = os.path.splitext(filename)
            new_filename = file_parts[0] + rename_text + file_parts[1]
        elif rename_type == "replace":
            new_filename = filename.replace(replace_text, new_text)

        # rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

    # check the hash value of the script file again
    new_hash = get_script_hash()
    if new_hash != original_hash:
        print("Error: the script has been modified. Exiting.")
        return

    print("Files renamed successfully")

if __name__ == '__main__':
    rename_files()
