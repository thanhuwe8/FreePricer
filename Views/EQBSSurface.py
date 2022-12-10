from PackagesSetup import *
from Views.BaseViews import *

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


class EQBSSurface(BaseView):
    def __init__(self, master=None):
        super().__init__(master)
    
    def create_view(self, option_list, main_text='BS pricing surface'):
        control_frame = tk.LabelFrame(master=self, text=main_text, font=('Helvetica 11 bold'))
        control_frame.grid(row=0,column=0,sticky=tk.W+tk.E+tk.N+tk.S,padx=3,pady=3)
        
        
        for i in range(1,8):
            control_frame.rowconfigure(i,weight=1)
        for i in range(1,4):
            control_frame.columnconfigure(i,weight=1)
        
        
        self.CreateDropdown(control_frame,name='Optiontype', text='Test',row=0,column=0,option_list=option_list)
        self.CreateEntry(control_frame,name='S',text='StockPrice',row=1,column=0,textvar=tk.DoubleVar())
        self.CreateEntry(control_frame,name='K',text='StrikePrice',row=2,column=0,textvar=tk.DoubleVar())
        self.CreateEntry(control_frame,name='t',text='TimeToMaturity',row=3,column=0,textvar=tk.DoubleVar())
        self.CreateEntry(control_frame,name='r',text='RiskFreeRate',row=4,column=0,textvar=tk.DoubleVar())
        self.CreateEntry(control_frame,name='q',text='DividendYield',row=5,column=0,textvar=tk.DoubleVar())
        self.CreateEntry(control_frame,name='vol',text='Volatility',row=6,column=0,textvar=tk.DoubleVar())
        

        available_axis = ['S', 'K', 't', 'r', 'q', 'vol']
        self.CreateDropdown(control_frame,name='Xaxis', text='X-axis option',row=0,column=1,option_list=)
        self.CreateDropdown(control_frame,name='Yaxis', text='Y-axis option',row=1,column=1,option_list=)

        
        
        self.CreateButton(control_frame, name='CalculateBSPrice', text='CalculateBSPrice', row=0,column=2)
        
        for key in self.entries:
            self.entries[key].delete(0, tk.END)