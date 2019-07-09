from tkinter import *
from tkinter import filedialog
# import re


def texteditor():

    class Window(Frame):

        def save(self):
            self.input = self.text.get("1.0", END)
            with open("Custom_functions.py", "w") as f:
                f.write(self.input)
            print("saved")

        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master

            self.master.title("Custom_functions.py")
            self.pack(fill=BOTH, expand=1)

            menu = Menu(top)
            top.config(menu=menu)
            self.file_menu = Menu(menu)
            menu.add_cascade(label="File", menu=self.file_menu)
            # self.file_menu.add_command(label="New")
            # self.file_menu.add_command(label="Open", command=self.open_file_function)

            self.text = Text(top, height=200, width=200)  # Use Text widget insted of Listbox
            self.text.pack(side=LEFT, fill=Y, expand=True)

            self.scrollbar = Scrollbar(top, orient="vertical")
            self.scrollbar.config(command=self.text.yview)
            self.scrollbar.pack(side=RIGHT, fill=Y, expand=True)

            # change all occurances of self.listNodes to self.text
            self.text.config(yscrollcommand=self.scrollbar.set)

        # def open_file_function(self):

            # self.file_save = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"), ("All files", "*.*")))
            with open("Custom_functions.py", "r") as file:
                print(1)
                for i in file.readlines():
                    print(3456)
                    self.text.insert(END, i)

            self.file_menu.add_command(label="Save", command=lambda: self.save())
            self.file_menu.add_separator()
            self.file_menu.add_command(label="Exit")

    top = Tk()
    top.geometry("1000x1000")
    ap = Window(top)
    ap.mainloop()
