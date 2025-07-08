import numpy as np

def tschemes(dt, ddt, alpha, A, B, X):

    if ddt == "EulerExplicite":
        Xn = X + alpha * dt * (A @ X + B)
        residu = (1/alpha) * (Xn - X) / dt - (A @ X + B)

    elif ddt == "EulerImplicite":
        I  = np.eye(A.shape[0])
        Xl = I - alpha * dt * A
        Xr = X + alpha * dt * B
        Xn = np.linalg.solve(Xl, Xr)
        residu = (1/alpha) * (Xn - X) / dt - (A @ Xn + B)

    elif ddt == "CrankNicolson":
        I  = np.eye(A.shape[0])
        Xl = I - (alpha * dt / 2) * A
        Xr = (I + (alpha * dt / 2) * A) @ X + alpha * dt * B
        Xn = np.linalg.solve(Xl, Xr)
        residu = (1/alpha) * (Xn - X) / dt - 0.5 * (A @ X + A @ Xn) - B

    elif ddt == "RK2":
        k1 = alpha * (A @ X + B)
        k2 = alpha * (A @ (X + dt * k1) + B)
        Xn = X + dt/2 * (k1 + k2)
        residu = (Xn - X)/dt - 1/2 * (k1 + k2)

    elif ddt == "RK4":
        k1 = alpha * (A @ X + B)
        k2 = alpha * (A @ (X + dt/2 * k1) + B)
        k3 = alpha * (A @ (X + dt/2 * k2) + B)
        k4 = alpha * (A @ (X + dt * k3) + B)
        Xn = X + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
        residu = (Xn - X)/dt - 1/6 * (k1 + 2*k2 + 2*k3 + k4)

    else:
        raise ValueError(f"Schéma de temps inconnu : {ddt}")

    residu_norm = np.linalg.norm(residu, ord=np.inf)
    return Xn, residu_norm
