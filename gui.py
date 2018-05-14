#!/usr/bin/env python      
import tkinter as tk   
from tkinter.font import Font
import chem as ch

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid()                       
        self.createWidgets()

    def createWidgets(self):
        label = tk.Label(self, text="Data file:")
        fileName = tk.Entry(self,width=20) 
        quitButton = tk.Button(self, text='Quit',
            command=self.quit) 
        runButton = tk.Button(self, text='Run',
            command=lambda: ch.chem_main(fileName.get()))
        label.grid(row=0, column=0)
        fileName.grid(row=0, column=1)       
        quitButton.grid(row=1, column=1)
        runButton.grid(row=1, column=0)        

app = Application()                       
app.master.title('Mabel')
app.mainloop()                           