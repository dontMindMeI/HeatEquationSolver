from parametres import *
from cl import limite
from timeloop import loop
from proprietes import coef
from sauvegarde import sParam
from initialisation import init
from xschemes import d2xschemes

def solveur1D(fichier, L, N, T, dt, T0, ddt, d2x, cl1, cl2, materiaux, debut, ecriture, interval):
    
    sParam(fichier, L, N, T, dt, T0, ddt, d2x, cl1, cl2, materiaux, debut, ecriture, interval)
    
    dx = L/N;
    alpha = coef(materiaux)
       
    Xmatrix, Ximpmatrix = d2xschemes(N, d2x, dx)
    Inttemp = init(N, T0)
    
    A, X, B = limite(N, d2x, cl1, cl2, materiaux, dx, Xmatrix, Ximpmatrix, Inttemp) 
    
    loop(fichier, L, N, T, dt, ddt, cl1, cl2, debut, ecriture, interval, alpha, Inttemp, A, X, B)

    
solveur1D(fichier, L, N, T, dt, T0, ddt, d2x, cl1, cl2, materiaux, debut, ecriture, interval)