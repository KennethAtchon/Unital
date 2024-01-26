import tkinter
import customtkinter
from tkinter import filedialog
from documents.convert_frame import ConvertFrame
from documents.wordoperations import TextOperationsFrame
from documents.filter import FilterFrame
from documents.unique import UniqueFrame

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Unital")
        self.geometry(f"{1100}x{580}")

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
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Setting", command=self.sidebar_button_event)
        self.sidebar_button_4.grid(row=7, column=0, padx=20, pady=20)

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

        


    def forget_all(self):
        # Hide all frames
        self.convertframe.grid_forget()
        self.tabviewframe.grid_forget()
        self.filterframe.grid_forget()
        self.uniqueframe.grid_forget()

    def show_documents_page(self):
        self.forget_all()

        self.convertframe.grid(row=0, column=1, padx=(20, 0), pady=(0,10), sticky="nsew")
        self.tabviewframe.grid(row=0, column=2, padx=(20, 20),pady=(0,10), sticky="nsew")
        self.filterframe.grid(row=1, column=1, padx=(20, 0), pady=(0,10), sticky="nsew")
        self.uniqueframe.grid(row=1, column=2, padx=(20, 20), pady=(0,10), sticky="nsew")

    def show_automation_page(self):
        self.forget_all()

        
    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":

    app = App()
    app.mainloop()