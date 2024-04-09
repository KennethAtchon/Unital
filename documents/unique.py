import customtkinter
from tkinter import filedialog
import os
import subprocess
import tkinter as tk
import time
import nltk
from nltk.corpus import wordnet
from nltk.corpus import words
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def download_nltk_resources():
    print("Downloading NLTK resources...")
    nltk.download('wordnet')
    nltk.download('words')

class UniqueFrame(customtkinter.CTkTabview):
    def __init__(self, master, nltk_installed=False):
        super().__init__(master, width=250)
        self.nltk_installed = nltk_installed 

        self.add("Word Cloud")
        self.tab("Word Cloud").grid_columnconfigure(0, weight=1)
        
        self.wc_label = customtkinter.CTkLabel(self.tab("Word Cloud"), text="Create a Word Cloud", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.wc_label.grid(row=0, column=0, padx=0, pady=5)
        
        self.wc_textbox = customtkinter.CTkTextbox(
            self.tab("Word Cloud"),
            height=80
        )
        self.wc_textbox.grid(row=1, columnspan=2, padx=20, pady=(0, 10), sticky="nsew")
        self.wc_textbox.insert("1.0", "Enter words to use for the word cloud(comma-separated)")
        
        self.wc_submit = customtkinter.CTkButton(self.tab("Word Cloud"), text="Submit", command= self.generate_wc)
        self.wc_submit.grid(row=3, column=0, padx=20, pady=(10,0))
        
        self.file_path = os.getcwd() + "\\"

        # Disable functionality if NLTK resources are not downloaded yet
        if not self.nltk_installed:
            self.disable_functionality()
        else:
            # If nltk_installed is True, download resources immediately
            download_nltk_resources()

    def disable_functionality(self):
        # Disable the submit button and adjust its text to indicate disabled state
        self.wc_submit.configure(state="disabled", text="Downloading NLTK...")

    def generate_wc(self):
        synonyms = set()
        words1 = self.wc_textbox.get("1.0", tk.END).strip()
        input_words = words1.split(',')
        
        for input_word in input_words:
            for syn in wordnet.synsets(input_word):
                for lemma in syn.lemmas():
                    synonyms.add(lemma.name().lower())
        
        # Filter out the original words and non-English words
        for input_word in input_words:
            synonyms.discard(input_word.lower())
        
        english_words = set(words.words())  # Note: Fixed 'words' reference
        synonyms = list(synonyms.intersection(english_words))
        synonyms_text = ' '.join(synonyms)
        
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(synonyms_text)
        
        # Display the generated word cloud using matplotlib
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(self.file_path + "\\WorldCloud")
        plt.show()

    def update_nltk_status(self, installed):
        self.nltk_installed = installed
        if installed:
            download_nltk_resources()
            self.enable_functionality()  # You might need to implement this method
        else:
            self.disable_functionality()

    def disable_functionality(self):
        # Method to disable functionality if NLTK resources are not downloaded
        print("Disabling")
        self.wc_submit.configure(state="disabled", text="Downloading NLTK...")

    # Implement the enable functionality method to re-enable the UI components
    def enable_functionality(self):
        self.wc_submit.configure(state="normal", text="Submit")

