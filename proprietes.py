def prop(material_name):
    materials = {
        "cuivre":      {"rho": 8920, "cp": 385, "k": 390},
        "aluminium":   {"rho": 2700, "cp": 900, "k": 205},
        "acier":       {"rho": 7850, "cp": 500, "k": 50},
        "titane":      {"rho": 4500, "cp": 520, "k": 22},
        "silicium":    {"rho": 2330, "cp": 700, "k": 150},
        "verre_pyrex": {"rho": 2230, "cp": 750, "k": 1.1},
    }

    if material_name not in materials:
        raise ValueError(f"Matériau {material_name} non disponible. Choisissez parmi {list(materials.keys())}")

    return materials[material_name]




def coef(materiaux):
    print("Recupération des propriétées du matériaux")
    info = prop(materiaux) 
    return info["k"]/(info["rho"]*info["cp"])