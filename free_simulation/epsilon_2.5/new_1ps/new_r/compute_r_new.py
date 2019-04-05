import sys, os
import numpy as np

for i in range(20):
    print 'traj', i
    xyz = np.load('%d/aligned_pbc_treat.npy'%i)
    n_frames = xyz.shape[0]
    spherical = np.zeros((n_frames,4)) # we only need r,cos_theta, cos_phi, sin_phi  for the ligand
    for j in range(n_frames):
        if xyz[j][11][0] == 0. and xyz[j][11][1] == 0. and xyz[j][11][2] == 0.:
            r = 0.
            cos_theta_r = 0.
            cos_phi_r = 0.
            sin_phi_r = 0.
        else:
            r = np.sqrt(xyz[j][11][0]**2.+xyz[j][11][1]**2.+xyz[j][11][2]**2.)
            if xyz[j][11][0] == 0. and xyz[j][11][1]==0.:
                if xyz[j][11][2] >= 0.:
                    cos_theta = 1.
                else:
                    cos_theta = -1.
            else:
                cos_theta = xyz[j][11][2]/r

            if xyz[j][11][1] == 0.:
                if xyz[j][11][0] > 0.:
                    cos_phi = 1.
                    sin_phi = 0.
                elif xyz[j][11][0] < 0.:
                    cos_phi = -1.
                    sin_phi = 0.
            elif xyz[j][11][0] == 0.:
                if xyz[j][11][1] > 0.:
                    cos_phi = 0.
                    sin_phi = 1.
                elif xyz[j][11][1] < 0.:
                    cos_phi = 0.
                    sin_phi = -1.
            else:
                cos_phi = xyz[j][11][0]/np.sqrt(xyz[j][11][0]**2.+xyz[j][11][1]**2.)
                sin_phi = xyz[j][11][1]/np.sqrt(xyz[j][11][0]**2.+xyz[j][11][1]**2.)
            if r < 3.00859/2.:
                cos_theta_r = (3.00859/2. - r)*cos_theta
                cos_phi_r = (3.00859/2. - r)*cos_phi
                sin_phi_r = (3.00859/2. - r)*sin_phi
            elif r >= 3.00859/2.:
                cos_theta_r = 0.*cos_theta
                cos_phi_r = 0.*cos_phi
                sin_phi_r = 0.*sin_phi
        spherical[j][0] = r
        spherical[j][1] = cos_theta_r
        spherical[j][2] = cos_phi_r
        spherical[j][3] = sin_phi_r
    np.save('new_r/spher_%d.npy'%i,spherical)
