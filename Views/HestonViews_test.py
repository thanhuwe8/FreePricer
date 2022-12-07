import tkinter as tk
from tkinter import ttk

from datetime import datetime
from pathlib import Path


class BoundText(tk.Text):
    def __init__(self, *args, textvariable=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._variable = textvariable
        if self._variable:
            self.insert('1.0', self._variable.get())
            self._variable.trace_add('write', self._set_content)
            self.bind('<<Modified>>', self._set_var)

class 






variables = dict()
records_saved = 0

root = tk.Tk()
root.title('ABQ Data Entry Application')
root.columnconfigure(0, weight=1)


ttk.Label(
root, text="ABQ Data Entry Application",font=("TkDefaultFont", 16)
).grid()


drf = ttk.Frame(root)
drf.grid(padx=10, sticky=(tk.E + tk.W))
drf.columnconfigure(0, weight=1)


r_info = ttk.LabelFrame(drf, text='Record Information')
r_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    r_info.columnconfigure(i, weight=1)


variables['Date'] = tk.StringVar()
ttk.Label(r_info, text='Date').grid(row=0, column=0)
ttk.Entry(
r_info, textvariable=variables['Date']
).grid(row=1, column=0, sticky=(tk.W + tk.E))



time_values = ['8:00', '12:00', '16:00', '20:00']
variables['Time'] = tk.StringVar()
ttk.Label(r_info, text='Time').grid(row=0, column=1)
ttk.Combobox(r_info, textvariable=variables['Time'], values=time_values)).grid(row=1, column=1, sticky=(tk.W + tk.E))


variables['Lab'] = tk.StringVar()
ttk.Label(r_info text='Lab').grid(row=2, column=0)
labframe = ttk.Frame(r_info)
for lab in ('A', 'B', 'C'):
    ttk.Radiobutton(
    labframe, value=lab, text=lab, variable=variables['Lab']).pack(side=tk.LEFT, expand=True)
    labframe.grid(row=3, column=0, sticky=(tk.W + tk.E))


import json


class JSONVar(tk.StringVar):
    def __init__(self, *args, **kwargs):
        kwargs['value'] = json.dumps(kwargs.get('value'))
        super().__init__(*args, **kwargs)
    
    def set(self, value, *args, **kwargs):
        string = json.dumps(value)
        super().set(string, *args, **kwargs)
    
    def get(self, *args, **kwargs):
        string = super().get(*args, **kwargs)
        return(json.loads(string))


root = tk.Tk()
var1 = JSONVar(root)
var1.set([1, 2, 3])
var2 = JSONVar(root, value={'a': 10, 'b': 15})
var2.get()



class LabelInput(tk.Frame):
    def __init__(self, parent, label, inp_cls, inp_args, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = tk.Label(self, text=label, anchor='w')
        self.input = inp_cls(self, **inp_args)
        
        self.columnconfigure(1, weight=1)
        self.label.grid(sticky=tk.E + tk.W)
        self.input.grid(row=0, column=1, sticky=tk.E + tk.W)
        
        
root = tk.Tk()
li1 = LabelInput(root, 'Name', tk.Entry, {'bg': 'red'})
li1.grid()


age_var = tk.IntVar(root, value=21)
li2 = LabelInput(root, 'Age', tk.Spinbox, {'textvariable': age_var, 'from_': 10, 'to': 150})
li2.grid()


class MyForm(tk.Frame):
    def __init__(self, parent, data_var, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.data_var = data_var
        self._vars = {
            'name':tk.StringVar(self),
            'age':tk.IntVar(self, value=2)
            
        }
        self.frame1= LabelInput(self,'Name',tk.Entry,{'textvariable': self._vars['name']}).grid(sticky=tk.E + tk.W)
        self.frame2= LabelInput(self,'Age',tk.Spinbox,{'textvariable': self._vars['age'], 'from_': 10, 'to': 150}).grid(sticky=tk.E + tk.W)
        self.button1 = tk.Button(self, text='Submit', command=self._on_submit).grid()
        
        def _on_submit(self):
            data = { key: var.get() for key, var in self._vars.items() }
            self.data_var.set(data)
            

