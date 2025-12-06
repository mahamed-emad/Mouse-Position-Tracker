import pyautogui
import ctypes
import tkinter as tk

def check_keyboard_is_en():
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    while True:
        curr_window = user32.GetForegroundWindow()
        thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
        klid = user32.GetKeyboardLayout(thread_id)
        lid_hex = hex(klid & 0xFFFF)

        if lid_hex == '0x409':  # English
            break

        with pyautogui.hold("shift"):
            pyautogui.press("alt")

def get_colour():
    screenshot = pyautogui.screenshot()
    r, g, b = screenshot.getpixel((896, 1062))
    return f"#{r:02X}{g:02X}{b:02X}"

def get_mouse_position():
    pos = pyautogui.position()
    return f"x= {pos.x}, y= {pos.y}"

def copy_text(event, app_window):
    app_window.clipboard_clear()
    app_window.clipboard_append(get_mouse_position())

def show_mouse_position():
    app_window = tk.Tk()
    app_window.geometry("250x85")
    app_window.title("Mouse Position")

    background = "#272727"
    app_window.configure(bg=background)

    colour = get_colour()
    app_window.attributes("-alpha", 0.9)

    text = tk.Label(app_window, text="<< Mouse Position  >>",
                    font=("Arial", 8), bg=background, fg=colour)
    text.pack()

    note = tk.Label(app_window, text='To copy press ctrl + c',
                    font=("Arial", 10), bg=background, fg=colour)
    note.pack()

    position_text = tk.Label(app_window, text=get_mouse_position(),
                             font=("Arial", 18), bg=background, fg=colour)
    position_text.pack()

    developer_named = tk.Label(app_window,
                    text="Made With Love ❤️ By Mahamed Emad",
                    font=("Arial", 7), bg=background, fg=colour)
    developer_named.pack()

    app_window.after(600, update_position_and_colour,
                     text, position_text, developer_named, note, app_window)

    app_window.bind("<Control-c>", lambda e: copy_text(e, app_window))
    app_window.bind("<Control-C>", lambda e: copy_text(e, app_window))

    app_window.mainloop()

def update_position_and_colour(text, position_text, developer_named, note, app_window):
    colour = get_colour()

    widgets = [text, position_text, developer_named, note]
    for w in widgets:
        w.config(fg=colour)

    position_text.config(text=get_mouse_position())

    position_text.after(600, update_position_and_colour,
                        text, position_text, developer_named, note, app_window)

check_keyboard_is_en()
show_mouse_position()
