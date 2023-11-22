import tkinter as tk
from tkinter import filedialog
import customtkinter
import filecmp
import os

class TextOperationsFrame(customtkinter.CTkTabview):
    def __init__(self, master):
        super().__init__(master, width=500)
        self.add("TextOp")
        self.add("Compare Files")
        self.add("Tab 3")
        self.tab("TextOp").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tab("Compare Files").grid_columnconfigure(0, weight=1)

        # textOp section
        self.op_label = customtkinter.CTkLabel(self.tab("TextOp"), text="Text Operations", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.op_label.grid(row=0, column=0, padx=20, pady=20)

        self.op_textbox = customtkinter.CTkTextbox(self.tab("TextOp"), height=60)
        self.op_textbox.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")

        self.select_file_button = customtkinter.CTkButton(self.tab("TextOp"), text="Select File", command=self.select_file)
        self.select_file_button.grid(row=1, column=1, padx=20, pady=(0, 20))

        self.checkboxes = []
        self.checkbox_vars = [tk.IntVar() for _ in range(3)]

        for i, (text, var) in enumerate(zip(["Word Count", "Reverse Text", "Text to Speech"], self.checkbox_vars)):
            cb = customtkinter.CTkCheckBox(self.tab("TextOp"), text=text, variable=var)
            cb.grid(row=i+2, column=0, padx=20, pady=(0, 10), sticky="w")
            self.checkboxes.append(cb)

        self.op_submit = customtkinter.CTkButton(self.tab("TextOp"), text="Process Text", command=self.handle_text_ops)
        self.op_submit.grid(row=5, column=0)

        self.file_path = None

        # Compare Files section
        self.com_label = customtkinter.CTkLabel(self.tab("Compare Files"), text="Select two files to compare", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.com_label.grid(row=0, column=0, padx=20)

        self.file1_entry = customtkinter.CTkEntry(self.tab("Compare Files"), placeholder_text="File1")
        self.file1_entry.grid(row=1, column=0)
        self.file2_entry = customtkinter.CTkEntry(self.tab("Compare Files"), placeholder_text="File2")
        self.file2_entry.grid(row=2, column=0)
        self.file1_button = customtkinter.CTkButton(self.tab("Compare Files"), text="Browse", command=self.browse_file_1)
        self.file1_button.grid(row=1, column=1, padx=20, pady=(10,0))
        self.file2_button = customtkinter.CTkButton(self.tab("Compare Files"), text="Browse", command=self.browse_file_2)
        self.file2_button.grid(row=2, column=1, padx=20, pady=(10,0))
        self.compare_button = customtkinter.CTkButton(self.tab("Compare Files"), text="Compare Files", command=self.compare_files)
        self.compare_button.grid(row=3, column=0, padx=20, pady=20)
        self.diff_label = customtkinter.CTkLabel(self.tab("Compare Files"), text="Differences:  ??%")
        self.diff_label.grid(row=3, column=1, padx=20)

    def select_file(self):
        file_types = [("Text files", ".txt")]
        file_path = filedialog.askopenfilename(filetypes=file_types)
        if file_path:
            self.file_path = file_path
            with open(file_path, "r") as f:
                text = f.read()
                self.op_textbox.delete(1.0, "end")
                self.op_textbox.insert(1.0, text)

    def handle_text_ops(self):
        if self.file_path:
            user_text = self.op_textbox.get("1.0", "end-1c")
        else:
            user_text = self.op_textbox.get("1.0", "end-1c") or self.read_file()

        output = []
        if self.checkbox_vars[0].get():
            print(f"Word Count: {len(user_text.split())}")

        if self.checkbox_vars[1].get():
            print(f"Reversed: {user_text[::-1]}")

        if self.checkbox_vars[2].get():
            # Assumption: gtts is installed
            print(f"Speech saved to: :D")

    def browse_file_1(self):
        file_path = filedialog.askopenfilename()
        self.file1_entry.delete(0, tk.END)
        self.file1_entry.insert(0, file_path)

    def browse_file_2(self):
        file_path = filedialog.askopenfilename()
        self.file2_entry.delete(0, tk.END)
        self.file2_entry.insert(0, file_path)

    def compare_files(self):
        pass

    def read_file(self):
        if self.file_path:
            with open(self.file_path, "r") as f:
                return f.read()
        return ""