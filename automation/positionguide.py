import pyautogui
import keyboard

def find_mouse_position():
    print("Move your mouse to the desired position and press Ctrl+C to retrieve the position.")
    while True:
        if keyboard.is_pressed('ctrl+c'):
            break
    
    mouse_position = pyautogui.position()
    print(f"Mouse position: {mouse_position}")

find_mouse_position()
