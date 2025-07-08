import numpy as np


def init(N, T0):
      
    print("Création du champ de température initial")
    
    if T0[0] == "uniforme":
        T = np.ones(N, dtype=np.float64) * T0[1]
        
    elif T0[0] == "lineaire":
        T = np.linspace(T0[1], T0[2], N, dtype=np.float64)
        
    elif T0[0] == "marche":
        T = np.ones(N, dtype=np.float64) * T0[2] 
        pos = int(T0[3]*N)
        T[:pos] = T0[1]
        
    elif T0[0] == "porte":
        T = np.ones(N, dtype=np.float64) * T0[1] 
        pos1 = int(T0[3]*N)
        pos2 = int(T0[4]*N)
        T[pos1:pos2] = T0[2]
        
    return T
        