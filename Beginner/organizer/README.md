# Download Files Organizer Bot

## Overview
This project provides an automation script for organizing your cluttered `Downloads` folder. The script sorts files into categories such as Documents, Images, Music, Videos, Code, and more. It also supports subcategories based on common keywords (like Python, Java, AI/ML, Office, etc.), making it easy to keep your downloads tidy and accessible.

The project follows clean coding principles, ensuring reusable and maintainable code. This repository is an excellent reference for anyone learning or demonstrating file automation with Python.

---

## Features

- **Comprehensive File Organization:** Automatically sorts files by type and subcategory.
- **Duplicate Handling:** Prevents overwriting by renaming duplicate files.
- **Skip Already Organized Files:** Ignores files that are already sorted.
- **Customizable:** Easily edit file types and categories to fit your needs.
- **Optional GUI:** Includes a Tkinter-based folder picker for convenience.
- **Ready for Automation:** Can be scheduled via Task Scheduler (Windows) or Cron (Linux/macOS).

---

## Prerequisites

To get started with this project, ensure you have the following installed:

- Python 3.8 or higher
- (Optional) Tkinter for GUI folder selection

---

## Example Folder Structure

```
Downloads/
├── Documents/
│   ├── Java/
│   │   └── my_project.java
│   ├── Office/
│   │   └── notes.docx
│   └── resume.pdf
├── Images/
│   └── screenshot.png
├── Code/
│   ├── Python/
│   │   └── script.py
│   └── JavaScript/
│       └── app.js
├── Videos/
│   └── tutorial.mp4
```

---

## File Operations Covered

- **Move by Category:** Files are moved into folders like Documents, Images, Music, etc.
- **Subcategorization:** Documents and code files can be further sorted into subfolders such as "Python", "Java", "AI_ML", "Office", etc.
- **Duplicate Handling:** Files with the same name are renamed to avoid overwriting.
- **Already Sorted Detection:** Files already in a category folder are skipped.

---

## How to Run

### Default Usage (Organizes `~/Downloads`)

```sh
python organizer.py
```

### Automation (Optional)

**On Windows (via Task Scheduler):**
```sh
schtasks /Create /SC DAILY /TN "DownloadsOrganizer" /TR "python C:\path\to\organizer.py" /ST 18:00
```

**On Linux/macOS (via crontab):**
```sh
crontab -e
0 18 * * * /usr/bin/python3 /path/to/organizer.py
```

---

## Customization

You can edit the following in `organizer.py`:

- `FILE_TYPES` to support more or different file extensions.
- `DOCUMENT_SUBCATEGORIES` and `CODE_SUBCATEGORIES` to fit your personal or team naming conventions.

**Tip:** Use generic names like "Python", "Java", "AI_ML", "Office", "JavaScript", etc., for subfolders so the script is reusable for everyone.

---

## Contributing

We welcome contributions to this project! To get started:

1. **Fork the repository**  
   Create your own copy of the repository by clicking the "Fork" button at the top-right corner of this page.

2. **Create a feature branch**  
   Create a new branch for your feature or bugfix. For example:
   ```sh
   git checkout -b feature/your-feature-name
   ```

3. **Commit your changes**  
   Make your changes and commit them with a clear and descriptive message:
   ```sh
   git commit -m "Add description of your changes"
   ```

4. **Push to the branch**  
   Push your branch to your forked repository:
   ```sh
   git push origin feature/your-feature-name
   ```

---

## Notes

- Designed for personal use, but adaptable for wider deployment.
- Make sure to test on a backup directory before full use.
- Python must be installed and on PATH.

---

## License

MIT License. Free for personal and commercial use.

---

## Author

Maintained by the open source community.

---

## Inspired By

Trying to keep a messy Downloads folder clean — automatically!

