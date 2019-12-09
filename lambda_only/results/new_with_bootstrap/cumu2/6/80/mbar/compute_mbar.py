import sys, os
import numpy as np
from pyemma.thermo import tram
from pyemma import msm
import pyemma
from pyemma.thermo import mbar

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
#	dtrajs.append(new_ass[i])
#print isinstance(dtrajs, (list, tuple))
#print isinstance(dtrajs, (list, tuple)) and (all(isinstance(s, string_types) for s in dtrajs))
#print isinstance(dtrajs, np.ndarray)
      #  if l.ndim == 1 and (l.dtype.kind == 'i' or l.dtype.kind == 'u'):
#print dtrajs.ndim == 1 and (dtrajs.dtype.kind == 'i' or dtrajs.dtype.kind == 'u')      
#sys.exit()

bias = np.load('../bias_tram.npy',allow_pickle=True)

mbar_obj = mbar(ttrajs, dtrajs, bias)
np.save('stationary_distribution.npy', mbar_obj.stationary_distribution)
np.save('active_set.npy', mbar_obj.active_set)
np.save('free_energies.npy', mbar_obj.free_energies)
sys.exit()
lagtimes = np.array([1,5,10,15,30,100,150,200,300,600,1000,1500,2000,2500])
motion = 4
tram_obj = tram(ttrajs, dtrajs, bias, lagtimes, unbiased_state=int(0))
its=[[] for m in range(motion)]
pop = []
dG = []
unbiased_model = []
for j in range(len(lagtimes)):
	pop.append(tram_obj[j].stationary_distribution)
	dG.append(tram_obj[j].free_energies)
	unbiased_model.append(tram_obj[j].msm)
	time = tram_obj[j].msm.timescales(motion)
	for l in range(motion):
		its[l].append(time[l])
np.save('results/pop.npy',pop)
np.save('results/dG.npy',dG)
np.save('results/msm.npy',unbiased_model)
np.save('results/its.npy',its)


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

