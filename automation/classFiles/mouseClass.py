import customtkinter
import tkinter as tk


class MousePositionDialog(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("400x250")
        self.title("Mouse Position") 
        self.attributes('-topmost', True)

        label_x = customtkinter.CTkLabel(self, text="X Position:")
        label_x.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.entry_x = customtkinter.CTkEntry(self)
        self.entry_x.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        label_y = customtkinter.CTkLabel(self, text="Y Position:")
        label_y.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.entry_y = customtkinter.CTkEntry(self)
        self.entry_y.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        label_delay = customtkinter.CTkLabel(self, text="Delay (ms):")
        label_delay.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.entry_delay = customtkinter.CTkEntry(self)
        self.entry_delay.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        button_search = customtkinter.CTkButton(self, text="Search Position", command=self.handle_search)
        button_search.grid(row=3, column=0, padx=10, pady=(20, 0), sticky="w")

        button_ok = customtkinter.CTkButton(self, text="OK", command=self.handle_ok)
        button_ok.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")

        button_cancel = customtkinter.CTkButton(self, text="Cancel", command=self.destroy)
        button_cancel.grid(row=4, column=1, padx=10, pady=(10, 0), sticky="w")

    def handle_ok(self):
        x_pos = self.entry_x.get()
        y_pos = self.entry_y.get()
        delay = self.entry_delay.get()
        self.argument = f"({x_pos}, {y_pos})" if x_pos.isdigit() and y_pos.isdigit() else "None"

        if self.argument == "None":
            self.master.alert_user_argument("position x and y.")
            self.destroy()
            return

        if self.master.validate_number(delay):
            self.delay = delay
            print("X Position:", x_pos)
            print("Y Position:", y_pos)
            print("Delay:", delay)
            print("Argument:", self.argument)
            self.destroy()

    def handle_search(self):
        # Add search logic here
        pass

class MouseScrollDialog(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("400x250")
        self.title("Mouse Position") 
        self.attributes('-topmost', True)

        self.scrollspeed = customtkinter.CTkLabel(self, text="Scroll speed:")
        self.scrollspeed.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.entry_scrollspeed = customtkinter.CTkEntry(self)
        self.entry_scrollspeed.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        label_delay = customtkinter.CTkLabel(self, text="Delay (ms):")
        label_delay.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.entry_delay = customtkinter.CTkEntry(self)
        self.entry_delay.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        button_ok = customtkinter.CTkButton(self, text="OK", command=self.handle_ok)
        button_ok.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")

        button_cancel = customtkinter.CTkButton(self, text="Cancel", command=self.destroy)
        button_cancel.grid(row=4, column=1, padx=10, pady=(10, 0), sticky="w")

    def handle_ok(self):
        scrollspeed1 = self.entry_scrollspeed.get()
        delay = self.entry_delay.get()
        self.argument = scrollspeed1 if self.master.validate_number(scrollspeed1) else "None"

        if self.master.validate_number(delay):
            self.delay = delay
            print("Scroll Speed:", scrollspeed1)
            print("Delay:", delay)
            print("Argument:", self.argument)
            self.destroy()

