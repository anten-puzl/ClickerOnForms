from os.path import exists
import pyautogui
import tkinter as tk
from time import sleep
import keyboard
import threading

root = tk.Tk()
root.geometry("250x50")
name_var = tk.StringVar()

event = threading.Event()


def make_clicks(pause):
    path_to_file = 'config.ini'

    if not exists(path_to_file):
        exit()

    with open(path_to_file, 'r') as f:
        lines = f.read().splitlines()
        while not event.is_set():
            for line in lines:
                coordinates = line.split(',')
                x = int(coordinates[0])
                y = int(coordinates[1])
                pyautogui.click(x, y)
                print(x)
                sleep(pause)


def Start():
    pause = int(time_entry.get())
    root.destroy()
    make_clicks(pause)


def stop():
    event.set()
    print("stop")


keyboard.add_hotkey("esc", stop)

time_label = tk.Label(root, text='pause, sec ', font=('calibre', 10, 'bold'))
time_entry = tk.Entry(root, textvariable=time_label, font=('calibre', 10, 'normal'))
sub_btn = tk.Button(root, text='Start', command=Start)
root.lift()

time_label.grid(row=0, column=0)
time_entry.grid(row=0, column=1)
sub_btn.grid(row=2, column=1)

# performing an infinite loop
# for the window to display
root.mainloop()
