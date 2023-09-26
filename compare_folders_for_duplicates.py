import os
import tkinter as tk
from tkinter import filedialog
from collections import Counter

def browse_directory(label):
    directory_path = filedialog.askdirectory()
    label.config(text=directory_path)
    return directory_path

def find_duplicate_files(directory1, directory2):
    files1 = [f for f in os.listdir(directory1) if os.path.isfile(os.path.join(directory1, f))]
    files2 = [f for f in os.listdir(directory2) if os.path.isfile(os.path.join(directory2, f))]
    
    common_files = set(files1) & set(files2)
    return list(common_files)

def report_duplicates():
    dir1 = directory_label1.cget("text")
    dir2 = directory_label2.cget("text")
    
    if not dir1 or not dir2:
        result_label.config(text="Please select both directories.")
        return
    
    duplicates = find_duplicate_files(dir1, dir2)
    
    if not duplicates:
        result_label.config(text="No duplicate files found.")
    else:
        result_label.config(text=f"Duplicate files: {', '.join(duplicates)}")
        count = len(duplicates)
        count_label.config(text=f"Number of duplicates: {count}")

# Create the main GUI window
root = tk.Tk()
root.title("Duplicate File Finder")

# Create and configure labels for directory selection
directory_label1 = tk.Label(root, text="Select Directory 1:")
directory_label1.pack()

directory_label2 = tk.Label(root, text="Select Directory 2:")
directory_label2.pack()

# Create and configure buttons for directory selection
browse_button1 = tk.Button(root, text="Browse Directory 1", command=lambda: browse_directory(directory_label1))
browse_button1.pack()

browse_button2 = tk.Button(root, text="Browse Directory 2", command=lambda: browse_directory(directory_label2))
browse_button2.pack()

# Create and configure button to find duplicates
find_duplicates_button = tk.Button(root, text="Find Duplicates", command=report_duplicates)
find_duplicates_button.pack()

# Create and configure labels for displaying results
result_label = tk.Label(root, text="")
result_label.pack()

count_label = tk.Label(root, text="")
count_label.pack()

root.mainloop()
