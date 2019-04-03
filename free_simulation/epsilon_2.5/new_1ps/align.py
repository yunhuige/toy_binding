import sys, os
import mdtraj as md

ref = md.load('new_test.pdb')

for i in range(20):
    print i
    t = md.load('%d/gmx_pbc_mol_center.xtc'%i,top='%d/protein.gro'%i)
    t_new = t.superpose(ref)
    t_new.save_xtc('%d/aligned_%d.xtc'%(i,i))
