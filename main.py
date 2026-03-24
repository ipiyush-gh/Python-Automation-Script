import os
import shutil
from datetime import datetime

# File type categories
file_types = {
    'Images': ['.jpg', '.png', '.jpeg', '.webp'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Compressed': ['.zip', '.rar'],
    'Programs': ['.exe']
}

# Log function
def log_action(message):
    with open("log.txt", "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

# Organize files
def organize_folder(path):
    try:
        for file in os.listdir(path):
            file_path = os.path.join(path, file)

            if os.path.isfile(file_path):
                _, ext = os.path.splitext(file)
                moved = False

                for folder, extensions in file_types.items():
                    if ext.lower() in extensions:
                        dest_folder = os.path.join(path, folder)

                        if not os.path.exists(dest_folder):
                            os.makedirs(dest_folder)

                        shutil.move(file_path, os.path.join(dest_folder, file))
                        log_action(f"Moved {file} to {folder}")
                        moved = True
                        break

                if not moved:
                    log_action(f"Skipped {file} (unsupported type)")

        print("✅ Files organized successfully!")

    except Exception as e:
        print("❌ Error:", e)
        log_action(f"Error: {e}")

# User input
folder_path = input("Enter folder path: ")
organize_folder(folder_path)