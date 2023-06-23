import os
import shutil

parent_folder = "/Users/kirstengrond/Desktop/sequences/"

# Create a set to store the unique folder names
folder_names = set()

for filename in os.listdir(parent_folder):
    if os.path.isfile(os.path.join(parent_folder, filename)):
        folder_name = filename.split('_')[0]
        # Add the folder name to the set
        folder_names.add(folder_name)

# Create a folder for each unique folder name and move the files into the corresponding folders
for folder_name in folder_names:
    folder_path = os.path.join(parent_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    for filename in os.listdir(parent_folder):
        if os.path.isfile(os.path.join(parent_folder, filename)):
            if filename.startswith(folder_name):
                file_path = os.path.join(parent_folder, filename)
                dest_path = os.path.join(folder_path, filename)
                if os.path.exists(dest_path):
                    os.remove(dest_path)  # Delete the existing file
                shutil.move(file_path, folder_path)

print("Folders and files moved successfully.")
