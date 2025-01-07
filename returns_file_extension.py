import os

def find_files_with_extension(directory, extension):
    matching_files = []
    try:
        for entry in os.listdir(directory):
            full_path = os.path.join(directory, entry)
            if os.path.isdir(full_path):
                matching_files.extend(find_files_with_extension(full_path, extension))
            elif entry.endswith(extension):
                matching_files.append(full_path)
    except PermissionError:
        pass  # Skip directories we don't have permission to access
    return matching_files

def main():
    directory = input("Enter the directory path: ")
    extension = input("Enter the file extension (e.g., .txt, .py): ")
    
    matching_files = find_files_with_extension(directory, extension)
    if matching_files:
        print(f"Files with extension '{extension}':")
        for file in matching_files:
            print(file)
    else:
        print(f"No files with extension '{extension}' found in the directory '{directory}'.")

if __name__ == "__main__":
    main()
