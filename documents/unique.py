import customtkinter
from tkinter import filedialog
import os
import subprocess
import tkinter as tk
import time

#word cloud using ntlk and spacy

class UniqueFrame(customtkinter.CTkTabview):
    def __init__(self, master):
        super().__init__(master, width=250)
        self.add("Word Cloud")
        self.tab("Word Cloud").grid_columnconfigure(0, weight=1)
        
        self.d2p_label = customtkinter.CTkLabel(self.tab("Word Cloud"), text="Converts docx file to Pdf", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.d2p_entry = customtkinter.CTkEntry(self.tab("Word Cloud"), placeholder_text="Enter the path to docx...")


