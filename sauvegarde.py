import h5py
import os
import numpy as np

def sVerif(t, dt, ecriture, interval, eps=1e-7):
    r = False
    if ecriture == "t":
        if abs(t % interval) < eps or abs(interval - (t % interval)) < eps:
            r = True 
    elif ecriture == "iteration":
        if int(round(t/dt)) % interval == 0:
            r = True
    return r



def sParam(fichier, L, N, T, dt, T0, ddt, d2x, cl1, cl2, materiaux, debut, ecriture, interval):
    with h5py.File(fichier, 'a') as f:
        grp = f.require_group("param")

        # Parametres scalaires simples (attributs)
        grp.attrs["L"] = L
        grp.attrs["N"] = N
        grp.attrs["T"] = T
        grp.attrs["dt"] = dt
        grp.attrs["ddt"] = ddt
        grp.attrs["d2x"] = d2x
        grp.attrs["materiaux"] = materiaux
        grp.attrs["debut"] = debut
        grp.attrs["ecriture"] = ecriture
        grp.attrs["interval"] = interval

        # Etat initial (dataset)
        if "T0" in grp:
            del grp["T0"]
        grp.create_dataset("T0", data=np.array(T0, dtype="S"))

        # Conditions aux limites (datasets)
        for name, cl in zip(["cl1", "cl2"], [cl1, cl2]):
            if name in grp:
                del grp[name]
            grp.create_dataset(name, data=np.array(cl, dtype="S"))

        
def sTemps(fichier, Xc, t, R, sAnalytique):
    print("   - Sauvegarde")

    mode = 'a' if os.path.exists(fichier) else 'w'
    time = round(t, 8)  
    group_name = f"{time:.8f}"  

    with h5py.File(fichier, mode) as f:
        sim_group = f.require_group("simulation")
        time_group = sim_group.create_group(group_name)

        time_group.create_dataset("temperature", data=Xc)
        time_group.attrs["t"] = time

        if R is not None:
            time_group.create_dataset("residu", data=R)
            
        if sAnalytique is not None:
            time_group.create_dataset("exacte", data=sAnalytique)

