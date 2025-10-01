#!/usr/bin/env python3

from keylogger import Keylogger

def main():
    print("Basic Keylogger Program")
    print("======================")
    print()
    print("This program will capture all keystrokes and save them to keylog.txt")
    print("Press ESC to stop the keylogger")
    print()
    
    keylogger = Keylogger("keylog.txt")
    keylogger.start_logging()

if __name__ == "__main__":
    main()