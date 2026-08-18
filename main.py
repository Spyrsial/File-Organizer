# File Organizer
# Scans a folder and organizes files into category subfolders
# based on their file extensions.
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
    """Return the category associated with a file's extension."""
    ext = os.path.splitext(filename)[1]
    return EXTENSION_MAP.get(ext, "Other")


def scan_folder(folder_path):
    """Return the full paths of all files directly inside a folder."""
    file_list = []

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        # Ignore subdirectories; only organize files in the target folder.
        if os.path.isfile(full_path):
            file_list.append(full_path)

    return file_list


def get_folder_path():
    """Prompt the user until a valid directory path is provided."""
    while True:
        folder_path = input("Give a folder path to organize: ")

        if os.path.isdir(folder_path):
            return folder_path

        print("Path isn't valid.")


def move_file(file_path, category, folder_path):
    """Move a file into its category folder without overwriting existing files."""
    destination_folder = os.path.join(folder_path, category)
    os.makedirs(destination_folder, exist_ok=True)

    filename = os.path.basename(file_path)
    destination_path = os.path.join(destination_folder, filename)

    base, ext = os.path.splitext(filename)
    counter = 1

    # Preserve existing files by generating names such as file_1.pdf,
    # file_2.pdf, etc.
    while os.path.exists(destination_path):
        duplicate_filename = f"{base}_{counter}{ext}"
        destination_path = os.path.join(
            destination_folder,
            duplicate_filename
        )
        counter += 1

    shutil.move(file_path, destination_path)


if __name__ == "__main__":

    # Keep asking until the user selects a folder containing at least one file.
    while True:
        folder_path = get_folder_path()
        files = scan_folder(folder_path)

        if not files:
            print("Folder is empty, try another.")
        else:
            break

    for file_path in files:
        category = categorize_file(file_path)
        move_file(file_path, category, folder_path)