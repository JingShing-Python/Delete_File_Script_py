import os

def delete_files_and_folders(root_folder, max_file_size, delete_empty_folders=True, ignored_file_types=None):
    ignored_file_types = ignored_file_types or []  # Set ignored_file_types to an empty list if not provided
    for root, dirs, files in os.walk(root_folder, topdown=False):
        # Delete files that are smaller than the specified size or have an extension in the ignored list
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_extension = os.path.splitext(file)[1].lower()  # Get the file extension and convert it to lowercase
            if file_size < max_file_size or file_extension in ignored_file_types:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")

        # Delete empty folders
        if delete_empty_folders:
            for folder in dirs:
                folder_path = os.path.join(root, folder)
                if not os.listdir(folder_path):  # Check if the folder is empty
                    os.rmdir(folder_path)
                    print(f"Deleted folder: {folder_path}")

root_folder = "file_path"
max_file_size = 1024 * 1024  # Specified file size in bytes (1MB)
delete_empty_folders = True  # Whether to delete empty folders
ignored_file_types = [".psd", ".zip", ".rar"]  # List of file types to be ignored

delete_files_and_folders(root_folder, max_file_size, delete_empty_folders, ignored_file_types)
