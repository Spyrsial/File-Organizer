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
    pass


if __name__ == "__main__":
    # folder_path = get_folder_path()
    # is_empty = check_folder(folder_path)

    # if is_empty = False
    # files = scan_folder(folder_path)

    # for every file in files
    #   category = categorize_file(file)
    #   move_file(file, category)
    pass
