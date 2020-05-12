import tkinter as tk
from db import DatabaseOperator

#example query
#db_sendiri = DatabaseOperator()
#db_sendiri.get_all_data("pasien")


class MainApplication(tk.Frame):
    def __init__(self, master=None, width=500, height=500):
        super().__init__(master,width=width,height=height,borderwidth=5)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
        command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = MainApplication(
        root,
        width = 500,
        height = 500
    )

app.mainloop()
