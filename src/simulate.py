import numpy as np
from qutip import mesolve, basis
from fmo_model import load_fmo_params, fmo_hamiltonian

def run_dynamics(tmax=1.0, steps=200):
    energies, couplings = load_fmo_params()
    H = fmo_hamiltonian(energies, couplings)

    # Initial state: excitation on site 0
    psi0 = basis(len(energies), 0)

    # Time array (ps)
    tlist = np.linspace(0, tmax, steps)

    # Simple pure dephasing Lindblad operators
    gamma = 0.01  # dephasing rate
    c_ops = []
    for i in range(len(energies)):
        proj = basis(len(energies), i) * basis(len(energies), i).dag()
        c_ops.append(np.sqrt(gamma) * proj)

    result = mesolve(H, psi0, tlist, c_ops, [basis(len(energies), i) * basis(len(energies), i).dag() for i in range(len(energies))])
    return tlist, np.array(result.expect)
