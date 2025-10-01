# Basic Keylogger Program

This program captures keystrokes and saves them to a log file.

## Files

- `keylogger.py` - Main keylogger class implementation
- `run_keylogger.py` - Simple runner script
- `requirements.txt` - Required dependencies
- `keylog.txt` - Output log file (created when program runs)

## Installation

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the keylogger:
```
python run_keylogger.py
```

The program will:
- Start capturing keystrokes immediately
- Save all keys to `keylog.txt` with timestamps
- Display pressed keys in the console
- Stop when ESC key is pressed

## Features

- Captures all keyboard input including special keys
- Timestamps each keystroke
- Saves logs to file automatically
- Clean exit with ESC key
- Error handling for graceful shutdown

## Security Note

This program is for educational purposes. Ensure you have proper authorization before monitoring keystrokes on any system.