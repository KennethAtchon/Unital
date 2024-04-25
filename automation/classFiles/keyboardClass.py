import customtkinter
import tkinter as tk


class KeyStroke(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("400x250")
        self.title("KeyStroke") 
        self.attributes('-topmost', True)

        self.keystroke = customtkinter.CTkLabel(self, text="Keystroke:")
        self.keystroke.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.entry_keystroke = customtkinter.CTkEntry(self)
        self.entry_keystroke.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        label_delay = customtkinter.CTkLabel(self, text="Delay (ms):")
        label_delay.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.entry_delay = customtkinter.CTkEntry(self)
        self.entry_delay.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        button_ok = customtkinter.CTkButton(self, text="OK", command=self.handle_ok)
        button_ok.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")

        button_cancel = customtkinter.CTkButton(self, text="Cancel", command=self.destroy)
        button_cancel.grid(row=4, column=1, padx=10, pady=(10, 0), sticky="w")

    def handle_ok(self):
        keystroke1 = self.entry_keystroke.get()
        delay = self.entry_delay.get()
        self.argument = keystroke1[0] if keystroke1.isalnum() else "None"


        if self.master.validate_number(delay):
            self.delay = delay
            print("Keystroke:", keystroke1)
            print("Delay:", delay)
            print("Argument:", self.argument)
            self.destroy()


class KeyType(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("400x250")
        self.title("KeyType") 
        self.attributes('-topmost', True)

        self.keytype = customtkinter.CTkLabel(self, text="KeyType:")
        self.keytype.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.entry_keytype = customtkinter.CTkEntry(self)
        self.entry_keytype.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        label_delay = customtkinter.CTkLabel(self, text="Delay (ms):")
        label_delay.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.entry_delay = customtkinter.CTkEntry(self)
        self.entry_delay.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        button_ok = customtkinter.CTkButton(self, text="OK", command=self.handle_ok)
        button_ok.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")

        button_cancel = customtkinter.CTkButton(self, text="Cancel", command=self.destroy)
        button_cancel.grid(row=4, column=1, padx=10, pady=(10, 0), sticky="w")

    def handle_ok(self):
        keytype1 = self.entry_keytype.get()
        delay = self.entry_delay.get()
        self.argument = keytype1


        if self.master.validate_number(delay):
            self.delay = delay
            print("KeyType:", keytype1)
            print("Delay:", delay)
            print("Argument:", self.argument)
            self.destroy()
