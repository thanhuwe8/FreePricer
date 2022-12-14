from Models.Analytical.BlackScholes import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

a = BlackScholes()

S = 100
K = 100
t = 1
r = 0.00
q = 0.00
vol = 0.2

y = a.Calcd1(S,K,t,r,q,vol)
x = a.Calc(Optiontype=Optiontypes.EUROPEAN_CALL,S=S,K=K,t=t,r=r,q=q,vol=vol)
delta = a.delta(Optiontype=Optiontypes.EUROPEAN_CALL,S=S,K=K,t=t,r=r,q=q,vol=vol)
gamma = a.gamma(Optiontype=Optiontypes.EUROPEAN_CALL,S=S,K=K,t=t,r=r,q=q,vol=vol)
vega = a.vega(Optiontype=Optiontypes.EUROPEAN_CALL,S=S,K=K,t=t,r=r,q=q,vol=vol)
theta = a.theta(Optiontype=Optiontypes.EUROPEAN_CALL,S=S,K=K,t=t,r=r,q=q,vol=vol)
rho = a.rho(Optiontype=Optiontypes.EUROPEAN_CALL,S=S,K=K,t=t,r=r,q=q,vol=vol)