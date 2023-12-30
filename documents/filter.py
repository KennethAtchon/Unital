import customtkinter
from tkinter import filedialog
import os
import subprocess
import tkinter as tk
import time

class FilterFrame(customtkinter.CTkTabview):
    def __init__(self, master):
        super().__init__(master, width=250)
        self.add("Filter Text")
        self.tab("Filter Text").grid_columnconfigure(0, weight=1)
        
        self.d2p_label = customtkinter.CTkLabel(self.tab("Filter Text"), text="Converts docx file to Pdf", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.d2p_entry = customtkinter.CTkEntry(self.tab("Filter Text"), placeholder_text="Enter the path to docx...")



