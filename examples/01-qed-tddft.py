import numpy
from pyscf import gto, scf, tdscf

import qed

mol         = gto.Mole()
mol.verbose = 4
mol.atom    = '''
H       -0.9450370725    -0.0000000000     1.1283908757
C       -0.0000000000     0.0000000000     0.5267587663
H        0.9450370725     0.0000000000     1.1283908757
O        0.0000000000    -0.0000000000    -0.6771667936
'''
mol.basis = 'cc-pVDZ'
mol.build()

mf    = scf.RKS(mol)
mf.xc = "b3lyp"
mf.kernel()

td = tdscf.TDA(mf)
td.nroots = 10
td.kernel()

cavity_freq = numpy.asarray([0.2940])
cavity_mode = numpy.asarray([[0.001, 0.0, 0.0]])

# TDDFT-PF
key = {'cavity_mode': cavity_mode, 'cavity_freq': cavity_freq}
cav_model = qed.PF(mf, key)
td        = qed.TDDFT(mf, td, cav_model, key)
td.nroots = 10
td.kernel()

# TDA-JC
cav_model = qed.JC(mf, key)
td        = qed.TDA(mf, td, cav_model, key)
td.nroots = 10
td.kernel()
