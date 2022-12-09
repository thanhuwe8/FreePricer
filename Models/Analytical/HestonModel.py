from PackagesSetup import *
from Utils.Complex import *


class HestonModel:
    
    def __init__(self,phi,kappa,theta,lbda,rho,sigma,tau,K,S,r,q,v0,pnum):
        #! Model paramters
        self.phi = phi
        self.kappa = kappa
        self.theta = theta
        self.lbda = lbda
        self.rho = rho
        self.sigma = sigma
        self.tau = tau
        
        #! Market/Product parameters
        self.K = K
        self.S = S
        self.r = r
        self.q = q
        self.v0 = v0
        self.pnum = pnum
    
        self.x = np.log(S)
        
        i = 