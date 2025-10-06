import json
import numpy as np
from qutip import Qobj

def load_fmo_params(path="../data/fmo_params.json"):
    with open(path, "r") as f:
        params = json.load(f)
    return np.array(params["site_energies"]), np.array(params["couplings"])

def fmo_hamiltonian(energies, couplings):
    """
    Build the Hamiltonian for the FMO complex.
    Energies and couplings are in cm^-1; convert to frequency units.
    """
    hbar = 5.308837e-12  # cm^-1 * s (Planck’s constant / 2π in cm^-1 units)
    H = np.diag(energies)
    H += couplings
    return Qobj(H)
