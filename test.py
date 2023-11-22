import tkinter as tk
import customtkinter
import docx2pdf
from gtts import gTTS

customtkinter.set_appearance_mode("Dark")

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Unital")
        self.geometry("1100x580")
        self.grid_columnconfigure(1, weight=1)

        # Sidebar (same as before)
        self.sidebar = customtkinter.CTkFrame(self, width=140)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")

        # ... sidebar button creation omitted for brevity ...

        # Text operations frame and widgets
        self.text_op_frame = customtkinter.CTkFrame(self)
        self.op_label = customtkinter.CTkLabel(self.text_op_frame, text="Text Operations", font=customtkinter.CTkFont(size=14, weight="bold"))

        self.op_textbox = customtkinter.CTkTextbox(self.text_op_frame, height=10)

        self.checkboxes = []
        self.checkbox_vars = [tk.IntVar() for _ in range(3)]

        for i, (text, var) in enumerate(zip(["Word Count", "Reverse Text", "Text to Speech"], self.checkbox_vars)):
            cb = customtkinter.CTkCheckBox(self.text_op_frame, text=text, variable=var)
            cb.grid(row=i+1, column=1, sticky="w")
            self.checkboxes.append(cb)

        self.op_submit = customtkinter.CTkButton(self.text_op_frame, text="Process Text", command=self.handle_text_ops)

        # Initially hidden
        self.text_op_frame.grid_remove()

    def show_documents_page(self):
        # Previous doc conversion...
        # ...

        # Show text ops frame
        self.text_op_frame.grid(row=0, column=1, sticky="nsew")
        self.op_label.grid(row=0, column=0, padx=20, pady=20)
        self.op_textbox.grid(row=1, column=0, padx=20, pady=20)
        self.op_submit.grid(row=4, column=0, padx=20, pady=20)

    def handle_text_ops(self):
        user_text = self.op_textbox.get("1.0", "end-1c")

        output = []
        if self.checkbox_vars[0].get():
            output.append(f"Word Count: {len(user_text.split())}")

        if self.checkbox_vars[1].get():
            output.append(f"Reversed: {user_text[::-1]}")

        if self.checkbox_vars[2].get():
            # Assumption: gtts is installed
            tts = gTTS(text=user_text, lang="en")
            filename = "output_speech.mp3"
            tts.save(filename)
            output.append(f"Speech saved to: {filename}")

        if output:
            self.show_message("\n".join(output))
        else:
            self.show_message("Please select at least one operation.")

    def show_message(self, message):
        customtkinter.CTkMessageBox.show_info(title="Results", message=message)

if __name__ == "__main__":
    app = App()
    app.mainloop()


            # # Text operations frame and widgets
        # self.text_op_frame = customtkinter.CTkFrame(self)
        # self.op_label = customtkinter.CTkLabel(self.text_op_frame, text="Text Operations", font=customtkinter.CTkFont(size=14, weight="bold"))

        # self.op_textbox = customtkinter.CTkTextbox(self.text_op_frame, height=10)

        # self.checkboxes = []
        # self.checkbox_vars = [tk.IntVar() for _ in range(3)]

        # for i, (text, var) in enumerate(zip(["Word Count", "Reverse Text", "Text to Speech"], self.checkbox_vars)):
        #     cb = customtkinter.CTkCheckBox(self.text_op_frame, text=text, variable=var)
        #     cb.grid(row=i+1, column=1, sticky="w")
        #     self.checkboxes.append(cb)

        # self.op_submit = customtkinter.CTkButton(self.text_op_frame, text="Process Text", command=self.handle_text_ops)

        # # Initially hidden
        # self.text_op_frame.grid_remove()\



            # def handle_text_ops(self):
    #     user_text = self.op_textbox.get("1.0", "end-1c")

    #     output = []
    #     if self.checkbox_vars[0].get():
    #         output.append(f"Word Count: {len(user_text.split())}")

    #     if self.checkbox_vars[1].get():
    #         output.append(f"Reversed: {user_text[::-1]}")

    #     if self.checkbox_vars[2].get():
    #         # Assumption: gtts is installed
    #         tts = gTTS(text=user_text, lang="en")
    #         filename = "output_speech.mp3"
    #         tts.save(filename)
    #         output.append(f"Speech saved to: {filename}")

    #     if output:
    #         print("\n".join(output))
    #     else:
    #         print("Please select at least one operation.")

    