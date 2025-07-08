import numpy as np
from proprietes import prop

def limite(N, d2x, cl1, cl2, materiaux, dx, Xmatrix, Ximpmatrix, Inttemp):
    
    print("Implémentation des conditions aux limites")
    
    B = np.zeros(N, dtype=np.float64)
    A = Xmatrix.copy()  
    X = Inttemp.copy()
    if Ximpmatrix is not None:
        C = Ximpmatrix.copy() 
        
    cond = prop(materiaux)["k"]
    

    
    #--------------------------------------------#
    # Bord gauche 
    #--------------------------------------------#
    if cl1[0] == "conduction":    
        A[0,:] = 0
        A[0,0] = 1
        X[0]   = cl1[1]
        B[0]   = 0
        if d2x == "Schema5Points":
            A[1,0] = 15/(12*dx*dx)
        elif d2x == "SchemaCompact3Points":
            C[0,:] = 0
            C[0,0] = 1

    
    elif cl1[0] == "adiabatique":
        if d2x == "Schema3Points":
            A[0,0] = -2/dx**2
            A[0,1] = 2/dx**2
            
        elif d2x == "Schema5Points":
            A[0,1] = 32/(12*dx*dx)
            A[0,2] = -2/(12*dx*dx)
            A[1,1] = -31/(12*dx*dx)
            
        elif d2x == "SchemaCompact3Points":
            A[0,0] = -19/(10*dx**2)
            A[0,1] = 9/(5*dx**2)
            A[0,2] = 1/(10*dx**2)
    
    elif cl1[0] == "convection":  
        if d2x == "Schema3Points":
            A[0,0] = (-2/(dx**2))-(2*cl1[1]/(cond*dx))
            A[0,1] = 2/(dx**2)
            B[0]   = 2*cl1[1]*cl1[2]/(cond*dx)
            
        elif d2x == "Schema5Points":
            A[0,0] = (-5/(2*dx**2))-(7*cl1[1]/(3*cond*dx))
            A[0,1] = 8/(3*dx**2)
            A[0,2] = -1/(6*dx**2)
            A[1,0] = (4/(3*dx**2))+(cl1[1]/(6*cond*dx))
            A[1,1] = -31/(12*dx**2)
            B[0]   = 7*cl1[1]*cl1[2]/(3*cond*dx)
            B[1]   = -cl1[1]*cl1[2]/(6*cond*dx)

        elif d2x == "SchemaCompact3Points":
            A[0,0] = (-19/(10*dx**2))-(10*cl1[1]/(5*cond*dx))
            A[0,1] = 9/(5*dx**2)
            A[0,2] = 1/(10*dx**2)
            B[0]   = 10*cl1[1]*cl1[2]/(5*cond*dx)
   
    else:
        raise ValueError(f"Schéma de spatial inconnu au bord gauche: {cl1[0]}")
    
    #--------------------------------------------#
    # Bord droit 
    #--------------------------------------------#
    if cl2[0] == "conduction":
        A[N-1,:]   = 0
        A[N-1,N-1] = 1
        X[N-1]     = cl2[1]
        B[N-1]     = 0
        if d2x == "Schema5Points":
            A[N-2,N-1] = 15/(12*dx*dx)
        elif d2x == "SchemaCompact3Points":
            C[N-1,:]   = 0
            C[N-1,N-1] = 1

    
    elif cl2[0] == "adiabatique":
        if d2x == "Schema3Points":
            A[N-1,N-1] = -2/dx**2
            A[N-1,N-2] = 2/dx**2
            
        elif d2x == "Schema5Points":
            A[N-1,N-2] = 32/(12*dx*dx)
            A[N-1,N-3] = -2/(12*dx*dx)
            A[N-2,N-2] = -31/(12*dx*dx)
              
        elif d2x == "SchemaCompact3Points":
            A[N-1,N-1] = -19/(10*dx**2)
            A[N-1,N-2] = 9/(5*dx**2)
            A[N-1,N-3] = 1/(10*dx**2)
        
    elif cl2[0] == "convection": 
        if d2x == "Schema3Points": 
            A[N-1,N-1] = (-2/(dx**2))-(2*cl2[1]/(cond*dx))
            A[N-1,N-2] = 2/(dx**2)
            B[-1]      = 2*cl2[1]*cl2[2]/(cond*dx)
            
        elif d2x == "Schema5Points":
            A[N-1,N-1] = (-5/(2*dx**2))-(7*cl2[1]/(3*cond*dx))
            A[N-1,N-2] = 8/(3*dx**2)
            A[N-1,N-3] = -1/(6*dx**2)
            A[N-2,N-1] = (4/(3*dx**2))+(cl2[1]/(6*cond*dx))
            A[N-2,N-2] = -31/(12*dx**2)
            B[N-1]   = 7*cl2[1]*cl2[2]/(3*cond*dx)
            B[N-2]   = -cl2[1]*cl2[2]/(6*cond*dx)
            
        elif d2x == "SchemaCompact3Points":
            A[N-1,N-1] = (-19/(10*dx**2))-(10*cl2[1]/(5*cond*dx))
            A[N-1,N-2] = 9/(5*dx**2)
            A[N-1,N-3] = 1/(10*dx**2)
            B[-1]      = 10*cl2[1]*cl2[2]/(5*cond*dx)
            
    else:
        raise ValueError(f"Schéma de spatial inconnu au bord droit : {cl2[0]}")




    if Ximpmatrix is not None:
        A = np.linalg.inv(C) @ A
        B = np.linalg.inv(C) @ B
    
    return A, X, B