#!/usr/bin/env python      
import Tkinter as tk   
from tkFont import Font
import chem as ch

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid()                       
        self.createWidgets()

    def createWidgets(self):
        label = tk.Label(self, text="Data file:")
        fileName = tk.Entry(self,width=20) 
        status = tk.Label(self, text="Ready")
        quitButton = tk.Button(self, text='Quit',
            command=self.quit) 
        runButton = tk.Button(self, text='Run',
            command=lambda: (
                status.config(text="Running..."),
                self.update_idletasks(),
                ch.chem_main(fileName.get()),
                status.config(text="Done")
                ))
        label.grid(row=0, column=0)
        fileName.grid(row=0, column=1)   
        status.grid(row=1)    
        quitButton.grid(row=2, column=1)
        runButton.grid(row=2, column=0)        

app = Application()                       
app.master.title('Mabel')
app.mainloop()                           