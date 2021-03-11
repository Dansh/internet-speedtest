from tkinter import *
import os

class Application:
    def __init__(self, master):
        self.master = master
        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()
        print(self.screen_width, self.screen_height)
        master.geometry(f"{self.screen_width}x{self.screen_height}+-10+0")
        master.title("Wifi Speed Test")
        self.master.iconbitmap('assets/icon.ico')
        self.load_page()


    def load_page(self):
        self.title = Label(self.master, text="Wifi Speed Test", font=("Arial", 34))
        self.title.pack(side="top", pady=50)
    


root = Tk()
app = Application(root)
root.mainloop()