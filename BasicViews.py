from PackagesSetup import *

import tkinter
import tkinter as tk
from tkinter import ttk

from abc import abstractmethod
from typing import List


class View(tk.Frame):
    @abstractmethod
    def create_view():
        raise NotImplementedError
    


class Form(View):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.entries = {}
        self.buttons = {}
        self.comboboxes = {}
        self.dropdown = {}
        self.labelframe = {}
        self.treematrix = {}
        self.variables = {}
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0)
    
    
    def CreateEntry(self,frame,name,text,row,column,textvar):
        Label_Frame = tk.LabelFrame(frame,text=text,font=('Helvetica 10 bold'))
        self.entries[name] = tk.Entry(Label_Frame,textvariable=textvar)
        self.entries[name].grid(row=1,column=1)
        Label_Frame.grid(row=row,column=column,padx=3,pady=3,sticky=tk.W)
    
    
    def CreateButton(self,frame,name,text,row,column):
        self.buttons[name] = tk.Button(frame,height=1,width=35)
        self.buttons[name]['text'] = text
        self.buttons[name].grid(row=row,column=column,padx=3,pady=3,sticky=tk.W)
        
    
    def CreateDropdown(self,frame,name,text,row,column,option_list):
        self.variables[name] = tk.StringVar()
        self.dropdown[name] = tk.OptionMenu(frame, self.variables[name], *option_list)
        
        self.variables[name].set(text)
        self.dropdown[name].grid(row=row,column=column,padx=3,pady=3,sticky=tk.W)
    
    
    def CreateTreeView(self, input_data, row, column,name, text):
        
        self.labelframe[name] = tk.LabelFrame(master=self, text=text)
        self.labelframe[name].columnconfigure(0, weight=1)
        self.labelframe[name].grid(row=row,column=column,stick=tk.N+tk.W,columnspan=2,padx=3,pady=3)
        
        header = input_data.columns.tolist()
        self.treematrix[name] = ttk.Treeview(self.labelframe[name],
                                            columns=header,height=15,
                                            selectmode='browse',
                                            style='mystyle.Treeview')
        self.treematrix[name]['show'] = 'headings'
        
        for row_data in input_data.itertuples(index=False):
            self.treematrix[name].insert('', tk.END, values=row_data)
        
        self.treematrix[name].grid(row=0,column=0,columnspan=2,sticky='W')


    def CreateBSView(self, option_list, main_text='MC generator'):
        control_frame = tk.LabelFrame(master=self, text=main_text, font=('Helvetica 11 bold'))
        control_frame.rowconfigure(0,weight=1)
        control_frame.columnconfigure(0,weight=1)
        control_frame.grid(row=1,column=0,sticky=tk.NW,padx=3,pady=3)
        
        self.CreateDropdown(control_frame,name='Optiontype', text='Test',row=1,column=1,option_list=option_list)
        
        self.CreateEntry(control_frame,name='S',text='StockPrice',row=2,column=1,textvar=tk.DoubleVar())
        
        for key in self.entries:
            self.entries[key].delete(0, tk.END)
        
