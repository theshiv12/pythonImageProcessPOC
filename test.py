import os
import shutil
import time

def copy_next_file():
    dest_path = '/Users/admin/Desktop/imagePythonPOC/image_folder'
    source_path = '/Users/admin/Desktop/imagePythonPOC/imgs'
    index_file = '/Users/admin/Desktop/imagePythonPOC/copied_files.txt'

    if not os.path.exists(index_file):
        with open(index_file, 'w') as file:
            file.write('0')

    # Check if the index file is empty
    if os.path.getsize(index_file) == 0:
        last_copied_index = 0
    else:
        with open(index_file, 'r') as file:
            last_copied_index = int(file.read().strip())

    source_files = sorted(os.listdir(source_path))
    dest_files = sorted(os.listdir(dest_path))

    if last_copied_index < len(source_files):
        file_to_copy = source_files[last_copied_index]
        print("Copying file:", file_to_copy)
        shutil.copy(os.path.join(source_path, file_to_copy), os.path.join(dest_path, dest_files[0]))

        with open(index_file, 'w') as file:
            file.write(str(last_copied_index + 1))
    else:
        # Reset the index back to zero when all files are copied
        with open(index_file, 'w') as file:
            file.write('0')
        print("All files have been copied. Resetting the index to start again.")

if __name__ == "__main__":
    while True:
        copy_next_file()
        time.sleep(2)  