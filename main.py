#imports
from concurrent.futures import wait
from asyncio import wait
import tkinter as tk
import customtkinter as ctk      #pip install customtkinter
import numpy as np               #pip install numpy
from PIL import Image, ImageTk   #pip install pillow
from pathlib import Path

#variables/settings
app = ctk.CTk()
icon_path = Path(__file__).resolve().parent / "images" / "icon.ico"
app.iconbitmap(default=str(icon_path))
app.geometry("350x320")
app.title("stopwatch")
app.resizable(False, False)
#app.iconphoto(False, tk.PhotoImage(file="H:/Coding/Python projects/join me/comment.png"))
ctk.set_appearance_mode("dark")
interval = 0.001 #seconds
cur_time = 0.000 #current time, seconds
timer_callback = None
#funtctions
def start_timer():
    global cur_time
    global timer_callback

    if timer_callback is not None:
        return

    start_button.configure(state="disabled")
    pause_button.configure(state="normal")
    stop_button.configure(state="normal")

    def update_timer():
        global cur_time
        global timer_callback

        cur_time += interval
        time_label.configure(text=f"{cur_time:.3f}")
        timer_callback = app.after(max(1, int(interval * 1000)), update_timer)

    timer_callback = app.after(max(1, int(interval * 1000)), update_timer)


def pause_timer():
    global timer_callback

    if timer_callback is not None:
        app.after_cancel(timer_callback)
        timer_callback = None

    time_label.configure(text=f"{cur_time:.3f}")

    start_button.configure(state="normal")
    pause_button.configure(state="disabled")
    stop_button.configure(state="normal")


def stop_timer():
    global cur_time

    pause_timer()
    cur_time = 0.000
    time_label.configure(text=f"{cur_time:.3f}")

    stop_button.configure(state="disabled")

#elements
bg_frame = ctk.CTkFrame(app, border_width=2, fg_color="#16002F")
bg_frame.pack(pady=0, padx=0, fill="both", expand=True)

time_label = ctk.CTkLabel(bg_frame, text=f"{cur_time:.3f}", font=("Century Gothic", 70), text_color="#FFFFFF")
time_label.pack(pady=20, padx=20)

start_button = ctk.CTkButton(bg_frame, text="▶", font=("Century Gothic", 20), command=lambda: start_timer())
start_button.pack(pady=15)

pause_button = ctk.CTkButton(bg_frame, text="⏸", font=("Century Gothic", 20), command=pause_timer)
pause_button.pack(pady=15)

stop_button = ctk.CTkButton(bg_frame, text="⏹", font=("Century Gothic", 20), command=stop_timer)
stop_button.pack(pady=15)

app.mainloop()