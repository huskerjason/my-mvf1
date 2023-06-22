import os

directory = r'C:/Users/Jason/Desktop/python/MultiViewer_Formula_1/'  # Replace with the path to your directory

for filename in os.listdir(directory):
    if ' ' in filename:
        print(filename)
        new_filename = filename.replace(' ', '_').lower()
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)
