import os
import datetime
import shutil

INPUT_FOLDER = "Input"
TARGET_VIDEO_FOLDER = "Videos"
TARGET_PHOTO_FOLDER = "Images"

VIDEO_FILE_TYPES = [".mp4", ".mov", ".mkv", ".avi", ".wmv", ".avchd", ".webm", ".flv"]

PHOTO_FILE_TYPES = [".jpg", ".jpeg", ".png",".gif", ".tiff", ".svg", ".ico", ".bmp", ".heic"]

def get_year(file):
    time_created_stamp = os.path.getctime(file.path)
    date_created_stamp = datetime.date.fromtimestamp(time_created_stamp).year
    return date_created_stamp

def move_file(target_path, date_created, file):
    new_folder_path = f"{target_path}/{date_created}"
    old_folder_path = file.path
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
    if not os.path.exists(f"{new_folder_path}/{file.name}"):
        shutil.move(old_folder_path, new_folder_path)


for file in os.scandir(INPUT_FOLDER):
    if file.is_file():
        file_ext = os.path.splitext(file.name)[1].lower()
        if file_ext in VIDEO_FILE_TYPES:
            date_created = get_year(file)
            move_file(TARGET_VIDEO_FOLDER, date_created, file)

        elif file_ext in PHOTO_FILE_TYPES:
            date_created = get_year(file)
            move_file(TARGET_PHOTO_FOLDER, date_created, file)
