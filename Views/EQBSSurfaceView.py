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


class EQBSSurfaceView(BaseView):
    def __init__(self, master=None):
        super().__init__(master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=6)
        self.option_list = ['EUROPEAN_CALL', 'EUROPEAN_PUT']


    def create_view(self, option_list, main_text='BS pricing surface'):
        surfaceframe = tk.LabelFrame(master=self, text=main_text, font=('Helvetica 11 bold'))
        surfaceframe.grid(row=0,column=0,sticky=tk.W+tk.E+tk.N,padx=3,pady=3)
        
        for i in range(15):
            surfaceframe.rowconfigure(i,weight=1)
        # for i in range(0,2):
        #     control_frame.columnconfigure(i,weight=1)
        
        #* Status bar
        self.CreateLabel(surfaceframe,name='StatusBar',text='Status Bar',label_text="Surface Pricing is created",row=0,column=0)
        
        self.CreateDropdown(surfaceframe,name='Optiontype', text='Option Type',row=1,column=0,option_list=self.option_list)
        self.CreateEntry(surfaceframe,name='S',text='StockPrice',row=2,column=0,textvar=tk.DoubleVar(), defaultvalue=20.0)
        self.CreateEntry(surfaceframe,name='K',text='StrikePrice',row=3,column=0,textvar=tk.DoubleVar(), defaultvalue=20.0)
        self.CreateEntry(surfaceframe,name='t',text='TimeToMaturity',row=4,column=0,textvar=tk.DoubleVar(), defaultvalue=1.0)
        self.CreateEntry(surfaceframe,name='r',text='RiskFreeRate',row=5,column=0,textvar=tk.DoubleVar(), defaultvalue=0.00)
        self.CreateEntry(surfaceframe,name='q',text='DividendYield',row=6,column=0,textvar=tk.DoubleVar(), defaultvalue=0.00)
        self.CreateEntry(surfaceframe,name='vol',text='Volatility',row=7,column=0,textvar=tk.DoubleVar(), defaultvalue=0.2)
        
        #* Surface inputs
        available_axis = ['S', 'K', 't', 'r', 'q', 'vol']
        self.CreateDropdown(surfaceframe,name='xaxis', text=available_axis[0],row=8,column=0,option_list=available_axis)
        self.CreateDropdown(surfaceframe,name='yaxis', text=available_axis[1],row=9,column=0,option_list=available_axis)
        
        #* Buttons
        self.CreateButton(surfaceframe, name='GenerateFullSurface', text='GenerateFullSurface', row=11,column=0)

        available_zaxis = ['Price', 'Delta', 'Gamma', 'Vega', 'Theta', 'Rho']
        self.CreateDropdown(surfaceframe,name='zaxis', text='Price',row=13,column=0,option_list=available_zaxis)
        self.CreateButton(surfaceframe, name='GenerateSingleSurface', text='GenerateSingleSurface', row=14,column=0)