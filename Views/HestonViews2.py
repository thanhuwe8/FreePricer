"""Demonstration of using classes with tkinter"""
import tkinter as tk
import json


#############################
# Improving Tkinter classes #
#############################

# Create a JSONVar

class JSONVar(tk.StringVar):
  """A Tk variable that can hold dicts and lists"""

  def __init__(self, *args, **kwargs):
    kwargs['value'] = json.dumps(kwargs.get('value'))
    super().__init__(*args, **kwargs)

  def set(self, value, *args, **kwargs):
    string = json.dumps(value)
    super().set(string, *args, **kwargs)

  def get(self, *args, **kwargs):
    """Get the list or dict value"""
    string = super().get(*args, **kwargs)
    return json.loads(string)


# Uncomment to try it, but comment this code before sub-classing Tk
#root = tk.Tk()
#var1 = JSONVar(root)
#var1.set([1, 2, 3, 4, 5])
#
#var2 = JSONVar(root, value={'a': 10, 'b': 15})
#print("Var1: ", var1.get()[1])
#print("Var2: ", var2.get()['b'])
#root.mainloop()
#exit()

#############################
# Creating compound widgets #
#############################

class LabelInput(tk.Frame):
  """A label and input combined together"""

  def __init__(
    self, parent, label, inp_cls,
    inp_args, *args, **kwargs
   ):
    super().__init__(parent, *args, **kwargs)
    self.label = tk.Label(self, text=label, anchor='w')
    self.input = inp_cls(self, **inp_args)

    # side-by-side layout
    self.columnconfigure(1, weight=1)
    self.label.grid(sticky=tk.E + tk.W)
    self.input.grid(row=0, column=1, sticky=tk.E + tk.W)



class MyForm(tk.Frame):

  def __init__(self, parent, data_var, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    self.data_var = data_var
    self._vars = {
      'name': tk.StringVar(),
      'age': tk.IntVar(value=2)
    }
    
    LabelInput(
      self,
      'Name',
      tk.Entry,
      {'textvariable': self._vars['name']}
    ).grid(sticky=tk.E + tk.W)
    
    LabelInput(
      self,
      'Age',
      tk.Spinbox,
      {'textvariable': self._vars['age'], 'from_': 10, 'to': 150}
    ).grid(sticky=tk.E + tk.W)
    
    tk.Button(self, text='Submit', command=self._on_submit).grid()

  def _on_submit(self):
    data = { key: var.get() for key, var in self._vars.items() }
    self.data_var.set(data)


# We can even subclass Tk

class Application(tk.Tk):
  """A simple form application"""

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.jsonvar = JSONVar()
    self.output_var = tk.StringVar()
    tk.Label(self, text='Please fill the form').grid(sticky='ew')
    MyForm(self, self.jsonvar).grid(sticky='nsew')
    tk.Label(self, textvariable=self.output_var).grid(sticky='ew')
    self.columnconfigure(0, weight=1)
    self.rowconfigure(1, weight=1)

    self.jsonvar.trace_add('write', self._on_data_change)

  def _on_data_change(self, *args, **kwargs):
    data = self.jsonvar.get()
    output = ''.join([
        f'{key} = {value}\n'
        for key, value in data.items()
    ])
    self.output_var.set(output)

#root.mainloop()
if __name__ == '__main__':
  app = Application()
  app.mainloop()




from PackagesSetup import *
from Views.BasicViews import *

import tkinter
import tkinter as tk
from tkinter import ttk

from abc import abstractmethod
from typing import List


class InputLabel(tk.Frame):
    #! functional programming
    def __init__(self, master, label, var, input_class = ttk.Entry, 
                inp_args=None, label_args=None, **kwargs):
        super().__init__(master, **kwargs)
        
        input_args = input_args or {}
        label_args = label_args or {}
        
        self.variable = var
        self.variable.label_widget = self
        
        if input_class in (ttk.Checkbutton, ttk.Button):
            input_args['text'] = label
        else:
            self.label = ttk.Label(self, text=label, **label_args)
            self.label.grid(row=0, column=0, sticky=(tk.W + tk.E))
        
        if input_class in (ttk.Checkbutton, ttk.Button, ttk.Radiobutton):
            input_args["variable"] = self.variable
        else:
            input_args["textvariable"] = self.variable
        
        # Setup the input
        if input_class == ttk.Radiobutton:
            # for Radiobutton, create one input per value
            self.input = tk.Frame(self)
            for v in input_args.pop('values', []):
                button = ttk.Radiobutton(self.input, value=v, text=v, **input_args)
                button.pack(side=tk.LEFT, ipadx=10, ipady=2, expand=True, fill='x')
        else:
            self.input = input_class(self, **input_args)

        self.input.grid(row=1, column=0, sticky=(tk.W + tk.E))
        self.columnconfigure(0, weight=1)

    def grid(self, sticky=(tk.E + tk.W), **kwargs):
        """Override grid to add default sticky values"""
        super().grid(sticky=sticky, **kwargs)
    
    
        


class BoundText(tk.Text):
    def __init__(self,*args, textvariable=None,**kwargs):
        super().__init__(*args, **kwargs)
        self._variable = textvariable
        if self._variable:
            self.insert('1.0', self._variable.get())
            self._variable.trace_add('write', self._set_content)
            self.bind('<<Modified>>', self._set_var)


    def _set_content(self, *_):
        self.delete('1.0', tk.END)
        self.insert('1.0', self._variable.get())
        
    
    def _set_var(self, *_):
        if self.edit_modified():
            content = self.get('1.0', 'end-1chars')
            self._variable.set(content)
            self.edit_modified(False)
    
    


class HestonView(View):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.variables = {}
        
        

