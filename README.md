# Python Keylogger – Keystroke Monitoring Tool

**SkillCraft Cybersecurity Internship – Task 4**  
**Author:** CHERUPALLI MANI KARTHIK  
**Domain:** CYBERSECURITY AND BLOCKCHAIN

## ⚠️ Ethical Disclaimer

**IMPORTANT: This tool is for educational purposes only.**

- Use this keylogger **ONLY** on systems you own or have explicit written permission to monitor
- Unauthorized keylogging is **illegal** and unethical
- This project is intended to demonstrate cybersecurity concepts for learning purposes
- The author is not responsible for any misuse of this tool

## 📝 Description

This is a basic keylogger program written in Python that records and logs keystrokes. The program captures keyboard input and saves it to a log file with timestamps. It demonstrates fundamental concepts in cybersecurity and system monitoring.

### Features

- Real-time keystroke capture
- Logs all key presses with timestamps
- Handles both regular characters and special keys (Shift, Ctrl, Alt, etc.)
- Clean exit with ESC key
- Timestamped log entries for analysis
- Simple and easy-to-understand code

## 🛠️ Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Setup

1. Clone this repository:
```bash
git clone https://github.com/dino50687/SCT_CS_4-KeyLogger.git
cd SCT_CS_4-KeyLogger
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the keylogger:
```bash
python keylogger.py
```

or

```bash
python3 keylogger.py
```

### How It Works

1. The program starts and displays a warning message
2. Keystrokes are logged to `keylog.txt` in the same directory
3. Each keystroke is saved with a timestamp
4. Press **ESC** to stop the keylogger
5. Check `keylog.txt` for the logged keystrokes

### Example Output

The log file (`keylog.txt`) will contain entries like:
```
2024-01-01 12:00:00 - Keylogger started
2024-01-01 12:00:01 - Key pressed: h
2024-01-01 12:00:02 - Key pressed: e
2024-01-01 12:00:03 - Key pressed: l
2024-01-01 12:00:04 - Key pressed: l
2024-01-01 12:00:05 - Key pressed: o
2024-01-01 12:00:06 - Special key pressed: Key.space
2024-01-01 12:00:07 - Special key pressed: Key.esc
2024-01-01 12:00:07 - ESC pressed - Stopping keylogger
```

## 📁 Project Structure

```
SCT_CS_4-KeyLogger/
│
├── keylogger.py          # Main keylogger program
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── .gitignore           # Git ignore rules
```

## 🔧 Technical Details

### Dependencies

- **pynput**: Python library for monitoring and controlling input devices

### Key Components

1. **Keylogger Class**: Main class that handles keystroke capture and logging
2. **on_press()**: Callback function triggered when a key is pressed
3. **on_release()**: Callback function triggered when a key is released
4. **Logging System**: Uses Python's logging module to write to file

## 🎓 Educational Value

This project demonstrates:

- Event-driven programming in Python
- Keyboard input monitoring
- File I/O operations
- Logging and timestamping
- Security awareness and ethical considerations

## 📚 Learning Resources

- Understanding keyloggers and their detection
- Ethical hacking principles
- Cybersecurity best practices
- Python keyboard monitoring libraries

## ⚖️ Legal Notice

This software is provided for educational purposes only. By using this software, you agree to:

1. Use it only on systems you own or have permission to monitor
2. Comply with all applicable local, state, national, and international laws
3. Not use it for malicious purposes
4. Take full responsibility for your actions

The author disclaims all liability for any misuse of this software.

## 📧 Contact

For questions or concerns about this educational project, please contact the repository owner.

---

**Remember: Always practice ethical hacking and responsible disclosure!**