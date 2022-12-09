from PackagesSetup import *
from Models.BlackScholes import *


def ImpliedVolatility(Model,Optiontype,S,K,t,r,q,vol_first,OptionPrice):
    
    eps = 1e-5
    n = 0
    vol = vol_first
    
    optPrice = Model.Calc(Optiontype=Optiontype,S=S,K=K,t=t,r=r,q=q,vol=vol)
    vega = Model.vega(Optiontype=Optiontype,S=S,K=K,t=t,r=r,q=q,vol=vol)
    
    while eps > 10e-10 and n < 10000:
        n += 1
        f = OptionPrice - optPrice
        f_prime = -1*vega
        
        vol_new = vol - f/f_prime
        eps = abs(vol_new - vol)
        vol = vol_new
        
        optPrice = Model.Calc(Optiontype=Optiontype,S=S,K=K,t=t,r=r,q=q,vol=vol)
        vega = Model.vega(Optiontype=Optiontype,S=S,K=K,t=t,r=r,q=q,vol=vol)
    print("Implied volatility is {}".format(vol))
    return(vol)


