# QED-TDDFT: Quantum-electrodynamical Time-dependent Density Functional Theory

`qed-tddft` is a Python library for Quantum-electrodynamical Time-dependent Density Functional Theory (QED-TDDFT) simulations, built on the [PySCF](https://pyscf.org/) framework. It enables the simulation of light-matter interactions in optical cavities, specifically focusing on polaritonic excited states and their potential energy surfaces.

## 🚀 Installation

1. **Install Dependencies**:
   ```bash
   pip install pyscf numpy scipy matplotlib
   ```

2. **Clone and Setup**:
   ```bash
   git clone git@github.com:cc-ats/qed-tddft.git
   cd qed-tddft
   export PYTHONPATH=$(pwd):$PYTHONPATH
   ```

## 📚 Tutorials

The project includes a series of interactive Jupyter notebooks to help you get started:

- **[Lesson 1: TDA-JC Basics](./Lesson1_TDAJC.ipynb)**: An introduction to the Tamm-Dancoff approximation with Jaynes-Cummings (TDA-JC), Rotating-Wave Approximation (RWA), Rabi, and Pauli-Fierz (PF) models. Learn how to model polariton spectra as a function of coupling strength.
- **[Lesson 2: Multi-State Coupling](./Lesson2_TDAnJC.ipynb)**: Extends the TDA-JC model to include multiple excited states ($TDA_n-JC$). Compare the differences between multi-state JC models and the full Pauli-Fierz treatment.
- **[Lesson 3: Multi-System Applications](./Lesson3_many_mol.ipynb)**: Focuses on collective polaritons in systems containing many molecules. Understand the theoretical framework and computational application of TDA-JC and TDA-PF in multi-fragment configurations.

## ✨ Key Features

- **Cavity Models (`qed/cavity/`)**:
  - Supports Restricted (RHF/RKS), Unrestricted (UHF/UKS), and Generalized (GHF/GKS) frameworks.
  - Implements **Pauli-Fierz (PF)**, **Rabi**, **Jaynes-Cummings (JC)**, and **Rotating Wave Approximation (RWA)**.
  - Handles Dipole Self-Energy (DSE) and magnetic dipole moments.
- **Excited State Solvers (`qed/tdscf/`)**:
  - **QED-TDA**: Efficient Tamm-Dancoff solvers for electronic-photonic eigenvalue problems.
  - **QED-RPA / QED-TDDFT**: Full linear response including excitation/de-excitation amplitudes and photon creation/annihilation.
  - Efficient Davidson and Davidson-QR algorithms for extracting polaritonic roots.
- **Analytic Gradients (`qed/grad/`)**:
  - Implements analytic energy gradients for QED-TDDFT states, enabling geometry optimizations on polaritonic potential energy surfaces.
- **Multi-Fragment Simulations**:
  - Specialized drivers for **Collective Polaritons** with support for inter-fragment Coulomb and Dipole-Dipole interactions.

## 💻 Usage Examples

### Python API
```python
import numpy
from pyscf import gto, scf
import qed

# 1. Define Molecule
mol = gto.M(atom='H 0 0 0; F 0 0 1.1', basis='cc-pVDZ')
mf = scf.RKS(mol).set(xc='b3lyp')
mf.kernel()

# 2. Configure Cavity
cavity_freq = numpy.array([0.200])
cavity_mode = numpy.array([[0.001, 0.0, 0.0]]) # Strength and Orientation

# 3. Solve QED-TDDFT
cav_model = qed.PF(mf, cavity_mode=cavity_mode, cavity_freq=cavity_freq)
td = qed.TDDFT(mf, cav_obj=cav_model)
td.nroots = 5
td.kernel()
```

### Input-File Driver
Run collective polariton simulations using the provided driver:
```bash
python qed/tdscf/collective_polariton.py examples/03-qed-tddft.in pf 0.010-y 0.1483
```

## 📖 References

If you use this software, please cite:

1.  **QED-TDDFT Theory**:
    Yang, J., et al. "Quantum-electrodynamical time-dependent density functional theory within Gaussian atomic basis." *J. Chem. Phys.* **155**, 064107 (2021). [DOI: 10.1063/5.0057542](https://doi.org/10.1063/5.0057542)
2.  **Analytic Gradients**:
    Yang, J., et al. "Cavity quantum-electrodynamical time-dependent density functional theory within Gaussian atomic basis. II. Analytic energy gradient." *J. Chem. Phys.* **156**, 124104 (2022). [DOI: 10.1063/5.0082386](https://doi.org/10.1063/5.0082386)
3.  **PySCF**:
    Sun, Q., et al. "PySCF: the Python-based simulations of chemistry framework." *WIREs Comput. Mol. Sci.* **8**: e1340 (2018). [DOI: 10.1002/wcms.1340](https://doi.org/10.1002/wcms.1340)
