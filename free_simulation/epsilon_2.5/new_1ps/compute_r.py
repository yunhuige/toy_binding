import sys, os
import numpy as np
import mdtraj as md

for i in range(20):
    print 'traj', i
    t=md.load('%d/aligned_%d.xtc'%(i,i),top='%d/protein.gro'%i)
    #print t.xyz[0][11]
    #sys.exit()
    n_frames = t.xyz.shape[0]
    n_atoms = t.xyz.shape[1]
#    r = np.zeros(n_frames)
#    cos_theta = np.zeros(n_frames)
#    cos_phi = np.zeros(n_frames)
#    sin_phi = np.zeros(n_frames)
    spherical = np.zeros((n_frames,4)) # we only need r,cos_theta, cos_phi, sin_phi  for the ligand
    for j in range(n_frames):
        r = np.sqrt(t.xyz[j][11][0]**2.+t.xyz[j][11][1]**2.+t.xyz[j][11][2]**2.)
        cos_theta = t.xyz[j][11][2]/r
        cos_phi = t.xyz[j][11][0]/np.sqrt(t.xyz[j][11][0]**2.+t.xyz[j][11][1]**2.)
        sin_phi = t.xyz[j][11][1]/np.sqrt(t.xyz[j][11][0]**2.+t.xyz[j][11][1]**2.)
        spherical[j][0] = r
        spherical[j][1] = cos_theta
        spherical[j][2] = cos_phi
        spherical[j][3] = sin_phi
    np.save('spher_%d.npy'%i,spherical)
