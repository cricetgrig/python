from tkinter import *
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
import json
from myClass import myGraph

def selectFile():
    path = askopenfilename()
    filename.set(path)

G = myGraph()

def loadData():
    with open(filename.get(), 'r', encoding='utf-8') as file: 
        G.setData(json.load(file)) 
    combo['values'] = G.getNodes()
    combo.current(0)

def printTheBaconNumber(event):
    actor = combo.get()
    textOutput_label['text'] = G.getTheBaconNumber(actor)

window = Tk() 
window.geometry('800x200')
window.title("Число Бейкона")

selectButton = Button(window, width=15, text = "Выбрать файл", command = selectFile)
selectButton.grid(row=0, column=6, columnspan = 2)

loadButton = Button(window, width=15, text = "Загрузить", command = loadData)
loadButton.grid(row=0, column=8, columnspan = 1)

filename = StringVar()
EntryFilename = Entry(window, width=50, font='Arial 12', textvariable = filename)
EntryFilename.grid(row=0, column=0, columnspan = 5)

actorLabel = Label(window, text = "Актёр:", font = ("Arial", 12))
actorLabel.grid(row = 1, column = 0, columnspan = 1)

combo = Combobox(window, width = 50) 
combo.grid(row = 1, column = 1, columnspan = 5) 
combo.bind("<<ComboboxSelected>>", printTheBaconNumber)

textOutput_label = Label(window)
textOutput_label.grid(row = 3, column = 1, columnspan = 10)

window.mainloop()
