import os
import shutil

current_folder = os.getcwd()
print(f"Scanning folder: {current_folder}")

target_folder = os.path.join(current_folder, "TextFiles")

if not os.path.exists(target_folder):
    os.makedirs(target_folder)
    print("Created 'TextFiles' directory.")

for filename in os.listdir(current_folder):
    if filename.endswith(".txt"):
        source_path = os.path.join(current_folder, filename)
        destination_path = os.path.join(target_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename} -> TextFiles/")

print("Folder organization complete!")