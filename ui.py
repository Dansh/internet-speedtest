from tkinter import *
import os
from PIL import ImageTk, Image  
from internet_speedtest import InternetSpeedTest
from threading import Thread

class Application:
    def __init__(self, master):
        self.speedtest = InternetSpeedTest()
        self.master = master
        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()
        master.geometry(f"{self.screen_width}x{self.screen_height}+-10+0")
        self.master.resizable(width=False ,height=False)
        master.title("Wifi Speed Test")
        self.master.iconbitmap('assets/icon.ico')
        self.load_page()


    def load_page(self):
        background_load = Image.open('assets/layer1_app.jpg')
        background_render = ImageTk.PhotoImage(background_load)
        self.background = Label(self.master, image=background_render)
        self.background.image = background_render
        self.background.place(x=0, y=0)
        self.wifi1_name_text = StringVar()
        self.wifi1_name_text.set("Loading Wifi...")
        self.wifi1_name = Label(self.master, textvariable=self.wifi1_name_text, font=("Arial", 77))
        self.wifi1_name.place(x=255, y=260)
        self.wifi1_downloadspeed_text = StringVar()
        self.wifi1_downloadspeed_text.set("Download:\nLoading...")
        self.wifi1_downloadspeed = Label(self.master, textvariable=self.wifi1_downloadspeed_text, font=("Arial", 55))
        self.wifi1_downloadspeed.place(x=315, y=400)
        self.wifi1_uploadspeed_text = StringVar()
        self.wifi1_uploadspeed_text.set("Upload:\nLoading...")
        self.wifi1_uploadspeed = Label(self.master, textvariable=self.wifi1_uploadspeed_text, font=("Arial", 55))
        self.wifi1_uploadspeed.place(x=315, y=580)
        self.wifi1_pingspeed_text = StringVar()
        self.wifi1_pingspeed_text.set("Ping:\nLoading...")
        self.wifi1_pingspeed = Label(self.master, textvariable=self.wifi1_pingspeed_text, font=("Arial", 55))
        self.wifi1_pingspeed.place(x=315, y=760)
        self.wifi2_name = Label(self.master, text="Wifi2 Name", font=("Arial", 77))
        self.wifi2_name.place(x=1120, y=260)
        self.wifi2_downloadspeed = Label(self.master, text="Download:\n128.34 Mbps", font=("Arial", 55))
        self.wifi2_downloadspeed.place(x=1180, y=400)
        self.wifi2_uploadspeed = Label(self.master, text="Upload:\n128.34 Mbps", font=("Arial", 55))
        self.wifi2_uploadspeed.place(x=1180, y=580)
        self.wifi2_pingspeed = Label(self.master, text="Ping:\n128.34 Mbps", font=("Arial", 55))
        self.wifi2_pingspeed.place(x=1180, y=760)
        update_network_thread = Thread(target=self.update_network)
        update_network_thread.start()
        
    def update_network(self):
        while True:
            internetspeed = self.speedtest.get_results()
            self.wifi1_downloadspeed_text.set(f"Download:\n{internetspeed['download']}")
            self.wifi1_uploadspeed_text.set(f"Upload:\n{internetspeed['upload']}")
            self.wifi1_pingspeed_text.set(f"Ping:\n{internetspeed['ping']}")
            self.wifi1_name_text.set(f"{internetspeed['wifiname']}")
            print("updated")
                

        
    

    

root = Tk()
app = Application(root)


root.mainloop()
