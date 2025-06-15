import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # Hide the Tkinter window
TARGET_FOLDER = Path(r"C:\Users\ccd\Downloads")  # <-- Set your folder path here

if not TARGET_FOLDER.exists():
    print("Target folder does not exist. Exiting.")
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
    "AI_ML": [
        "anaconda", "pytorch", "tensorflow", "scikit", "keras", "machine learning", "ai", "ml", "jupyter", "colab", "notebook", ".whl"
    ],
    "Python": [
        "python", "pycharm", ".py", ".ipynb", "pip", "virtualenv", "venv"
    ],
    "App_Development": [
        "android", "studio", "flutter", "react", "node", "npm", "gradle", "kotlin", "swift", "xcode", "appdev"
    ],
    "Java": [
        "java", "jdk", "jre", ".jar", "eclipse", "intellij"
    ],
    "Automation": [
        "selenium", "automation", "robot", "autohotkey", "macro", "scrapy", "beautifulsoup"
    ],
    "Office": [
        "word", "excel", "powerpoint", "office", ".docx", ".xlsx", ".pptx", ".ppt", ".xls"
    ],
}


def get_category(file_ext):
    for category, extensions in FILE_TYPES.items():
        if file_ext.lower() in extensions:
            return category
    return "Others"

def get_document_subcategory(filename, file_ext):
    lower_name = filename.lower()
    for subcat, keywords in DOCUMENT_SUBCATEGORIES.items():
        for keyword in keywords:
            if keyword.startswith("."):
                if file_ext.lower() == keyword:
                    return subcat
            elif keyword in lower_name:
                return subcat
    return None

def is_already_sorted(item_path, folder):
    rel = item_path.relative_to(folder)
    return len(rel.parts) > 1

def get_unique_dest(dest_path):
    if not dest_path.exists():
        return dest_path
    stem, suffix = dest_path.stem, dest_path.suffix
    parent = dest_path.parent
    i = 1
    while True:
        new_name = f"{stem} ({i}){suffix}"
        new_path = parent / new_name
        if not new_path.exists():
            return new_path
        i += 1
        
def organize_folder(folder):
    for item in os.listdir(folder):
        item_path = folder / item
        if item_path.is_file():
            if is_already_sorted(item_path, folder):
                continue

            ext = item_path.suffix
            category = get_category(ext)
            dest_path = folder / category

            if category in ["Documents", "Installers", "Code", "Archives", "Images"]:
                subcat = get_document_subcategory(item, ext)
                if subcat:
                    dest_path = dest_path / subcat

            dest_path.mkdir(parents=True, exist_ok=True)
            final_dest = get_unique_dest(dest_path / item_path.name)
            shutil.move(str(item_path), str(final_dest))
            print(f"Moved {item} → {final_dest.relative_to(folder)}")

if __name__ == "__main__":
    organize_folder(TARGET_FOLDER)
    print("✅ Done organizing!")