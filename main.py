try:
    import tkinter as tk
    import sys
    from tkinter import simpledialog
    from tkinter import filedialog
    from tkinter import messagebox
    import os
    from ball_tracker_core import run, Dist_between_two_points, write_to_csv_file
    from plotter import Dataset
    import collections
    from writter import *
    from inspect import getmembers, isfunction
except ImportError as e:
    root = tk.Tk()
    root.title("Ball Tracker V1.1 2019 Séverin FERARD")
    label = tk.Label(root,
                     text="""Oops, it seems like you need to install some modules. Everything is gonna be alright don't worry, Severin got you.\n\n Just copy and past the following command to your Bash: \npip3 install opencv-contrib-python pandas easygui matplotlib collections\n\n\n\n Dont forget, Severin loves you <3\n\n\n{}""".format(e),
                     font='Helvetica 15 bold')
    label.pack(side="top", fill="both", expand=True, padx=100, pady=100)
    button = tk.Button(root, text="Got it thanks!", command=lambda: root.destroy())
    button.pack(side="bottom", fill="none", expand=True)
    root.mainloop()
    sys.exit()

height = 3
global parameters
parameters = {}

global positions
positions = {}
global dicdistorigin
dicdistorigin = {}
global dicdistrelative
dicdistrelative = {}
global is_saved
is_saved = True
global data
data = []


def donothing():
    print('nothing')
    pass


def commandrun():
    print("RUN\n")
    messagebox.showinfo("Info", "To select a ball to track, trace a rectangle over it with your mouse, then press Enter. If you want to select another ball, press any keyboard key and repeat. When you are done selecting, press Enter and Q ")
    global data
    data = []
    data = run(parameters["Circle"],
               parameters["Max Label"],
               parameters["Current Label"],
               parameters["Frame count"],
               parameters["Drift warning"],
               parameters["Treshold"],
               parameters["Path"],
               parameters["acquisitiontimesb"],
               parameters["videopath"])
    global is_saved
    is_saved = False
    print("is_saved", is_saved)
    availabledata()
    print(data)
    return()


def New():
    print("len", len(datamenu.winfo_children()))
    datamenu.delete(0, len(datamenu.winfo_children()))
    datamenu.add_command(label="No data available")
    # parameters["Circle"] = True
    # parameters["Max Label"] = False
    # parameters["Current Label"] = True
    # parameters["Frame count"] = True
    # parameters["Drift warning"] = True
    # parameters["Treshold"] = 40
    # parameters["Path"] = True
    # parameters["acquisitiontimesb"] = 10
    # parameters["videopath"] = -1


def helpthing():
    messagebox.showinfo("Help", "Ask your mom !\n\nIf you can't find your momma in a 30 feet permimeter, just ask Severin.\nYou'r welcome!\n\n Oh and don't forget; Severin loves you <3")
def about():
    messagebox.showinfo("About/Licence",'''About", "Program created by Severin FERARD between 5/28/19 and 6/03/19\n\n

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.''')

def askclose():
    print("askclose", is_saved)
    if is_saved == True:
        root.destroy()
        sys.exit()

    else:
        if messagebox.askyesno("Save beafore closing", "The last measurment has not been saved, close without saving ?"):
            root.destroy()
            print("delete")
            sys.exit()
        else:
            return()


def openfile():
    parameters["videopath"] = root.filename = filedialog.askopenfilename(initialdir="/", title="Select file")
    if not parameters["videopath"]:
        filenamesb.config(text="File: No file selected")
    else:
        string = parameters["videopath"].split("/")
        filenamesb.config(text="File :" + string[-1])
    print("openfile", parameters)
    return()


def savefile():
    parameters["savepath"] = root.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file")
    if not parameters["savepath"]:
        savefilenamesb.config(text="Save file: No file selected")
    else:
        string = parameters["savepath"].split("/")
        savefilenamesb.config(text="Save file :" + string[-1])
    print("savefile", parameters)
    return()


def save():
    try:
        file = parameters["savepath"]
    except KeyError:
        print("no savefile selected, selecting...")
        savefile()

    file = parameters["savepath"]
    if file == '':
        return()
    write_to_csv_file(data[0], data[1], data[2], file)
    global is_saved
    is_saved = True
    print("is_saved", is_saved)
    return()


def exit():
    global root
    root.destroy()


def askacquisitiontime():
    user_input = simpledialog.askstring("Acquisition time", "Enter an acquisition time in frames")
    parameters["acquisitiontimesb"] = int(user_input)
    acquisitiontimesb.config(text="Acquisition time (frames): \n{}".format(parameters["acquisitiontimesb"]))
    acquisitiontimesb.pack()
    print("Aquisition time menue", parameters)
    return()


