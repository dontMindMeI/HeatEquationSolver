import numpy as np
from solution import exacte
from ddtschemes import tschemes
from simcontrol import tinit, stabilitee
from sauvegarde import sVerif, sTemps

def loop(fichier, L, N, T, dt, ddt, cl1, cl2, debut, ecriture, interval, alpha, Inttemp, A, X, B):
    Xc = X.copy()
    x = np.linspace(0, L, N)  
    t = tinit(debut)

    _, R0 = tschemes(dt, ddt, alpha, A, B, Xc)
    if R0 == 0:
        R0 = 1e-16  
    
    sTemps(fichier, X, t, 1.0, None)
    
    while t < T:
        t += dt
        print("")
        print(f"Résolution pour le temps {t} s")
        Xc, Rabs = tschemes(dt, ddt, alpha, A, B, Xc)
        R = Rabs / R0
        
        if not stabilitee(R):
            print("Schéma instable")
            break
        
        if sVerif(t, dt, ecriture, interval):
            s = exacte(L, cl1, cl2, alpha, Inttemp, x, t)
            sTemps(fichier, Xc, t, R, s)
            
