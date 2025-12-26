# How to Convert Python Tkinter App to Windows Executable / تبدیل برنامه پایتون Tkinter به فایل اجرایی ویندوز

## English
This document explains how the GPA Calculator Python application was converted into a Windows executable (.exe) using PyInstaller.

### Requirements
- Python installed on your system
- PyInstaller (can be installed via pip)

### Steps
1. Open your command prompt or PowerShell.
2. Navigate to the folder containing your Python file:
   ```powershell
   cd path\to\your\program
Install PyInstaller if not already installed:

powershell
Copy code
pip install pyinstaller
Run PyInstaller to create an executable:

powershell
Copy code
python -m PyInstaller --onefile --windowed --name "GPA_Calculator" Gpa_calculator.py
--onefile → Combines everything into a single .exe file

--windowed → Hides the console window (for GUI apps)

--name → Sets the name of the final executable

After the process completes, the .exe file will be located in the dist folder inside your project directory.

You can now run GPA_Calculator.exe on any Windows system without Python installed.