def asktreshold():
    user_input = simpledialog.askstring("Treshold", "Enter the value of the drift warning treshold")
    parameters["Treshold"] = int(user_input)
    tresholdsb.config(text="Drif warning treshold \n{}".format(parameters["Treshold"]))
    tresholdsb.pack()
    print("Treshold", parameters)
    return()


widthroot = 1600
heightroot = 900
test = widthroot - 300
print(test)
root = tk.Tk()
root.title("Ball Tracker V2")
root.configure(background='grey')
root.geometry(f"{widthroot}x{heightroot}")

sidebar = tk.Frame(width=heightroot * 0.3, height=heightroot, bg="white")
sidebar.pack(side=tk.RIGHT)
sidebar.pack_propagate(False)

sidebar.update()


menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=New)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save to ..", command=savefile)
filemenu.add_command(label="Close", command=askclose)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=askclose)
menubar.add_cascade(label="File", menu=filemenu)

settingsmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Settings", menu=settingsmenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help window", command=helpthing)
helpmenu.add_command(label="About/Licence...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)


class sidebarlabel:

    def callback(self, name):
        if parameters[name]:
            self.name.config(bg="white")
            parameters[name] = False
        else:
            parameters[name] = True
            self.name.config(bg="blue")
        print(parameters)

        # print(name)

    def __init__(self, name, height, default):
        self.name = tk.Label(sidebar, text=name, bg="blue", fg="black", relief="sunken")
        self.name.config(font=("Arial", 18))
        self.name.pack(fill=tk.X)
        settingsmenu.add_command(label=name, command=lambda: self.callback(name))
        parameters[name] = default


circlesb = sidebarlabel("Circle", height, True)
currentlabelsb = sidebarlabel("Current Label", height, True)
maxlabelsb = sidebarlabel("Max Label", height, True)
pathsb = sidebarlabel("Path", height, True)
framecountsb = sidebarlabel("Frame count", height, True)
driftwarningsb = sidebarlabel("Drift warning", height, True)

parameters["Treshold"] = 40
tresholdsb = tk.Label(sidebar, text="Drift warning treshold: \n{}".format(parameters["Treshold"]), bg="white", fg="black", height=height, relief="sunken")
tresholdsb.pack(fill=tk.X)
settingsmenu.add_command(label="Drift warning treshold", command=asktreshold)

filenamesb = tk.Label(sidebar, text="File: No file selected", bg="white", fg="black", height=int(height / 3), relief="sunken")
filenamesb.pack(fill=tk.X)

savefilenamesb = tk.Label(sidebar, text="Save file: No file selected", bg="white", fg="black", height=int(height / 3), relief="sunken")
savefilenamesb.pack(fill=tk.X)


parameters["acquisitiontimesb"] = 10
acquisitiontimesb = tk.Label(sidebar, text="Acquisition time (frames): \n{}".format(parameters["acquisitiontimesb"]), bg="white", fg="black", height=height, relief="sunken")
acquisitiontimesb.pack(fill=tk.X)
settingsmenu.add_command(label="Acquisition time", command=askacquisitiontime)

try:
    a = parameters["videopath"]
except KeyError:
    parameters["videopath"] = -1

startbutton = tk.Button(sidebar, text="START", bg="white", fg="black", relief="sunken", command=commandrun)
startbutton.pack(fill=tk.X)


dicdataset = {}


# testbutton = tk.Button(sidebar, text="print dic", bg="white", fg="black", relief="sunken", command=testdic)
# startbutton.pack(fill=tk.X)


datamenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Data", menu=datamenu)
datamenu.add_command(label="No data available", command=lambda: print('no data'))
datamenu.add_command(label="Edit custom functions", command=texteditor)
# datatest = Dataset(tk, root, "datatest", datamenu, dicdataset, [], [], [])
# testdata =


def availabledata():
    try:
        global data
        n_dataset = len(data[0])
        try:
            datamenu.delete("No data available")
        except:
            pass
        # datamenu.delete("No data available")
        global datasets
        datasets = [Dataset(tk, root, "dataset {}".format(i), datamenu, dicdataset, data[0][i], data[1][i], data[2][i]) for i in range(n_dataset)]
    except Exception as e:
        print(e)
        datamenu.add_command(label="No data available", command=lambda: print('no data'))
        print("error")
        print(data)


def New():
    for dataset in datasets:
        print(dataset)


root.protocol("WM_DELETE_WINDOW", askclose)

root.config(menu=menubar)
root.mainloop()
