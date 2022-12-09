from PackagesSetup import *

from Utils.Types import *
from Utils.Vars import *
from Utils.Maths import *

from Models.Analytical.Analytical.BaseModel import *


class BlackScholes(BaseModel):
    
    def __init__(self):
        self.data = None
    
    def setdata(self, S, K, t, r, q, vol, Optiontype):
        self.data = {'S':S, 'K':K, 't':t, 'r':r, 'q':q, 'vol':vol}
        self.Optiontype = Optiontype
    
    
    def getdata(self):
        return(self.data)
    
    
    def Calcd1(self,S,K,t,r,q,vol):
        K = np.maximum(K, gSmall)
        t = np.maximum(t, gSmall)
        vol = np.maximum(vol, gSmall)
        
        volsqrtT = vol*np.sqrt(t)
        sdc = S*np.exp(-q*t)
        kdc = K*np.exp(-r*t)
        
        d1 = np.log(sdc/kdc)/volsqrtT + volsqrtT/2.0
        return(d1)


    def Calcd2(self,S,K,t,r,q,vol):
        d1 = self.Calcd1(S,K,t,r,q,vol)
        d2 = d1 - vol*np.sqrt(t)
        return(d2)
    
    
    def payoff(self, Optiontype,S,K,t,r,q,vol):
        if Optiontype == Optiontypes.EUROPEAN_CALL:
            phi = 1
        elif Optiontype == Optiontypes.EUROPEAN_PUT:
            phi = -1
        else:
            print("error")
            return 0.0
        payoff = np.maximum((S-K)*phi, 0)
        return(payoff)


    def Calc(self,Optiontype,S,K,t,r,q,vol):
        if Optiontype == Optiontypes.EUROPEAN_CALL:
            phi = 1
        elif Optiontype == Optiontypes.EUROPEAN_PUT:
            phi = -1
        else:
            print("error")
            return(0.0)
        
        sdc = S*np.exp(-q*t)
        kdc = K*np.exp(-r*t)
        
        d1 = self.Calcd1(S,K,t,r,q,vol)
        d2 = self.Calcd2(S,K,t,r,q,vol)
        
        value = phi*sdc*NCDF(phi*d1) - phi*kdc*NCDF(phi*d2)
        return(value)
    
    
    def delta(self,Optiontype,S,K,t,r,q,vol):
        if Optiontype == Optiontypes.EUROPEAN_CALL:
            phi = 1
        elif Optiontype == Optiontypes.EUROPEAN_PUT:
            phi = -1
        else:
            print("error")
            return 0.0
        
        K = np.maximum(K, gSmall)
        t = np.maximum(t, gSmall)
        vol = np.maximum(vol, gSmall)
        
        d1 = self.Calcd1(S,K,t,r,q,vol)
        delta = phi*np.exp(-q*t)*NCDF(phi*d1)
        return(delta)

    
    def gamma(self,Optiontype,S,K,t,r,q,vol):
        K = np.maximum(K,gSmall)
        t = np.maximum(t,gSmall)
        vol = np.maximum(vol,gSmall)
        vsqrtT = vol*np.sqrt(t)
        
        d1 = self.Calcd1(S,K,t,r,q,vol)
        gamma = np.exp(-q*t)*NPDF(d1)
        return(gamma)
    
    
    def vega(self,Optiontype,S,K,t,r,q,vol):
        K = np.maximum(K,gSmall)
        t = np.maximum(t,gSmall)
        vol = np.maximum(vol, gSmall)
        sqrtT = np.sqrt(t)
        
        sdc = S*np.exp(-q*t)
        kdc = K*np.exp(-r*t)
        d1 = self.Calcd1(S,K,t,r,q,vol)
        vega = sdc*sqrtT*NPDF(d1)
        return(vega)


    def theta(self,Optiontype,S,K,t,r,q,vol):
        if Optiontype == Optiontypes.EUROPEAN_CALL:
            phi = 1
        elif Optiontype == Optiontypes.EUROPEAN_PUT:
            phi = -1
        else:
            print("error")
            return 0.0

        K = np.maximum(K,gSmall)
        t = np.maximum(t,gSmall)
        vol = np.maximum(vol,gSmall)
        sqrtT = np.sqrt(t)
        vsqrtT = vol*np.sqrt(t)
        sdc = S*np.exp(-q*t)
        kdc = K*np.exp(-r*t)
        
        d1 = self.Calcd1(S,K,t,r,q,vol)
        d2 = self.Calcd2(S,K,t,r,q,vol)
        
        theta = -1*sdc*NPDF(d1)*vol/2.0/sqrtT-phi*r*K*np.exp(-r*t)*NCDF(phi*d2) + phi*q*sdc*NCDF(phi*d1)
        return(theta)
    
    
    def rho(self,Optiontype,S,K,t,r,q,vol):
        if Optiontype == Optiontypes.EUROPEAN_CALL:
            phi = 1
        elif Optiontype == Optiontypes.EUROPEAN_PUT:
            phi = -1
        else:
            print("error")
            return 0.0
        
        K = np.maximum(K,gSmall)
        t = np.maximum(t,gSmall)
        vol = np.maximum(vol,gSmall)
        
        sqrtT = np.sqrt(t)
        vsqrtT = vol*np.sqrt(t)
        sdc = S*np.exp(-q*t)
        kdc = S*np.exp(-r*t)
        
        d1 = self.Calcd1(S,K,t,r,q,vol)
        d2 = self.Calcd2(S,K,t,r,q,vol)
        
        rho = phi*K*t*np.exp(-r*t)*NCDF(phi*d2)
        return(rho)
        
    
    
    
    