import tkinter
import customtkinter
from tkinter import filedialog
from documents.convert_frame import ConvertFrame
from documents.wordoperations import TextOperationsFrame
from documents.filter import FilterFrame
from documents.unique import UniqueFrame
from automation.automation import AutomationFrame


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.nltk_installed = False  

        # configure window
        self.title("Unital")
        self.geometry(f"{1100}x{580}")

        self.settings_window = None

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((1), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Unital", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Documents", command=self.show_documents_page)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Automation", command=self.show_automation_page)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Trading", command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.settings_button = customtkinter.CTkButton(
            self.sidebar_frame, text="Settings", command=self.open_settings_window
        )
        self.settings_button.grid(row=7, column=0, padx=20, pady=20)

        # Convert docx to pdf 
        self.convertframe = ConvertFrame(self)
        self.convertframe.grid(row=0, column=1, padx=(20, 0), pady=(0,10), sticky="nsew")

        # Text operations
        self.tabviewframe = TextOperationsFrame(self)
        self.tabviewframe.grid(row=0, column=2, padx=(20, 20),pady=(0,10), sticky="nsew")
        
        # Filter operations
        self.filterframe = FilterFrame(self)
        self.filterframe.grid(row=1, column=1, padx=(20, 0), pady=(0,10), sticky="nsew")

        self.uniqueframe = UniqueFrame(self)
        self.uniqueframe.grid(row=1, column=2, padx=(20, 20), pady=(0,10), sticky="nsew")

        # Automation
        self.automationframe = AutomationFrame(self)
        


    def forget_all(self):
        # Hide all frames
        self.convertframe.grid_forget()
        self.tabviewframe.grid_forget()
        self.filterframe.grid_forget()
        self.uniqueframe.grid_forget()
        self.automationframe.grid_forget()

    def show_documents_page(self):
        self.forget_all()

        self.convertframe.grid(row=0, column=1, padx=(20, 0), pady=(0,10), sticky="nsew")
        self.tabviewframe.grid(row=0, column=2, padx=(20, 20),pady=(0,10), sticky="nsew")
        self.filterframe.grid(row=1, column=1, padx=(20, 0), pady=(0,10), sticky="nsew")
        self.uniqueframe.grid(row=1, column=2, padx=(20, 20), pady=(0,10), sticky="nsew")

    def show_automation_page(self):
        self.forget_all()
        self.automationframe.grid(row=0, column=1, rowspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        
    def sidebar_button_event(self):
        print("sidebar_button click")

    def open_settings_window(self):
        if not self.settings_window or not self.settings_window.winfo_exists():
            self.settings_window = SettingsWindow(self)
        self.settings_window.lift()  # Brings the SettingsWindow to the top
        self.settings_window.focus_force()  # Forces focus on the SettingsWindow

    def update_nltk_installed(self, installed):
        self.nltk_installed = installed
        # Here, pass the updated value to the UniqueFrame instance
        self.uniqueframe.update_nltk_status(installed)

class SettingsWindow(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Settings")
        self.geometry("400x300")
        self.configure(bg='grey')

        self.parent = parent 

        # Set the window to be always on top
        self.attributes('-topmost', True)
        self.after(500, lambda: self.attributes('-topmost', False))  # 
        
        
        self.settings_frame = customtkinter.CTkFrame(self)
        self.settings_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Theme selector option
        self.theme_selector_label = customtkinter.CTkLabel(self.settings_frame, text="Select theme:")
        self.theme_selector_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        theme_selector = customtkinter.CTkOptionMenu(
            self.settings_frame, values=["Light", "Dark", "System"], command=self.change_theme
        )
        theme_selector.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Install NLTK option with a switch
        self.nltk_label = customtkinter.CTkLabel(self.settings_frame, text="Install NLTK:")
        self.nltk_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.nltk_switch = customtkinter.CTkSwitch(self.settings_frame, text="", command=self.toggle_nltk)
        self.nltk_switch.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    def change_theme(self, theme):
        customtkinter.set_appearance_mode(theme)

    def toggle_nltk(self):
        nltk_status = self.nltk_switch.get()
        if nltk_status == 0:
            nltk_status = False
        else:
            nltk_status = True
        self.parent.update_nltk_installed(nltk_status)


if __name__ == "__main__":

    app = App()
    app.mainloop()