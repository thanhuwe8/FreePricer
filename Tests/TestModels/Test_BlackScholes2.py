from Models.Analytical.BlackScholes import *


#? For matplotlib plot surface
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


#* test single plot for Call option
def test_singleplot():
    S = 100
    K = 100
    t = 1
    r = 0.00
    q = 0.00
    vol = 0.2
    Optiontype = Optiontypes.EUROPEAN_CALL

    BSobject = BlackScholes()
    result = BSobject.BSSensitivityAnalysis(S, K, t, r, q, vol, Optiontype,'Delta','K', 't', 0.01, 2, 50)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    surf = ax.plot_surface(result['K'], result['t'], result['Delta'], rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    ax.set(
        xlabel = 'Strike Price',
        ylabel = 'Time to Maturity',
        zlabel = 'Delta'
    )
    fig.colorbar(surf, aspect=10, shrink=0.5)
    ax.set_title('surface')
    fig.show()


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
    
    plt.tight_layout()
    fig.show()


