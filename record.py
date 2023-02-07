import pyautogui
from pynput import keyboard

clicks = []

def on_press(key):
    print('pressed ')
    if key == keyboard.Key.esc:
        return False
    else:
        click = pyautogui.position()
        clicks.append(str(click.x) +','+ str(click.y))


with keyboard.Listener(on_press=lambda event: on_press(event), suppress=True) as listener:
    listener.join()

path_to_file = 'config.ini'
file_to_delete = open(path_to_file,'w')
file_to_delete.close()

with open(path_to_file, 'w') as f:
    for click in clicks:
        f.write(click+'\n')
