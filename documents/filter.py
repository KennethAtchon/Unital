import customtkinter
from tkinter import filedialog
import os
import tkinter as tk
import subprocess
import re

class FilterFrame(customtkinter.CTkTabview):
    def __init__(self, master):
        super().__init__(master, width=250)
        self.add("Filter Text")
        self.tab("Filter Text").grid_columnconfigure(0, weight=1)

        self.filter_label = customtkinter.CTkLabel(self.tab("Filter Text"), text="Filter Docx File", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.filter_label.grid(row=0, column=0, padx=20, pady=5)

        self.filter_textbox = customtkinter.CTkTextbox(
            self.tab("Filter Text"),
            height=50
        )
        self.filter_textbox.grid(row=1, columnspan=2, padx=20, pady=(0, 20), sticky="nsew")

        self.filter_textbox.insert("1.0", "Enter words to filter (comma-separated)")

        self.file_path_entry = customtkinter.CTkEntry(self.tab("Filter Text"), placeholder_text="Enter the path to docx file")
        self.file_path_entry.grid(row=2, column=0, padx=20)

        self.browse_button_1 = customtkinter.CTkButton(self.tab("Filter Text"), text="Browse", command=self.browse_file_1)
        self.browse_button_1.grid(row=2, column=1, padx=20)

        self.filter_button = customtkinter.CTkButton(self.tab("Filter Text"), text="Filter Text", command=self.filter_docx)
        self.filter_button.grid(row=3, column=0, padx=20, pady=(10,0))

    
    def filter_docx(self):
        # Get user inputs
        words_to_filter = self.filter_textbox.get("1.0", tk.END).strip()
        file_path = self.file_path_entry.get()

        # Validate inputs
        if not words_to_filter or not file_path:
            # Handle empty inputs or show an error message
            print("Please enter words to filter and the path to the docx file.")
            return

        # Split the words and remove leading/trailing spaces
        filter_words = [word.strip().lower() for word in words_to_filter.split(',')]

        try:
            # Read the content of the docx file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

                # Filter the content
                for word in filter_words:
                    # Use a case-insensitive replace for each filter word
                    content = re.compile(re.escape(word), re.IGNORECASE).sub('', content)

                # Write the filtered content back to the docx file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)

                print(f"Docx file filtered successfully. Filtered words: {', '.join(filter_words)}")
        except Exception as e:
            print(f"Error filtering docx file: {e}")



    def browse_file_1(self):
        file_types = [("Accepted Files", ".txt .docx .py .java .html .css .js"), ("Other Files", "")]
        file_path = filedialog.askopenfilename(filetypes=file_types)
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, file_path)



