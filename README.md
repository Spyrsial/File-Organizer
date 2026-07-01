# File Organizer

A Python CLI tool that automatically organizes files in a folder into subfolders based on their extension. Point it at a messy directory — like your Downloads folder — and it sorts every file into a clean category folder (`Documents/`, `Images/`, `Audio/`, and so on).

## Features

- Sorts files into category folders based on their extension
- Handles unknown or missing extensions by routing them to an `Other/` folder
- Handles duplicate filenames without overwriting: a second `report.pdf` becomes `report_1.pdf`, a third becomes `report_2.pdf`, and so on
- Leaves existing subfolders untouched — only loose files are organized
- Validates the target path and re-prompts if the folder doesn't exist or is empty
- Fully covered by unit tests

## Supported Categories

| Category    | Extensions                                   |
| ----------- | -------------------------------------------- |
| Documents   | `.pdf` `.doc` `.docx` `.txt` `.xlsx` `.pptx` |
| Images      | `.jpg` `.jpeg` `.png` `.gif` `.svg`          |
| Audio       | `.mp3` `.wav` `.flac`                        |
| Video       | `.mp4` `.mkv` `.avi` `.mov`                  |
| Code        | `.py` `.js` `.html` `.css` `.java`           |
| Archives    | `.zip` `.tar` `.gz` `.rar`                   |
| Other       | Anything not listed above, or files with no extension |

## Requirements

- Python 3.x

No external dependencies — the script uses only the Python standard library (`os`, `shutil`).

## Usage

```bash
python3 main.py
```

You'll be prompted to enter the path of the folder you want to organize:

```
Give a folder path to organize: /home/user/Downloads
```

The script then sorts every file in that folder into its category subfolder.

> **Warning:** This tool moves files. Always test it on a throwaway folder before running it on a directory you care about.

## Example

**Before:**

```
Downloads/
├── report.pdf
├── photo.jpg
├── song.mp3
└── notes.txt
```

**After:**

```
Downloads/
├── Documents/
│   ├── report.pdf
│   └── notes.txt
├── Images/
│   └── photo.jpg
└── Audio/
    └── song.mp3
```

## How It Works

The script is broken into small, single-responsibility functions:

- **`get_folder_path()`** — prompts the user for a folder path and re-asks until a valid directory is given.
- **`scan_folder(folder_path)`** — returns a list of the full paths of files in the folder, ignoring any subfolders.
- **`categorize_file(filename)`** — looks up a file's extension in `EXTENSION_MAP` and returns its category (or `"Other"` if unknown).
- **`move_file(file, category, folder_path)`** — creates the category subfolder if needed, resolves any filename collision by appending a counter, and moves the file.

The `main()` block ties these together: it keeps asking for a folder until a non-empty one is provided, then categorizes and moves each file.

## Testing

The project is covered by unit tests written with Python's built-in `unittest` framework. The tests use temporary directories (`tempfile`) so they never touch real files on your system.

Run the tests with:

```bash
python3 tests.py
```

## Possible Future Improvements

- Accept the folder path as a command-line argument instead of an interactive prompt
- Add a `--dry-run` mode that previews changes without moving anything
- Make extension matching case-insensitive (`.JPG` treated the same as `.jpg`)
- Let users customize categories via a config file
