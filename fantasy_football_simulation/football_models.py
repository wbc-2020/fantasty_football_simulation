import numpy as np




#models for play types

def predict_run():
    return np.random.poisson(lam = 5)
    
    
def predict_pass():
    return np.random.poisson(lam = 5)