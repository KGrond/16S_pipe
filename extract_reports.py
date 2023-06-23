import os
import shutil

parent_folder = "/Users/kirstengrond/Desktop/sequences"
new_folder = "/Users/kirstengrond/Desktop/reports"

# Create the new folder if it doesn't exist
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for dirpath, dirnames, filenames in os.walk(parent_folder):
    for filename in filenames:
        if filename == "report.json":
            file_path = os.path.join(dirpath, filename)
            folder_names = os.path.normpath(dirpath).split(os.path.sep)[-2:]
            new_name = "_".join(folder_names) + "_" + filename
            new_path = os.path.join(new_folder, new_name)
            shutil.copy(file_path, new_path)
            print(f"Copied {file_path} to {new_path}")
