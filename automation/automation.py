import customtkinter
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image
import tkinter.filedialog as fd
from tkinter import messagebox
from automation.mouseClass import MousePositionDialog, MouseScrollDialog

class AutomationFrame(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        style = ttk.Style(self)
        style.configure('Grey.TSeparator', background='grey')
        
        self.configure(corner_radius=10)  # Customize appearance
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=0)  

        self.save_button = customtkinter.CTkButton(self, text="Save", command=self.on_save_click, width=80, height=40, corner_radius=10)
        self.save_button.grid(row=0, column=0, padx=(10,0), pady=10, sticky="ns")
        
        self.open_button = customtkinter.CTkButton(self, text="Open", command=self.on_open_click, width=80, height=40, corner_radius=10)
        self.open_button.grid(row=0, column=1, pady=10, sticky="ns")

        self.separator1 = ttk.Separator(self, orient='vertical', style='Grey.TSeparator')
        self.separator1.grid(row=0, column=2, sticky='ns')

        # Create clickable title buttons for the sections
        self.record_button = customtkinter.CTkButton(self, text="Record", command=self.on_record_click, width=120, height=40, corner_radius=10)
        self.record_button.grid(row=0, column=3, padx=10, pady=5)
        
        self.smart_click_button = customtkinter.CTkButton(self, text="Smart Click", command=self.on_smart_click, width=120, height=40, corner_radius=10)
        self.smart_click_button.grid(row=0, column=4, padx=10, pady=5)
        
        self.play_button = customtkinter.CTkButton(self, text="Play", command=self.on_play_click, width=120, height=40, corner_radius=10)
        self.play_button.grid(row=0, column=5, padx=10, pady=5)

        self.separator2 = ttk.Separator(self, orient='vertical', style='Grey.TSeparator')
        self.separator2.grid(row=0, column=6, sticky='ns')

        # Add a 'Delete' button to the right
        self.delete_button = customtkinter.CTkButton(self, text="Delete", command=self.on_delete_click, width=100, height=40, corner_radius=10)
        self.delete_button.grid(row=0, column=7, padx=10, pady=10, sticky="ne")

        self.bottom_separator = ttk.Separator(self, orient='horizontal', style='Grey.TSeparator')
        self.bottom_separator.grid(row=1, column=0, columnspan= 8, sticky='ew')

        self.sidebar_frame = customtkinter.CTkFrame(self, corner_radius=10)
        self.sidebar_frame.grid(row=2, column=0, padx=10, pady=10, sticky='nsew', rowspan = 5)
        self.grid_rowconfigure(2, weight=1)

        options1 = ["Mouse", "Left Click", "Right Click","Double Click", "Mouse Position", "Scroll"]
        options2 = ["Option 2-1", "Option 2-2", "Option 2-3"]
        options3 = ["Option 3-1", "Option 3-2", "Option 3-3"]

        # Create option menus and add them to the sidebar frame
        self.option_menu1 = customtkinter.CTkOptionMenu(self.sidebar_frame, values=options1, command=self.option_menu1_callback, width=90)
        self.option_menu1.grid(row=1, column=0, padx=12.5, pady=30, sticky='nw')

        self.option_menu2 = customtkinter.CTkOptionMenu(self.sidebar_frame, values=options2, width=90)
        self.option_menu2.grid(row=2, column=0, padx=12.5, pady=30, sticky='nw')

        self.option_menu3 = customtkinter.CTkOptionMenu(self.sidebar_frame, values=options3, width=90)
        self.option_menu3.grid(row=3, column=0, padx=12.5, pady=30, sticky='nw')

        self.main_section_top = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_section_bottom = customtkinter.CTkFrame(self, corner_radius=10)

        self.main_section_top.grid(row=2, column=1, padx=10, pady=10, sticky="nsew", rowspan=4, columnspan = 7)  # This section is three times larger
        self.main_section_bottom.grid(row=6, column=1, padx=10, pady=10, sticky="nsew", rowspan=1, columnspan = 7)  # This section is the smaller one

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

        self.linenumber = 1
        
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
        # Get the content from the text box or another source
        content = self.textbox.get("1.0", tk.END)

        # Ask the user where to save the file
        file_path = fd.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

        # Save the file if a path was selected
        if file_path:
            with open(file_path, 'w') as file:
                file.write(content)
            print(f"File saved at {file_path}")

    def on_open_click(self):
        # Ask the user to select a file to open
        file_path = fd.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

        # Open and read the file if a path was selected
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.textbox.configure(state='normal')
                self.textbox.delete("1.0", tk.END)  # Clear existing content
                self.textbox.insert("1.0", content)  # Insert new content
                self.textbox.configure(state='disabled')
            print(f"File opened from {file_path}")


            lines = content.split('\n')
            print(lines)
            last_sentence =  lines[-1]
            words = last_sentence.split()
            if words:
                first_word = words[0]
                print(f"First word from the last sentence: {first_word}")
                self.linenumber = int(first_word[0: len(first_word) - 1]) + 1
                print(self.linenumber)
            

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

    #1. Unital -c "Category" ex: Mouse, keyboard, Smart_click, Record 
    #-a (agruments) -d (delay)

    def option_menu1_callback(self, choice):
        print("I pick: ", choice)
        self.open_input_dialog_event(choice)

    def open_input_dialog_event(self, choice):
        delay = "None"
        argument = "None"
        if choice == "Left Click":
            dialog = customtkinter.CTkInputDialog(text="Delay(ms):", title="Left Click")
            delay = dialog.get_input()

            if delay is None:
                return
            if not self.validate_number(delay):
                return

        elif choice == "Right Click":
            dialog = customtkinter.CTkInputDialog(text="Delay(ms):", title="Right Click")

            delay = dialog.get_input()
            if delay is None:
                return
            if not self.validate_number(delay):
                return

        elif choice == "Double Click":
            dialog = customtkinter.CTkInputDialog(text="Delay(ms):", title="Double Click")

            delay = dialog.get_input()
            if delay is None:
                return
            if not self.validate_number(delay):
                return

        elif choice == "Mouse Position":    
            dialog = MousePositionDialog(self)
            self.wait_window(dialog)  # Wait until the dialog is closed
            if hasattr(dialog, "argument"):
                argument = dialog.argument
                delay = dialog.delay
            else:
                return  # Return without inserting into the textbox if dialog didn't set argument and delay

        elif choice == "Scroll":
            
            dialog = MouseScrollDialog(self)
            self.wait_window(dialog)  # Wait until the dialog is closed
            if hasattr(dialog, "argument") and dialog.argument is not "None" and delay is not "None":
                argument = dialog.argument
                delay = dialog.delay
            else:
                return  # Return without inserting into the textbox if dialog didn't set argument and delay

        else:
            return


        self.textbox.configure(state='normal')
        self.textbox.insert(f"{self.linenumber}.0", str(self.linenumber) + ". Unital -c " + choice + " -a " + argument + " -d " + delay + "\n")  # Insert new content
        self.linenumber += 1
        self.textbox.configure(state='disabled')

    def validate_number(self, input_text):
        try:
            int(input_text)
            return True
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return False
    def alert_user_argument(self, alert):
        messagebox.showerror("Invalid Input", f"Please enter a valid number for {alert}")

        
