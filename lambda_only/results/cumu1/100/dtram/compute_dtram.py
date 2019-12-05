import sys, os
import numpy as np
from pyemma.thermo import dtram
from pyemma import msm
import pyemma

ttraj = np.load('../ttraj.npy',allow_pickle=True)
ttrajs = [[] for i in range(len(ttraj))]
for i in range(len(ttraj)):
        for j in range(len(ttraj[i])):
                ttrajs[i].append(int(ttraj[i][j]))

new_ass = np.load('../combined_assignment.npy',allow_pickle=True)
#dtrajs=np.load('combined_assignment.npy',allow_pickle=True)
dtrajs = [[] for i in range(len(new_ass))]
for i in range(len(new_ass)):
        for j in range(len(new_ass[i])):
                dtrajs[i].append(int(new_ass[i][j]))
#dtrajs = []
#for i in range(len(new_ass)):
#       dtrajs.append(new_ass[i])
#print isinstance(dtrajs, (list, tuple))
#print isinstance(dtrajs, (list, tuple)) and (all(isinstance(s, string_types) for s in dtrajs))
#print isinstance(dtrajs, np.ndarray)
      #  if l.ndim == 1 and (l.dtype.kind == 'i' or l.dtype.kind == 'u'):
#print dtrajs.ndim == 1 and (dtrajs.dtype.kind == 'i' or dtrajs.dtype.kind == 'u')      
#sys.exit()

bias = np.load('bias_dtram.npy',allow_pickle=True)

lagtimes = np.array([1,2])
motion = 1
dtram_obj = dtram(ttrajs, dtrajs, bias, lagtimes, unbiased_state=int(0))
its=[[] for m in range(motion)]
pop = []
dG = []
tpm = []
active_set = []
unbiased_model = []
for j in range(len(lagtimes)):
        pop.append(dtram_obj[j].stationary_distribution)
        dG.append(dtram_obj[j].free_energies)
        unbiased_model.append(dtram_obj[j].msm)
        tpm.append(dtram_obj[j].msm.transition_matrix)
        active_set.append(dtram_obj[j].active_set)
        time = dtram_obj[j].msm.timescales(motion)
        for l in range(motion):
                its[l].append(time[l])
np.save('results/count_matrix.npy',dtram_obj.count_matrices)
np.save('results/models.npy',dtram_obj.models)

np.save('results/pop.npy',pop)
np.save('results/dG.npy',dG)
np.save('results/msm.npy',unbiased_model)
np.save('results/its.npy',its)
np.save('results/tpm.npy',tpm)
np.save('results/active_set.npy',active_set)

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
plt.figure()
ns_per_frame = 0.1
for m in range(motion):
        plt.plot(ns_per_frame*lagtimes,[n*ns_per_frame for n in its[m]])
plt.xlabel('lagtime (ns)')
plt.ylabel('implied timescale (ns)')
plt.yscale('log')
plt.savefig('results/ipts.pdf')
plt.close()

