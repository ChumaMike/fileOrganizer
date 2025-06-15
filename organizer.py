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
    
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xls", ".xlsx", ".pptx", ".ppt", ".odt", ".rtf", ".csv", ".md"],
    "Installers": [".exe", ".msi", ".whl"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".ipynb", ".json", ".xml", ".sh", ".bat"],
    "Others": []
}

DOCUMENT_SUBCATEGORIES = {
    "AIML": [
        "anaconda", "pytorch", "tensorflow", "scikit", "keras", "machine learning", "ai", "ml", "jupyter", "colab", "notebook", ".whl"
    ],
    "Chuma PY": [
        "python", "pycharm", ".py", ".ipynb", "pip", "virtualenv", "venv"
    ],
    "Chuma App Dev": [
        "android", "studio", "flutter", "react", "node", "npm", "gradle", "kotlin", "swift", "xcode", "appdev"
    ],
    "Chuma Java": [
        "java", "jdk", "jre", ".jar", "eclipse", "intellij"
    ],
    "Automation": [
        "selenium", "automation", "robot", "autohotkey", "macro", "scrapy", "beautifulsoup"
    ],
    "Office": [
        "word", "excel", "powerpoint", "office", ".docx", ".xlsx", ".pptx", ".ppt", ".xls"
    ],
}