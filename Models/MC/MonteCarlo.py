from PackagesSetup import *

'''
def MonteCarloPricer(randomNumberGenerator, nPaths, nThreads, valDate, fixings):

'''


def MonteCarloGBMPaths(nPaths,nSteps,T,r,sigma,S0,seed=200):
    np.random.seed(seed)
    
    nPaths = int(nPaths)
    
    Z = np.random.normal(0.0,1.0,[nPaths,nSteps])
    W = np.zeros([nPaths, nSteps])
    
    S1 = np.zeros([nPaths, nSteps+1])
    S1[:,0] = S0
    
    S2 = np.zeros([nPaths,nSteps+1])
    S2[:,0] = S0
    
    time = np.zeros([nSteps+1])
    
    dt = T/float(nSteps)
    
    for i in range(0, nSteps):
        if nPaths > 1:
            Z[:,i] = (Z[:,i] - np.mean(Z[:,i]))/np.std(Z[:,i])
        W[:,i+1] = W[:,i] + np.power(dt, 0.5)*Z[:,i]
        
        S1[:,i+1] = S1[:,i] + r*S1[:,i]*dt + sigma*S1[:,i]*(W[:,i+1]-W[:,i])
        S2[:,i+1] = S2[:,i] + np.exp((r-0.5*sigma*sigma)*dt + sigma*(W[:,i+1] - W[:,i]))
        time[i+1] = time[i] + dt
    paths = {"time":time, "S1":S1, "S2":S2}
    return(paths)
    
    
    