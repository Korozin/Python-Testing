import os
import shutil
from termcolor import colored

# List of file types and their corresponding folders
file_types = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".bmp": "Images",
    ".svg": "Images",
    ".tiff": "Images",
    ".psd": "Images",
    ".ai": "Images",
    ".eps": "Images",
    ".indd": "Images",
    ".pdf": "Images",
    ".doc": "Documents",
    ".docx": "Documents",
    ".odt": "Documents",
    ".rtf": "Documents",
    ".tex": "Documents",
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".xlsm": "Spreadsheets",
    ".ods": "Spreadsheets",
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".pps": "Presentations",
    ".ppsx": "Presentations",
    ".key": "Presentations",
    ".mp3": "Music",
    ".wav": "Music",
    ".aac": "Music",
    ".flac": "Music",
    ".m4a": "Music",
    ".ogg": "Music",
    ".wma": "Music",
    ".avi": "Videos",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".wmv": "Videos",
    ".mov": "Videos",
    ".flv": "Videos",
    ".mpg": "Videos",
    ".mpeg": "Videos",
    ".webm": "Videos",
    ".srt": "Subtitles",
    ".zip": "Archives",
    ".rar": "Archives",
    ".tar.gz": "Archives",
    ".7z": "Archives",
    ".dmg": "Archives",
    ".iso": "Archives",
    ".apk": "Apps",
    ".exe": "Programs",
    ".msi": "Programs",
    ".deb": "Packages",
    ".rpm": "Packages",
    ".py": "Python",
    ".pyw": "Python",
    ".rb": "Ruby",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".cs": "C#",
    ".sh": "Shell",
    ".pl": "Perl",
    ".php": "PHP",
    ".go": "Go",
    ".cpp": "C++",
    ".c": "C",
    ".java": "Java",
    ".m": "Objective-C",
    ".swift": "Swift",
    ".vb": "Visual Basic",
    ".scala": "Scala",
    ".r": "R",
    ".lua": "Lua",
    ".mat": "MATLAB",
    ".ipynb": "Jupyter Notebook",
    ".scss": "Stylesheets",
    ".css": "Stylesheets",
    ".html": "Web",
    ".htm": "Web",
    ".xml": "Web",
    ".json": "Web",
    ".sql": "Databases",
    "": "Misc",
}

# Get the path of the current script
current_script_path = os.path.abspath(__file__)

# Organize files based on their file type
for filename in os.listdir():
    if os.path.isfile(filename):
        if os.path.abspath(filename) != current_script_path:  # Do not move the script
            file_ext = os.path.splitext(filename)[1]
            if file_ext in file_types:
                folder_name = file_types[file_ext]
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                src_path = os.path.abspath(filename)
                dst_path = os.path.abspath(os.path.join(folder_name, filename))
                shutil.move(filename, folder_name)
                print(colored(f"Moved file {filename} to directory {folder_name}", "green"))
                print(colored(f"Source path: {src_path}", "yellow"))
                print(colored(f"Destination path: {dst_path}", "yellow"))
            else:
                folder_name = file_types[""]
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                src_path = os.path.abspath(filename)
                dst_path = os.path.abspath(os.path.join(folder_name, filename))
                shutil.move(filename, folder_name)
                print(colored(f"Moved file {filename} to directory {folder_name}", "green"))
                print(colored(f"Source path: {src_path}", "yellow"))
                print(colored(f"Destination path: {dst_path}", "yellow"))

# Remove any empty folders
for folder_name in file_types.values():
    if os.path.exists(folder_name) and not os.listdir(folder_name):
        os.rmdir(folder_name)
