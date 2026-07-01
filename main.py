# File Organizer:
# "A script that scans a target folder and moves each file
# into a subfolder based on its extension."
import os
import shutil

EXTENSION_MAP = {
    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".svg": "Images",
    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    # Video
    ".mp4": "Video",
    ".mkv": "Video",
    ".avi": "Video",
    ".mov": "Video",
    # Code
    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
    ".java": "Code",
    # Archives
    ".zip": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".rar": "Archives",
}


def categorize_file(filename):
    ext = os.path.splitext(filename)[1]
    category = EXTENSION_MAP.get(ext, "Other")
    return category


# os.listdir() returns only filenames, not full paths.
# We need os.path.join(folder_path, file) to build the full path,
# so os.path.isfile() knows where to look.
def scan_folder(folder_path):
    file_list = []
    folder_list = os.listdir(folder_path)
    for file in folder_list:
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):
            file_list.append(full_path)
    return file_list


def get_folder_path():
    while True:
        folder_path = input("Give a folder path to organize: ")
        if os.path.isdir(folder_path):
            break
        else:
            print("Path isnt valid")
    return folder_path
    

def move_file(file, category, folder_path):
    destination_folder = os.path.join(folder_path, category)#the Complete path of subfolder
    os.makedirs(destination_folder, exist_ok=True)#create the subfolder but no dublicates

    filename = os.path.basename(file)
    destination_path = os.path.join(destination_folder, filename)#the Complete path of the file

    base, ext = os.path.splitext(filename) # tuple unpacking 
    counter = 1
    while os.path.exists(destination_path): # if there is dublicate in the same path
        dublicate_filename = f"{base}_{counter}{ext}" 
        destination_path = os.path.join(destination_folder, dublicate_filename) # the path with the new updated name
        counter += 1

    shutil.move(file, destination_path)

    
if __name__ == "__main__":

    while True:
       folder_path = get_folder_path()
       files = scan_folder(folder_path)
    # if not files:
    #     print("Folder is empty, try another.")
    #  else:
    #      break

    # for every file in files
    #   category = categorize_file(file)
    #   move_file(file, category, folder_path)

