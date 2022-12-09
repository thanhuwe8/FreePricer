from PackagesSetup import *
from Views.BasicViews import *

import tkinter
import tkinter as tk
from tkinter import ttk

from abc import abstractmethod
from typing import List




class HestonInputViews(View):

    def _add_frame(self, label, cols = 3):
        frame = ttk.LabelFrame(self, text=label)
        frame.grid(sticky=tk.W + tk.E)
        for i in range(cols):
            frame.columnconfigure(i, weight=1)
        return(frame)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self._vars = {
            'SpotPrice':tk.DoubleVar, 
            'Strike':tk.StringVar, 
            'TimeToMaturity':tk.DoubleVar, 
            'RiskFreeRate':tk.DoubleVar, 
            'DividendRate':tk.DoubleVar, 
            'Kappa':tk.DoubleVar, 
            'Theta':tk.DoubleVar, 
            'Sigma':tk.DoubleVar, 
            'V0':tk.DoubleVar, 
            'Rho':tk.DoubleVar, 
            'Lambda':tk.DoubleVar,
            'Trap':tk.DoubleVar
        }
    
        self.columnconfigure(1, weight=1)
        
        input_info = self._add_frame("Input Parameters for Heston")
        
        #? 1st section: Market information
        
        
        
        
        #? 2nd section: 
        