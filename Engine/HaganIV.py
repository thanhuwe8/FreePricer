
def HaganImpliedVolatility(K,T,f,alpha,beta,rho,gamma):
    
    if type(K) == float:
        K = np.array([K])
    if K is not np.array