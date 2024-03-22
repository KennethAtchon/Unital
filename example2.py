import tkinter as tk
from tkinter import simpledialog

class CustomIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom IDE")

        # Creating a frame for text area and line numbers
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True, fill=tk.BOTH)

        # Line number bar
        self.line_number_bar = tk.Text(self.frame, width=4, padx=3, takefocus=0, border=0,
                                       background='lightgrey', state='disabled', wrap='none')
        self.line_number_bar.pack(side=tk.LEFT, fill=tk.Y)

        # Create text area
        self.text_area = tk.Text(self.frame, wrap="word")
        self.text_area.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        self.text_area.bind("<KeyPress>", self.on_key_press)
        self.text_area.bind("<Return>", self.on_return_key)

        self.update_line_numbers()

    def on_key_press(self, event):
        self.update_line_numbers()

    def on_return_key(self, event):
        # Insert a newline at the cursor's current position
        self.text_area.insert(tk.INSERT, "\n")
        self.update_line_numbers()
        return "break"  # Prevent the default Return key behavior

    def update_line_numbers(self):
        self.line_number_bar.config(state='normal')
        self.line_number_bar.delete(1.0, tk.END)
        line_count = int(self.text_area.index('end-1c').split('.')[0])
        line_number_content = "\n".join(str(i) for i in range(1, line_count + 1))
        self.line_number_bar.insert(1.0, line_number_content)
        self.line_number_bar.config(state='disabled')

root = tk.Tk()
app = CustomIDE(root)
root.mainloop()
