# Mouse-Position-Tracker
A lightweight desktop utility that displays real-time mouse coordinates with dynamic UI coloring and instant copy-to-clipboard support.
# 🖱️ Mouse Position Tracker

A lightweight desktop tool built with **Python** and **Tkinter** that displays the real-time position of your mouse cursor on the screen.  
The tool also allows you to **copy the coordinates** instantly using `Ctrl + C`.

---

## ✨ Features

✔ Shows real-time mouse coordinates (x, y)  
✔ Allows copying coordinates with a single shortcut (`Ctrl + C`)  
✔ Auto-adjusts UI color dynamically based on a selected pixel  
✔ Lightweight & always-on-top style window  
✔ Auto-switches keyboard layout to English before startup  
✔ Created for personal productivity and UI/automation work

---

## 🖥️ Preview  
A tiny, minimal, floating window showing:
- Title  
- Copy instructions  
- Live mouse coordinates  
- Developer credit  

*(UI is intentionally simple & lightweight.)*

---

## 📌 How It Works

### 1️⃣ **Tracking the mouse position**  
The program uses `pyautogui.position()` to continuously read the cursor location.

### 2️⃣ **Reading color under a specific pixel**  
A screenshot is taken every 600 ms and a pixel color is extracted to theme the UI.

### 3️⃣ **Automatic English keyboard layout switching**  
The app ensures your keyboard is in English using Win32 API via `ctypes`.

### 4️⃣ **Copy to clipboard**  
Pressing `Ctrl + C` copies the current `x, y` coordinates.

---

## 🚀 Installation

### **1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/Mouse-Position-Tracker.git
cd Mouse-Position-Tracker
```

### **2. Install dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the app**
```bash
python src/mouse_position.py
```

## 📦 Build EXE (Optional)

If you want to package it:
```bash
pyinstaller --noconsole --onefile --icon="Mouse Position.ico" mouse_position.py
```

## 🧩 Project Structure

```
Mouse-Position-Tracker/
│
├── src/
│   └── mouse_position.py     # Main application
│
├── README.md
│
├── requirements.txt
│
└── Mouse Position.ico         # Optional icon
```

## 👤 Developer

Made With Love ❤️ By Mahamed Emad
