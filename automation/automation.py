import customtkinter
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image


class AutomationFrame(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        style = ttk.Style(self)
        style.configure('Grey.TSeparator', background='grey')
        
        self.configure(corner_radius=10)  # Customize appearance
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.grid_rowconfigure((0,1,2,3,4,5,6), weight=0)
        
        # Add a 'Save' button to the left
        self.save_button = customtkinter.CTkButton(self, text="Save", command=self.on_save_click, width=100, height=40, corner_radius=10)
        self.save_button.grid(row=0, column=0, padx=(40,0), pady=10, sticky="nw")

        self.separator1 = ttk.Separator(self, orient='vertical', style='Grey.TSeparator')
        self.separator1.grid(row=0, column=1, sticky='ns')

        # Create clickable title buttons for the sections
        self.record_button = customtkinter.CTkButton(self, text="Record", command=self.on_record_click, width=120, height=40, corner_radius=10)
        self.record_button.grid(row=0, column=2, padx=10, pady=5)
        
        self.smart_click_button = customtkinter.CTkButton(self, text="Smart Click", command=self.on_smart_click, width=120, height=40, corner_radius=10)
        self.smart_click_button.grid(row=0, column=3, padx=10, pady=5)
        
        self.play_button = customtkinter.CTkButton(self, text="Play", command=self.on_play_click, width=120, height=40, corner_radius=10)
        self.play_button.grid(row=0, column=4, padx=10, pady=5)

        self.separator2 = ttk.Separator(self, orient='vertical', style='Grey.TSeparator')
        self.separator2.grid(row=0, column=5, sticky='ns')

        # Add a 'Delete' button to the right
        self.delete_button = customtkinter.CTkButton(self, text="Delete", command=self.on_delete_click, width=100, height=40, corner_radius=10)
        self.delete_button.grid(row=0, column=6, padx=10, pady=10, sticky="ne")

        self.bottom_separator = ttk.Separator(self, orient='horizontal', style='Grey.TSeparator')
        self.bottom_separator.grid(row=1, column=0, columnspan=7, sticky='ew')

        self.sidebar_frame = customtkinter.CTkFrame(self, corner_radius=10)
        self.sidebar_frame.grid(row=2, column=0, padx=10, pady=10, sticky='nsew', rowspan = 5)
        self.grid_rowconfigure(2, weight=1)

        options1 = ["Option 1-1", "Option 1-2", "Option 1-3"]
        options2 = ["Option 2-1", "Option 2-2", "Option 2-3"]
        options3 = ["Option 3-1", "Option 3-2", "Option 3-3"]

        # Create option menus and add them to the sidebar frame
        self.option_menu1 = customtkinter.CTkOptionMenu(self.sidebar_frame, values=options1, width=90)
        self.option_menu1.grid(row=1, column=0, padx=12.5, pady=30, sticky='nw')

        self.option_menu2 = customtkinter.CTkOptionMenu(self.sidebar_frame, values=options2, width=90)
        self.option_menu2.grid(row=2, column=0, padx=12.5, pady=30, sticky='nw')

        self.option_menu3 = customtkinter.CTkOptionMenu(self.sidebar_frame, values=options3, width=90)
        self.option_menu3.grid(row=3, column=0, padx=12.5, pady=30, sticky='nw')

        self.main_section_top = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_section_bottom = customtkinter.CTkFrame(self, corner_radius=10)

        self.main_section_top.grid(row=2, column=1, padx=10, pady=10, sticky="nsew", rowspan=4, columnspan = 6)  # This section is three times larger
        self.main_section_bottom.grid(row=6, column=1, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan = 6)  # This section is the smaller one

        self.grid_columnconfigure(1, weight=3)  # This column will contain the two main sections

        self.radio_var = tk.IntVar(value=0)

        self.play_options_label = customtkinter.CTkLabel(self.main_section_bottom, text="Play Options")
        self.play_options_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.radio_button_once = customtkinter.CTkRadioButton(self.main_section_bottom, variable=self.radio_var, value=0, text="Repeat once", command=self.on_play_option_change)
        self.radio_button_once.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.radio_button_times = customtkinter.CTkRadioButton(self.main_section_bottom, variable=self.radio_var, value=1, text="Repeat 10 times", command=self.on_play_option_change)
        self.radio_button_times.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.radio_button_for_time = customtkinter.CTkRadioButton(self.main_section_bottom, variable=self.radio_var, value=2, text="Repeat for 1 minute", command=self.on_play_option_change)
        self.radio_button_for_time.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.separator3 = ttk.Separator(self.main_section_bottom, orient='vertical', style='Grey.TSeparator')
        self.separator3.grid(row=1, column=1, rowspan=3, sticky='ns', padx=100)

        # Shutdown option checkbox
        self.shutdown_checkbox = customtkinter.CTkCheckBox(self.main_section_bottom, text="Shutdown computer when repeating finished", command=self.on_shutdown_click)
        self.shutdown_checkbox.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        # View Execution Log button
        self.view_log_button = customtkinter.CTkButton(self.main_section_bottom, text="View Execution Log", command=self.on_view_log_click)
        self.view_log_button.grid(row=2, column=2, padx=10, pady=10, sticky="w")

        self.main_section_top.grid_rowconfigure(0, weight=1)  # Make the row expandable
        self.main_section_top.grid_columnconfigure(0, weight=1)  # Make the second column expandable (where the text widget will be)

        self.textbox = customtkinter.CTkTextbox(self.main_section_top)
        self.textbox.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.textbox.configure(state='disabled')
        
        # Method placeholders for button click events
    def on_record_click(self):
        print("Record button clicked")
        # Add functionality for record button click here

    def on_smart_click(self):
        print("Smart Click button clicked")
        # Add functionality for smart click button click here

    def on_play_click(self):
        print("Play button clicked")
        # Add functionality for play button click here

    def on_save_click(self):
        print("Save button clicked")
        # Add functionality for save button click here

    def on_delete_click(self):
        print("Delete button clicked")
        # Add functionality for delete button click here
    
    # Placeholders for functions to be bound to the new GUI elements

    def on_repeat_once_click(self):
        print("Repeat once selected")
        # Add functionality for repeat once click here

    def on_repeat_times_click(self):
        print("Repeat times selected")
        # Add functionality for repeat times click here

    def on_repeat_for_time_click(self):
        print("Repeat for time selected")
        # Add functionality for repeat for time click here

    def on_shutdown_click(self):
        print("Shutdown option selected")
        # Add functionality for shutdown option click here

    def on_view_log_click(self):
        print("View Execution Log clicked")
        # Add functionality for view execution log click here

    def on_play_option_change(self):
        print(f"Selected play option: {self.radio_var.get()}")
        # Add functionality here based on the value of self.radio_var