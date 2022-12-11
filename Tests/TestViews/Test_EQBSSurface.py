
#* package setup
from PackagesSetup import *

#* MVC import
from Views.EQBSSurfaceView import *
from Controllers.EQPricingController import *
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
# import ctypes
# ctypes.windll.shcore.GetProcessDpiAwareness(1)


#* test multpleplot for put option
def test_multipleplot():
    S = 100
    K = 100
    t = 1
    r = 0.00
    q = 0.00
    vol = 0.2
    Optiontype = Optiontypes.EUROPEAN_CALL

    BSobject = BlackScholes()
    
    resultPrice = BSobject.BSSensitivityAnalysis(S, K, t, r, q, vol, Optiontype,'Price','K', 't', 0.01, 2, 50)
    resultDelta = BSobject.BSSensitivityAnalysis(S, K, t, r, q, vol, Optiontype,'Delta','K', 't', 0.01, 2, 50)
    resultGamma = BSobject.BSSensitivityAnalysis(S, K, t, r, q, vol, Optiontype,'Gamma','K', 't', 0.01, 2, 50)
    resultTheta = BSobject.BSSensitivityAnalysis(S, K, t, r, q, vol, Optiontype,'Theta','K', 't', 0.01, 2, 50)
    resultVega = BSobject.BSSensitivityAnalysis(S, K, t, r, q, vol, Optiontype,'Vega','K', 't', 0.01, 2, 50)
    resultRho = BSobject.BSSensitivityAnalysis(S, K, t, r, q, vol, Optiontype,'Rho','K', 't', 0.01, 2, 50)


    fig = plt.figure(figsize=plt.figaspect(0.5))
    plt.suptitle("BS Option surface")
    
    #* Price surface
    ax = fig.add_subplot(2, 3, 1, projection='3d')
    ax.plot_surface(resultPrice['K'], resultPrice['t'], resultPrice['Price'], 
                    rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.set_title('Price Surface')
    
    #* Delta surface
    ax = fig.add_subplot(2, 3, 2, projection='3d')
    ax.plot_surface(resultDelta['K'], resultDelta['t'], resultDelta['Delta'], 
                    rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.set_title('Delta Surface')
    
    #* Gamma surface
    ax = fig.add_subplot(2, 3, 3, projection='3d')
    ax.plot_surface(resultGamma['K'], resultGamma['t'], resultGamma['Gamma'], 
                    rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.set_title('Gamma Surface')
    
    #* Theta surface
    ax = fig.add_subplot(2, 3, 4, projection='3d')
    ax.plot_surface(resultTheta['K'], resultTheta['t'], resultTheta['Theta'], 
                    rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.set_title('Theta Surface')
    
    
    #* Vega surface
    ax = fig.add_subplot(2, 3, 5, projection='3d')
    ax.plot_surface(resultVega['K'], resultVega['t'], resultVega['Vega'], 
                    rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.set_title('Vega Surface')
    
    #* Rho surface
    ax = fig.add_subplot(2, 3, 6, projection='3d')
    ax.plot_surface(resultRho['K'], resultRho['t'], resultRho['Rho'], 
                    rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.set_title('Rho Surface')
    
    fig.tight_layout()
    return(fig)


def test_command():
    fig = test_multipleplot()

    canvas = FigureCanvasTkAgg(fig, master=frame1)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=0,column=1, rowspan=2,columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)


    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().grid(row=0,column=1)
    
    
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    
    canvas.mpl_connect("key_press_event", on_key_press)


if __name__=="__main__":
    
    root = tk.Tk()
    # root.state("zoomed")
    root.geometry('1680x1050')
    # root.attributes("-fullscreen", True)
    
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    tc = ttk.Notebook(master=root)

    frame1 = tk.LabelFrame(master=tc, text="Calculation testing")
    
    frame1.columnconfigure(0, weight=1)
    frame1.columnconfigure(1, weight=8)
    
    frame1.rowconfigure(0, weight=1)
    frame1.rowconfigure(1, weight=3)
    
    frame1.grid(row=0,column=0,stick=tk.N+tk.W+tk.S+tk.N)
    
    
    test_frame = EQBSSurfaceView(master=frame1)
    test_frame.create_view(option_list=['A', 'B', 'C', 'D'], main_text='BS pricing surface')
    
    #? Configure button
    test_frame.buttons['CalculateBSPrice'].configure(command=test_command)
    # test_frame.columnconfigure(0, 1)

    tc.add(frame1, text="EQBSSurface")
    tc.pack(expand = 1, fill ="both") 
    
    root.mainloop()