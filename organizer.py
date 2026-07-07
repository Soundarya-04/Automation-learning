import os
import shutil

current_folder = os.getcwd()
print(f"Scanning folder: {current_folder}")

# A dictionary mapping file extensions to their target folders
FILE_TYPES = {
    '.txt': 'TextFiles',
    '.pdf': 'Documents',
    '.jpg': 'Images',
    '.png': 'Images',
    '.xlsx': 'Spreadsheets'
}

for filename in os.listdir(current_folder):
    # Separate the filename from its extension (e.g., 'test' and '.pdf')
    name, extension = os.path.splitext(filename)
    
    # Check if the extension is one of the types we want to organize
    if extension in FILE_TYPES:
        folder_name = FILE_TYPES[extension]
        target_folder = os.path.join(current_folder, folder_name)
        
        # Create the specific folder if it doesn't exist yet
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            print(f"Created folder: {folder_name}")
            
        source_path = os.path.join(current_folder, filename)
        destination_path = os.path.join(target_folder, filename)
        
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename} -> {folder_name}/")

print("Advanced folder organization complete!")