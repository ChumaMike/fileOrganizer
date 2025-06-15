# 🗃️ Download Files Organizer Bot

An automation script that organizes your cluttered `Downloads` folder by automatically sorting files into categories (like Documents, Images, Music, Videos, Code, and more), and even subcategories based on keywords (like Python, Java, AIML, etc.).

---

## 📦 Features

✅ Automatically sorts files by type  
✅ Recognizes and moves files into subfolders like "Chuma Java", "AIML", "Chuma App Dev"  
✅ Prevents overwriting by renaming duplicate files  
✅ Skips files already organized  
✅ Easily customizable file types and categories  
✅ Optional GUI folder picker (Tkinter enabled)  
✅ Ready for automation via Task Scheduler or Cron

---

## 🔧 Technologies Used

- Python 3.8+
- `os`, `shutil`, `pathlib` for file operations
- `tkinter` (optional) for folder selection UI

---

## 🖼️ Example Folder Structure After Running

Downloads/
├── Documents/
│ ├── Chuma Java/
│ │ └── my_project.java
│ ├── Office/
│ │ └── notes.docx
│ └── resume.pdf
├── Images/
│ └── screenshot.png
├── Code/
│ └── test_script.py
├── Videos/
│ └── tutorial.mp4


---

## 🚀 How to Use

### Default (Organizes `~/Downloads`)
python organizer.py

## 🔁 Automation (Optional)
On Windows (via Task Scheduler):
schtasks /Create /SC DAILY /TN "DownloadsOrganizer" /TR "python C:\path\to\organizer.py" /ST 18:00

On Linux/macOS (via crontab):
crontab -e
0 18 * * * /usr/bin/python3 /path/to/organizer.py

## 🧠 Customization

You can edit:

  FILE_TYPES to support more or different file extensions
  DOCUMENT_SUBCATEGORIES to fit your personal naming conventions

## 📌 Notes

Designed for personal use, but adaptable for wider deployment

Make sure to test on a backup directory before full use

Python must be installed and on PATH

## 📄 License
MIT License. Free for personal and commercial use.

## 👤 Author
Chuma (Mike Meyiswa)
Student & Software Enthusiast
🇿🇦 South Africa

## 💡 Inspired By
Trying to keep a messy Downloads folder clean — automatically!

