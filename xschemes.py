import numpy as np

def d2xschemes(N, laplacien, dx):
    A = np.zeros((N, N), dtype=np.float64)
    B = None  # Pour schéma compact implicite
    
    print("Discrétisation de la dérivée seconde en espace")
    
    if laplacien == "Schema3Points":
        np.fill_diagonal(A, -2/(dx*dx))
        np.fill_diagonal(A[:, 1:], 1/(dx*dx))
        np.fill_diagonal(A[1:, :], 1/(dx*dx))
        
    elif laplacien == "Schema5Points":
        np.fill_diagonal(A, -30/(12*dx*dx))
        np.fill_diagonal(A[:, 1:], 16/(12*dx*dx))
        np.fill_diagonal(A[1:, :], 16/(12*dx*dx))
        np.fill_diagonal(A[:, 2:], -1/(12*dx*dx))
        np.fill_diagonal(A[2:, :], -1/(12*dx*dx))
    
    
    elif laplacien == "SchemaCompact3Points":
        alpha = 1/10
        a = 6/5
    
        A = np.zeros((N, N))
        np.fill_diagonal(A, -2 * a / (dx*dx))
        np.fill_diagonal(A[:, 1:], a / (dx*dx))     
        np.fill_diagonal(A[1:, :], a / (dx*dx)) 
    
        B = np.eye(N)
        np.fill_diagonal(B[:, 1:], alpha)   
        np.fill_diagonal(B[1:, :], alpha) 

    
    else:
        raise ValueError(f"Type de schémas spatial inconnu : {laplacien}")
    
    return A, B

