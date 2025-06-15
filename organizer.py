import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # Hide the Tkinter window
TARGET_FOLDER = Path(filedialog.askdirectory(title="Select folder to organize"))

if not TARGET_FOLDER:
    print("No folder selected. Exiting.")
    exit()