import numpy as np

def exacte(L, cl1, cl2, alpha, Inttemp, x, t):
    if cl1[0] == "conduction" and cl2[0] == "conduction":
       
        w = cl1[1] + (cl2[1] - cl1[1]) * x / L
        
        g = Inttemp - w
        
        u = np.zeros_like(x)
        for n in range(1, 1000):
            lambda_n = n * np.pi / L
            bn = 2 / L * np.trapz(g * np.sin(lambda_n * x), x)
            u += bn * np.sin(lambda_n * x) * np.exp(-alpha * lambda_n**2 * t)
        
        return u + w
    else:
        return None
