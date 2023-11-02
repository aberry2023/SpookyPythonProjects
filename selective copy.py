import os
import shutil

def get_files_recursively(start_directory, filter_extension=None):
    for root, _, files in os.walk(start_directory):
        for file in files:
            if filter_extension is None or file.lower().endswith(filter_extension):
                yield os.path.join(root, file)

def selective_copy(source, target, file_extension=None):
    for file in get_files_recursively(source, file_extension):
        print(file)
        shutil.copy(file, target)
        print("The following file has been copied", file)

if __name__ == "__main__":
    selective_copy("/Users/my_user_name/Desktop/newPDFs",
                   "/Users/my_user_name/Desktop/oldPDFs",
                   ".pdf")