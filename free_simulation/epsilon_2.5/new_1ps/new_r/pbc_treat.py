import sys, os
import mdtraj as md
import numpy as np

for i in range(11,20):
    t = md.load('%d/aligned_%d.xtc'%(i,i),top='new_test.pdb')
    new_t = np.zeros((t.xyz.shape))
    for j in range(t.xyz.shape[0]):
        for k in range(t.xyz.shape[1]):
            for l in range(t.xyz.shape[2]):
                c = t.xyz[j][k][l]
                if c > 3.00859/2.:
                    c - 3.00859/2.
                elif c < -3.00859/2.:
                    c + 3.00859/2.
                else:
                    c = c
                new_t[j][k][l] = c
    np.save('%d/aligned_pbc_treat.npy'%i,new_t)
    #md.save_xtc('%d/aligned_pbc_treat.xtc'%i,new_t)
