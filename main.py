import os
import shutil
import datetime
from classes import *

# Source and destination directories
source_dir = r"\\Dfs01.pbmc.org\dfs\DATA\ADMITREG\VPS_Reports"
dest_dir = r"C:\Users\mdorio\Library\Northwell Health\CBO DPU Leadership - Dashboard Files\Dashboard Files\Master Data Directory\Peconic"

# File prefixes to check for (contains)
file_prefixes = ["A2OUT2", "A2PAMB", "A2OSUR", "A2PINP"]

def copy_files(source, destination, prefixes):
    """Copies files containing specified prefixes from source to destination, creating subfolders and appending today's date."""
    print("Starting the file copying process...")
    today = datetime.datetime.now().date()  # Get today's date
    files_copied = 0  # Counter for copied files
    for filename in os.listdir(source):
        for prefix in prefixes:  # Iterate through prefixes for each file
            if prefix in filename:  # Check if the prefix is contained in the filename
                source_path = os.path.join(source, filename)
                # Check if the modification date of the file is today
                modification_time = os.path.getmtime(source_path)
                modification_date = datetime.datetime.fromtimestamp(modification_time).date()
                if modification_date == today:  # Only proceed if the file was modified today
                    # Get today's date and format it as mmddyyyy
                    today_date = today.strftime("%m%d%Y")
                    # Create the new filename with today's date prepended
                    new_filename = f"{today_date}_{filename}"
                    # Create the subfolder in the destination directory if it doesn't exist
                    subfolder_name = prefix  # Use the prefix as the subfolder name
                    subfolder_path = os.path.join(destination, subfolder_name)
                    os.makedirs(subfolder_path, exist_ok=True)
                    # Copy the file to the subfolder with the new name
                    destination_path = os.path.join(subfolder_path, new_filename)
                    try:
                        shutil.copy2(source_path, destination_path)
                        print(f"Copied '{filename}' to '{destination_path}'")
                        files_copied += 1  # Increment the counter for copied files
                    except Exception as e:
                        print(f"Error copying '{filename}': {e}")
                break  # Exit the inner loop after finding a matching prefix
    print(f"File copying process completed. Total files copied: {files_copied}")

def process_files(directory):
    """Process each file in the specified directory based on the contained string."""
    print("Starting the file processing...")
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} not found")
    files_to_process = os.listdir(directory)
    for file in files_to_process:
        file_name = file
        file_path = os.path.join(directory, file)
        try:
            if '$$A2AINP' in file_name:
                df = A2AINP(file_path).convert_to_dataframe()
            if '$$A2AOUT2' in file_name:
                df = A2AOUT2(file_path).convert_to_dataframe()
            if '$$A2PAMB' in file_name:
                df = A2PAMB(file_path).convert_to_dataframe()
            if '$$A2OSUR' in file_name:
                df = A2OSUR(file_path).convert_to_dataframe()
        except Exception as e:
            print(f"Error processing file: {file_name} with error: {e}")

if __name__ == '__main__':
    # First, copy required files to the destination directory
    copy_files(source_dir, dest_dir, file_prefixes)

    # Then, process each prefix directory independently
    for prefix in file_prefixes:
        process_files(os.path.join(dest_dir, prefix))
