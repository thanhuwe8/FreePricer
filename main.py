from PackagesSetup import *

from Views.EQPricingViews import *
from Controllers.EQPricingController import *
from Models.Analytical.BlackScholes import *

import tkinter as tk
from tkinter import *

# import ctypes
# ctypes.windll.shcore.GetProcessDpiAwareness(1)


class Application(ttk.Notebook):
    def __init__(self, master=None):
        super().__init__(master)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid(row=0,column=0,sticky=tk.E+tk.W+tk.N+tk.S)
    
    #? use functional programming as part of parameters
    def new_tab(self,controller,view,name):
        view = view(self)
        controller.bind(view)
        self.add(view,text=name)


if __name__=="__main__":
    
    root = tk.Tk()
    
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    app = Application(master=root)
    
    BSmodel = BlackScholes()
    BSController = BlackScholesController(model=BlackScholes(), option_list=['EUROPEAN_CALL', 'EUROPEAN_PUT'])
    app.new_tab(controller=BSController, view=BaseView, name='BS calculator')
    
    root.mainloop()