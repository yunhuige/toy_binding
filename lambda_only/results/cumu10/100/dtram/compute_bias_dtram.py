import sys, os
import numpy as np
from pyemma.thermo.util import get_averaged_bias_matrix as _get_averaged_bias_matrix

new_ass = np.load('../combined_assignment.npy',allow_pickle=True)
dtraj = [[] for i in range(len(new_ass))]
for i in range(len(new_ass)):
        for j in range(len(new_ass[i])):
                dtraj[i].append(int(new_ass[i][j]))
dtrajs = []
for i in range(len(dtraj)):
    dtrajs.append(np.array(dtraj[i]))
bias = np.load('../bias_tram.npy',allow_pickle=True)

bias_dtram = _get_averaged_bias_matrix(bias,dtrajs,nstates = 18)

np.save('bias_dtram.npy',bias_dtram)

