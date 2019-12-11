import sys, os
import numpy as np
from os import path

force1 = np.array([0.0,0.0,0.0,0.0,0.0,0.0])
lamb1 = np.array([0,1,2,3,4,5])
umb1 = np.array([0.0,0.0,0.0,0.0,0.0,0.0])
taus1 = np.load('../round1/tau.npy')



force2 = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
lamb2 = np.array([0,1,2,3,4,5,6,7,8,9,10])
umb2 = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
taus2 = np.load('../round2/tau.npy')
# set-up
temperature = 300.
kB = 1.381e-23 * 6.022e23 / 1000.0 # Boltzmann constant in kJ/mol/K
beta = 1.0 / (kB * temperature) # inverse temperature of simulations (in 1/(kJ/mol))
N_k1=[]
N_k2=[]
ensembles2 = [[10,5,6,7,8,9]]
ensembles1 = [[5,0,1,2,3,4]]
for comb in range(len(ensembles1)):
    ensemble1 = ensembles1[comb]
    ensemble2 = ensembles2[comb]
    ukn1 = [[] for i in range(len(ensemble1))]
    ukn2 = [[] for i in range(len(ensemble2))]
    for ens in range(len(ensemble1)):
        state = ensemble1[ens]
        for ensem in range(len(ensemble1)):
            if ensem == 0:
                dhdl = np.load('../round1/%d/pull/dhdl.npy'%(ensemble1[ensem]))[::1000]
                Nk = 0
                Nk+=len(dhdl)
                for snap in dhdl:
                    ukn1[ens].append(snap[2:][state])
                dhdl = np.load('../round1/%d/push/dhdl.npy'%(ensemble1[ensem]))[::1000]
                Nk+=len(dhdl)
                if ens == 0:
                    N_k1.append(Nk)
                for snap in dhdl:
                    ukn1[ens].append(snap[2:][state])
            else:
                Nk = 0
                tau = taus1[ensemble1[ensem]][0]
                dhdl = np.load('../round1/%d/pull/dhdl.npy'%(ensemble1[ensem]))
                spacing  = min(1000,int(tau))
                for frame in range(0,1000,spacing):
                    Nk+=len(dhdl[frame::1000])
                    for snap in dhdl[frame::1000]:
                        ukn1[ens].append(snap[2:][state])
                tau = taus1[ensemble1[ensem]][1]
                dhdl = np.load('../round1/%d/push/dhdl.npy'%(ensemble1[ensem]))
                spacing  = min(1000,int(tau))
                for frame in range(0,1000,spacing):
                    Nk+=len(dhdl[frame::1000])
                    for snap in dhdl[frame::1000]:
                        ukn1[ens].append(snap[2:][state])
                if ens == 0:
                    N_k1.append(Nk)
    np.save('ukn1.npy',ukn1)
    np.save('Nk1.npy',N_k1)
    for ens in range(len(ensemble2)):
        state = ensemble2[ens]
        for ensem in range(len(ensemble2)):
            if ensem == 0:
                dhdl = np.load('../round2/%d/pull/dhdl.npy'%(ensemble2[ensem]))[::1000]
                Nk = 0
                Nk+=len(dhdl)
                for snap in dhdl:
                    ukn2[ens].append(snap[2:][state])
                dhdl = np.load('../round2/%d/push/dhdl.npy'%(ensemble2[ensem]))[::1000]
                Nk+=len(dhdl)
                if ens == 0:
                    N_k2.append(Nk)
                for snap in dhdl:
                    ukn2[ens].append(snap[2:][state])
            else:
                Nk = 0
                tau = taus2[ensemble2[ensem]][0]
                dhdl = np.load('../round2/%d/pull/dhdl.npy'%(ensemble2[ensem]))
                spacing  = min(1000,int(tau))
                for frame in range(0,1000,spacing):
                    Nk+=len(dhdl[frame::1000])
                    for snap in dhdl[frame::1000]:
                        ukn2[ens].append(snap[2:][state])
                tau = taus2[ensemble2[ensem]][1]
                dhdl = np.load('../round2/%d/push/dhdl.npy'%(ensemble2[ensem]))
                spacing  = min(1000,int(tau))
                for frame in range(0,1000,spacing):
                    Nk+=len(dhdl[frame::1000])
                    for snap in dhdl[frame::1000]:
                        ukn2[ens].append(snap[2:][state])
                if ens == 0:
                    N_k2.append(Nk)

    np.save('ukn2.npy',ukn2)
    np.save('Nk2.npy',N_k2)





