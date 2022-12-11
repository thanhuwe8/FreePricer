
#* package setup
from PackagesSetup import *

#* MVC import
from Views.EQBSSurfaceView import *
from Controllers.EQPricingController import *
from Controllers.EQBSSurfaceController import *
from Models.Analytical.BlackScholes import *

#* Tkinter
import tkinter as tk
from tkinter import *

#* Matplotlib
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure



if __name__=="__main__":
    
    root = tk.Tk()
    # root.state("zoomed")
    root.geometry('1680x1050')
    # root.attributes("-fullscreen", True)
    
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    tc = ttk.Notebook(master=root)
    
    view = EQBSSurfaceView(tc)
    controller = EQBSSurfaceController()
    controller.bind(view)
    
    # test_frame.columnconfigure(0, 1)

    tc.add(view, text="EQBSSurface")
    tc.pack(expand = 1, fill ="both") 
    
    root.mainloop()