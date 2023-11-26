import customtkinter
from tkinter import filedialog
import os
import subprocess
import tkinter as tk

class ConvertFrame(customtkinter.CTkTabview):
    def __init__(self, master):
        super().__init__(master, width=250)
        self.add("Doc2Pdf")
        self.tab("Doc2Pdf").grid_columnconfigure(0, weight=1)
        
        self.d2p_label = customtkinter.CTkLabel(self.tab("Doc2Pdf"), text="Converts docx file to Pdf", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.d2p_entry = customtkinter.CTkEntry(self.tab("Doc2Pdf"), placeholder_text="Enter the path to docx...")
        self.d2p_browse_button = customtkinter.CTkButton(self.tab("Doc2Pdf"), text="Browse", command=self.browse_file_d2p)
        self.d2p_browse_button.grid(row=2, column=1, padx=10, pady=(20, 0))
        self.d2psubmit_button = customtkinter.CTkButton(self.tab("Doc2Pdf"), text="Convert", command=self.convert_docx_to_pdf)
        self.d2p_label.grid(row=0, column=0)
        self.d2psubmit_button.grid(row=3, column=0, pady=(20,0))
        self.d2p_entry.grid(row=2, column=0, padx=(20, 0), pady=(20, 0),  sticky="nsew")

        self.progressbar_1 = customtkinter.CTkProgressBar(self.tab("Doc2Pdf"))
        self.progressbar_1.grid(row=4, column=0, pady=(20, 0), sticky="ew")
        self.progressbar_1.set(0)
        self.progressbar_1.configure(mode="determinate")
    def browse_file_d2p(self):
        file_types = [("Doc files", ".docx")]
        file_path = filedialog.askopenfilename(title="Select a .docx File", filetypes=file_types)
        if file_path:
            self.d2p_entry.delete(0, tk.END)  # Clear any existing text
            self.d2p_entry.insert(0, file_path)


    def convert_docx_to_pdf(self):
        docx_path = self.d2p_entry.get()
        pdf_path = os.path.splitext(docx_path)[0]

        self.progressbar_1.start()
        self.progressbar_1.update_idletasks()  # Force update before subprocess call

        # Schedule the subprocess call after a brief delay
        self.after(1500, self.execute_conversion, docx_path, pdf_path)

    def execute_conversion(self, docx_path, pdf_path):
        try:
            subprocess.call([r"C:\Program Files\LibreOffice\program\soffice.exe",
                '--convert-to',
                'pdf',
                '--outdir',
                pdf_path,
                docx_path])

            # Your conversion code here

        finally:
            # Stop the progress bar regardless of the conversion result
            self.progressbar_1.stop()
            self.progressbar_1.set(0)
