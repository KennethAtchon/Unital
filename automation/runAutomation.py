import threading
import time
import pyautogui
import re

class runAuto:
    def __init__(self, automation_code):
        print(automation_code)
        self.automation_code = automation_code
        self.running = False
        self.stop_event = threading.Event() 
        self.command_actions = {
            "Left Click": self.left_click_action,
            "Right Click": self.right_click_action,
            "Double Click": self.double_click_action,
            "Mouse Position": self.mouse_position_action,
            "Scroll": self.scroll_action,
            "Keystroke": self.keystroke_action,
            "Type": self.type_action,
            "Keydown": self.keydown_action,
            "Keyup": self.keyup_action,
            "If": self.if_action,
            "For": self.for_action
        }

    def process_automation(self):
        lines = self.automation_code.splitlines()  # Split the string into lines
        decoded_data = []  # Initialize an empty list to store decoded data

        for line in lines:
            if line == "":
                break
            decoded_data.append(self.decode_string(line))

        for data in decoded_data:
            self.pick_command(data)

        print("Automation Complete")
        self.stop_automation()

    def pick_command(self, data):
        command, argument, delay = data
        action_function = self.command_actions.get(command)
        if action_function:
            action_function(argument, delay)
        else:
            print(f"Unknown command: {command}")


    def decode_string(self,input_string):
        parts = input_string.split('-')
        command = parts[1][1:].strip()
        argument = parts[2][1:].strip()
        delay = parts[3][1:].strip()
        return [command, argument, delay]


    def start_automation(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.process_automation)
            self.thread.start()
        else:
            print("Automation is already running.")

    def stop_automation(self):
        if self.running:
            self.running = False
            self.stop_event.set()  
            self.stop_event.clear()  
            print("Automation stopped.")
        else:
            print("Automation is not running.")


    def left_click_action(self, argument, delay):
        pyautogui.click(button='left')
        self.stimulate_delay(delay)
        print(f"Left Click: Argument - {argument}, Delay - {delay}")

    def right_click_action(self, argument, delay):
        pyautogui.click(button='right')
        self.stimulate_delay(delay)
        print(f"Right Click: Argument - {argument}, Delay - {delay}")

    def double_click_action(self, argument, delay):
        pyautogui.doubleClick()
        self.stimulate_delay(delay)
        print(f"Double Click: Argument - {argument}, Delay - {delay}")

    def mouse_position_action(self, argument, delay):
        pattern = r'\(\s*(\d+)\s*,\s*(\d+)\s*\)'
        match = re.match(pattern, argument)
        if not match:
            return
        
        x, y = match.groups()
        x = int(x)
        y = int(y)
        pyautogui.moveTo(x, y, duration=0.5)
        self.stimulate_delay(delay)
        print(f"Mouse Position: Argument - {argument}, Delay - {delay}")

    def scroll_action(self, argument, delay):
        pyautogui.scroll(int(argument))
        self.stimulate_delay(delay)
        print(f"Scroll: Argument - {argument}, Delay - {delay}")

    def keystroke_action(self, argument, delay):
        pyautogui.typewrite(argument)
        self.stimulate_delay(delay)
        print(f"Keystroke: Argument - {argument}, Delay - {delay}")

    def type_action(self, argument, delay):
        pyautogui.write(argument)
        self.stimulate_delay(delay)
        print(f"Type: Argument - {argument}, Delay - {delay}")

    def keydown_action(self, argument, delay):
        pyautogui.keyDown(argument)
        self.stimulate_delay(delay)
        print(f"Keydown: Argument - {argument}, Delay - {delay}")

    def keyup_action(self, argument, delay):
        pyautogui.keyUp(argument)
        self.stimulate_delay(delay)
        print(f"Keyup: Argument - {argument}, Delay - {delay}")

    def if_action(self, argument, delay):
        print(f"If: Argument - {argument}, Delay - {delay}")

    def for_action(self, argument, delay):
        print(f"For: Argument - {argument}, Delay - {delay}")

    def stimulate_delay(self, delay):
        delay_seconds = float(delay) / 1000.0  
        time.sleep(delay_seconds)


