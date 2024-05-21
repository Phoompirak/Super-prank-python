import os
import time

dist_folder = os.getcwd() + '\dist'  # Change the path if needed

print(dist_folder)
for filename in os.listdir(dist_folder):
    if filename.endswith(".exe"):
        print(f"Running file: {filename}")
        os.startfile(os.path.join(dist_folder, filename))  # Run the .exe file
