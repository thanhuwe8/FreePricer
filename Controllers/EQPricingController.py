from PackagesSetup import *
from Views.EQPricingViews import *

from abc import ABC, abstractmethod
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as msg
from tkinter.ttk import Notebook
from tkinter import filedialog

from Controllers.BaseControllers import *

class BlackScholesController(Controller):
    
    def __init__(self, model, option_list) -> None:
        self.model = model
        self.view = None
        self.data = None
        self.option_list = option_list
        
    def bind(self,view=BaseView):
        self.view = view
        self.view.CreateBSView(option_list = self.option_list)
        self.view.buttons['CalculateBSPrice'].configure(command=self.ControllerCalculateBSprice)

    def ControllerCalculateBSprice(self):
        pass