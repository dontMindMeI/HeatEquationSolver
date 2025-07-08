import h5py
import numpy as np
import matplotlib.pyplot as plt


#-------------------------------------------------------#
# Exemple de lecture des fichiers
#-------------------------------------------------------#

fichier = "simulation11.h5"  # Fichier à lire


with h5py.File(fichier, 'r') as f:

    param = f["param"]
    params = {key: param.attrs[key] for key in param.attrs}
    T0 = param["T0"][()].astype(str)
    cl1 = param["cl1"][()].astype(str)
    cl2 = param["cl2"][()].astype(str)


    temperatures = {}
    residus = {}
    exacts = {}
    temps = []

    if "simulation" in f:
        sim = f["simulation"]

        for key in sim:
            try:
                grp = sim[key]

                # Récupérer l'attribut de temps (float)
                t = grp.attrs.get("t", float(key))
                temps.append(t)

                # Stocker les données associées
                temperatures[t] = grp["temperature"][()]
                if "residu" in grp:
                    residus[t] = grp["residu"][()]
                if "exacte" in grp:
                    exacts[t] = grp["exacte"][()]

            except (ValueError, KeyError, TypeError) as e:
                print(f"Ignoré: {key} (raison: {e})")

    temps = sorted(temps)



t_plot = 50.0

T = temperatures[t_plot]

N = int(params["N"])
L = float(params["L"])
x = np.linspace(0, L, N)

plt.plot(x, T, label=f"T(x) à t = {t_plot}")
plt.xlabel("x")
plt.ylabel("Température")
plt.title(f"Profil de température à t = {t_plot}")
plt.grid(True)
plt.legend()
plt.show()
