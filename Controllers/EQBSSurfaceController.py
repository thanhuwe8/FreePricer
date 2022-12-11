

from abc import ABC, abstractmethod
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as msg
from tkinter.ttk import Notebook
from tkinter import filedialog

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure



from PackagesSetup import *
from Views.EQPricingViews import *
from Controllers.BaseControllers import *
from Models.Analytical.BlackScholes import *


class EQBSSurfaceController(Controller):
    
    def __init__(self) -> None:
        self.model = BlackScholes()
        self.view = None
        self.data = None
        self.option_list = ['EUROPEAN_CALL', 'EUROPEAN_PUT']
    
    def bind(self,view=BaseView):
        self.view = view
        self.view.create_view(option_list=self.option_list, main_text='BS pricing surface')
        self.view.buttons['GenerateFullSurface'].configure(command=self.ControllerFullSurface)
        self.view.buttons['GenerateSingleSurface'].configure(command=self.ControllerSingleSurface)
    
    def CreateFullSurface(self, S, K, t, r, q, vol, Optiontype, xaxis, yaxis):
        
        BSobject = BlackScholes()
        
        resultPrice = BSobject.BSSensitivityAnalysis(S, K, t, r, q, vol, Optiontype,'Price',xaxis, yaxis, 0.01, 2, 50)
        resultDelta = BSobject.BSSensitivityAnalysis(S, K, t, r, q, vol, Optiontype,'Delta',xaxis, yaxis, 0.01, 2, 50)
        resultGamma = BSobject.BSSensitivityAnalysis(S, K, t, r, q, vol, Optiontype,'Gamma',xaxis, yaxis, 0.01, 2, 50)
        resultTheta = BSobject.BSSensitivityAnalysis(S, K, t, r, q, vol, Optiontype,'Theta',xaxis, yaxis, 0.01, 2, 50)
        resultVega = BSobject.BSSensitivityAnalysis(S, K, t, r, q, vol, Optiontype,'Vega',xaxis, yaxis, 0.01, 2, 50)
        resultRho = BSobject.BSSensitivityAnalysis(S, K, t, r, q, vol, Optiontype,'Rho',xaxis, yaxis, 0.01, 2, 50)

        fig = plt.figure(figsize=plt.figaspect(0.5))
        plt.suptitle("BS Option surface for {}".format(Optiontype))
        
        #* Price surface
        ax = fig.add_subplot(2, 3, 1, projection='3d')
        ax.plot_surface(resultPrice[xaxis], resultPrice[yaxis], resultPrice['Price'], 
                        rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        ax.set(
            xlabel=str(xaxis),
            ylabel=str(yaxis),
            zlabel='Price'
        )
        ax.set_title('Price Surface')
        
        #* Delta surface
        ax = fig.add_subplot(2, 3, 2, projection='3d')
        ax.plot_surface(resultDelta[xaxis], resultDelta[yaxis], resultDelta['Delta'], 
                        rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        ax.set(
            xlabel=str(xaxis),
            ylabel=str(yaxis),
            zlabel='Delta'
        )
        ax.set_title('Delta Surface')
        
        #* Gamma surface
        ax = fig.add_subplot(2, 3, 3, projection='3d')
        ax.plot_surface(resultGamma[xaxis], resultGamma[yaxis], resultGamma['Gamma'], 
                        rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        ax.set(
            xlabel=str(xaxis),
            ylabel=str(yaxis),
            zlabel='Gamma'
        )
        ax.set_title('Gamma Surface')
        
        #* Theta surface
        ax = fig.add_subplot(2, 3, 4, projection='3d')
        ax.plot_surface(resultTheta[xaxis], resultTheta[yaxis], resultTheta['Theta'], 
                        rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        ax.set(
            xlabel=str(xaxis),
            ylabel=str(yaxis),
            zlabel='Theta'
        )
        ax.set_title('Theta Surface')
        
        
        #* Vega surface
        ax = fig.add_subplot(2, 3, 5, projection='3d')
        ax.plot_surface(resultVega[xaxis], resultVega[yaxis], resultVega['Vega'], 
                        rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        ax.set(
            xlabel=str(xaxis),
            ylabel=str(yaxis),
            zlabel='Vega'
        )
        ax.set_title('Vega Surface')
        
        #* Rho surface
        ax = fig.add_subplot(2, 3, 6, projection='3d')
        ax.plot_surface(resultRho[xaxis], resultRho[yaxis], resultRho['Rho'], 
                        rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        ax.set(
            xlabel=str(xaxis),
            ylabel=str(yaxis),
            zlabel='Rho'
        )
        ax.set_title('Rho Surface')
        
        fig.tight_layout()
        return(fig)


    def CreateSingleSurface(self, S, K, t, r, q, vol, Optiontype, metrics, xaxis, yaxis):
        BSobject = BlackScholes()
        
        result= BSobject.BSSensitivityAnalysis(S, K, t, r, q, vol, Optiontype, metrics, xaxis, yaxis, 0.01, 2, 50)

        fig = plt.figure(figsize=plt.figaspect(0.5))
        plt.suptitle("BS Option surface for {}".format(Optiontype))
        
        #* Price surface
        ax = fig.add_subplot(1, 1, 1, projection='3d')
        ax.plot_surface(result[xaxis], result[yaxis], result[metrics], 
                        rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        ax.set(
            xlabel=str(xaxis),
            ylabel=str(yaxis),
            zlabel=str(metrics)
        )
        ax.set_title('{} Surface'.format(str(metrics)))
        
        fig.tight_layout()
        return(fig)
    
    
    def ControllerFullSurface(self):
        print("Calculate Black-Scholes")
        
        Optiontype_str = str(self.view.variables['Optiontype'].get())
        print(Optiontype_str)
        if Optiontype_str == 'EUROPEAN_CALL':
            Optiontype_input = Optiontypes.EUROPEAN_CALL
        elif Optiontype_str == 'EUROPEAN_PUT':
            Optiontype_input = Optiontypes.EUROPEAN_PUT
        else:
            self.view
            print("Check available option")
        
        S_input = float(self.view.entries['S'].get())
        K_input = float(self.view.entries['K'].get())
        t_input = float(self.view.entries['t'].get())
        r_input = float(self.view.entries['r'].get())
        q_input = float(self.view.entries['q'].get())
        vol_input = float(self.view.entries['vol'].get())
        
        xaxis = str(self.view.variables['xaxis'].get())
        yaxis = str(self.view.variables['yaxis'].get())
        
        fig = self.CreateFullSurface(S_input, K_input, t_input, r_input, q_input, vol_input, Optiontype_input, xaxis, yaxis)
        
        self.view.CreateMPLFrame(figure=fig, name='MPLtab', text='PricingSurface', row=0, column=1)
        
        
    def ControllerSingleSurface(self):
        print("Calculate Black-Scholes")
        
        Optiontype_str = str(self.view.variables['Optiontype'].get())
        print(Optiontype_str)
        if Optiontype_str == 'EUROPEAN_CALL':
            Optiontype_input = Optiontypes.EUROPEAN_CALL
        elif Optiontype_str == 'EUROPEAN_PUT':
            Optiontype_input = Optiontypes.EUROPEAN_PUT
        else:
            self.view
            print("Check available option")
        
        S_input = float(self.view.entries['S'].get())
        K_input = float(self.view.entries['K'].get())
        t_input = float(self.view.entries['t'].get())
        r_input = float(self.view.entries['r'].get())
        q_input = float(self.view.entries['q'].get())
        vol_input = float(self.view.entries['vol'].get())
        
        xaxis = str(self.view.variables['xaxis'].get())
        yaxis = str(self.view.variables['yaxis'].get())
        metrics = str(self.view.variables['zaxis'].get())
        
        print(metrics)
        print(type(metrics))
        
        fig = self.CreateSingleSurface(S_input, K_input, t_input, r_input, q_input, vol_input, Optiontype_input, metrics, xaxis, yaxis)
        
        self.view.CreateMPLFrame(figure=fig, name='MPLtab', text='SingleSurface', row=0, column=1)
