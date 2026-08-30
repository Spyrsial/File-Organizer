# File Organizer
# Scans a folder and organizes files into category subfolders
# based on their file extensions.
import os
import shutil
import sys

# keys must be lowercase
EXTENSION_MAP: dict[str, str]= {
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


def categorize_file(filename: str) -> str:
    """Return the category associated with a file's extension."""
    ext = os.path.splitext(filename)[1].lower()
    return EXTENSION_MAP.get(ext, "Other")


def scan_folder(folder_path: str) -> list[str]:
    """Return the full paths of all files directly inside a folder."""
    file_list = []

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        # Ignore subdirectories, only organize files in the target folder.
        if os.path.isfile(full_path):
            file_list.append(full_path)

    return file_list 


def get_folder_path() -> str:
    """Prompt the user until a valid directory path is provided."""
    while True:
        folder_path = input("Give a folder path to organize: ")

        if os.path.isdir(folder_path):
            return folder_path

        print("Path isn't valid.", file=sys.stderr)


def move_file(file_path: str, category: str, folder_path: str) -> None:
    """Move a file into its category folder without overwriting existing files."""
    destination_folder = os.path.join(folder_path, category)
    os.makedirs(destination_folder, exist_ok=True)

    filename = os.path.basename(file_path)
    destination_path = os.path.join(destination_folder, filename)

    base, ext = os.path.splitext(filename)
    counter = 1

    #Preserve existing files by generating names such as file_1.pdf, file_2.pdf,etc.
    while os.path.exists(destination_path):
        duplicate_filename = f"{base}_{counter}{ext}"
        destination_path = os.path.join(
            destination_folder,
            duplicate_filename
        )
        counter += 1

    shutil.move(file_path, destination_path)


def main() -> None:
    while True:
        folder_path = get_folder_path()
        files = scan_folder(folder_path)

        if not files:
            print("Folder is empty, try another.", file=sys.stderr)
        else:
            break

    for file_path in files:
        category = categorize_file(file_path)
        try:
            move_file(file_path, category, folder_path)
        except OSError as e:
            print(f"Failed to move {file_path}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()