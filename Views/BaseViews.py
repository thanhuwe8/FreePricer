import tkinter
import tkinter as tk
from tkinter import ttk

from abc import abstractmethod
from typing import List

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure



#? Used for MVC pattern
class View(tk.Frame):
    @abstractmethod
    def create_view():
        raise NotImplementedError



class LabelEntry(tk.Frame):
    def __init__(self, master, var, label,
                input_args=None, *args, **kwargs):
        
        super().__init__(master, *args, **kwargs)

        input_args = input_args or {}

        self.variable = var
        self.label = ttk.Label(self, text=label).grid(row=0,column=0,sticky=(tk.W + tk.E))
        self.input = ttk.Entry(self, **input_args).grid(row=1, column=0, sticky=(tk.W + tk.E))

        self.columnconfigure(0, weight=1)


class LabelRadioButton(tk.Frame):
    def __init__(self, master, var, label,
                input_args=None, *args, **kwargs):
        
        '''
        LabelInput(r_info, "Lab", input_class=ttk.Radiobutton,var=self._vars['Lab'], input_args={"values": ["A", "B", "C"]}).grid(row=1, column=0)
        '''
        
        super().__init__(master, **kwargs)
        
        input_args = input_args or {}
        
        self.variable = var
        
        for v in input_args.pop('values', []):
            button = ttk.Radiobutton(self, text=v, value=v, variable=self.variable,**input_args).pack(side=tk.TOP, ipadx=10, ipady=2, expand=True, fill='x')
        
        self.columnconfigure(0, weight=1)


class BaseView(View):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.labels = {}
        self.entries = {}
        self.buttons = {}
        self.comboboxes = {}
        self.dropdown = {}
        self.labelframe = {}
        self.treematrix = {}
        self.variables = {}
        self.labelvariables = {}
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)


    def CreateLabel(self,frame,name,text,label_text,row,column):
        self.labelframe[name] = tk.LabelFrame(frame,text=text,font=('Helvetica 10 bold'))
        self.labelframe[name].grid(row=row,column=column,padx=3,pady=3,sticky=tk.W+tk.E)
        self.labelframe[name].columnconfigure(0, weight=1)
        self.labelframe[name].rowconfigure(0, weight=1)
        
        self.labelvariables[name] = tk.StringVar()
        self.labelvariables[name].set(label_text)
        
        self.labels[name] = ttk.Label(self.labelframe[name], textvariable=self.labelvariables[name])
        self.labels[name].grid(row=0,column=0, sticky=tk.W+tk.E)
        self.labels[name].columnconfigure(0, weight=1)
        self.labels[name].rowconfigure(0, weight=1)

    
    
    def CreateEntry(self,frame,name,text,row,column,textvar, defaultvalue=20.0):
        self.labelframe[name] = tk.LabelFrame(frame,text=text,font=('Helvetica 10 bold'))
        self.labelframe[name].grid(row=row,column=column,padx=3,pady=3,sticky=tk.W+tk.E)
        self.labelframe[name].columnconfigure(0, weight=1)
        self.labelframe[name].rowconfigure(0, weight=1)
        
        self.entries[name] = tk.Entry(self.labelframe[name],textvariable=textvar)
        self.entries[name].delete(0, tk.END)
        self.entries[name].insert(0, str(defaultvalue))
        
        self.entries[name].grid(row=0,column=0,sticky=tk.W+tk.E)
        self.entries[name].columnconfigure(0, weight=1)
        self.entries[name].rowconfigure(0, weight=1)
    
    
    def CreateButton(self,frame,name,text,row,column):
        self.buttons[name] = tk.Button(frame,height=1,width=25)
        self.buttons[name]['text'] = text
        self.buttons[name].grid(row=row,column=column,padx=3,pady=3,sticky=tk.W+tk.E+tk.N)
        
    
    def CreateDropdown(self,frame,name,text,row,column,option_list):
        DropdownFrame = tk.LabelFrame(frame,text=text,font=('Helvetica 10 bold'))
        DropdownFrame.grid(row=row,column=column,padx=3,pady=3,sticky=tk.W+tk.E+tk.N)
        DropdownFrame.columnconfigure(0, weight=1)
        DropdownFrame.rowconfigure(0, weight=1)
        
        self.variables[name] = tk.StringVar()
        self.variables[name].set(option_list[0])
        self.dropdown[name] = tk.OptionMenu(DropdownFrame, self.variables[name], *option_list)
        self.dropdown[name].columnconfigure(0, weight=1)
        self.dropdown[name].rowconfigure(0, weight=1)
        self.dropdown[name].grid(row=0,column=0,padx=3,pady=3,sticky=tk.W+tk.E+tk.N)
        self.variables[name].set(text)
    
    
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


    def CreateMPLFrame(self, figure, name, text, row, column):
        self.labelframe[name] = tk.LabelFrame(master=self, text=text, font=('Helvetica 11 bold'))
        self.labelframe[name].columnconfigure(0, weight=1)
        self.labelframe[name].grid(row=row, column=column, sticky=tk.N + tk.S + tk.W + tk.E, padx=3, pady=3)
        
        canvas = FigureCanvasTkAgg(figure, self.labelframe[name])
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        toolbar = NavigationToolbar2Tk(canvas, self.labelframe[name])
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH,expand=1)

