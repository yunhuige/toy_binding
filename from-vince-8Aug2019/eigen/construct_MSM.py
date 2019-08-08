import sys ,os
import numpy as np
from numpy.linalg import eig
from tools_box import *
from estimators import *


new_ass = np.load('Assignment.npy')
nstates = 18

# create implied timescale files
fout = open('implied_timescales.dat','w')
header = '# tau(ns)\tround\tmotion\timplied_timescale(ns)'

#print header
fout.write(header+'\n')

# construct raw transition count matrix
bootstrap = True
r = 1   # 1 rounds of bootstrapping
sm = 4  # 4 slow motions to compute

if bootstrap:
    for i in range(r):
        new_cm = []
        traj = np.random.choice(len(new_ass),len(new_ass))   # randomly pick up trajectories (sample with replacement)
        for j in traj:
            new_cm.append(new_ass[j])
        new_cm = np.array(new_cm) # make this new matrix in numpy array format
        print "constructing transition count matrix..."
        tau_values = [1,10,200,500,1000,2000,3000,5000,7000,8000,10000,15000,20000,40000,60000,80000,100000,200000,300000,400000,500000,600000]  # lagtimes
        for tau in tau_values:
            tau_in_ns = tau*0.001   # tau is in unit of ns
            print "lagtime = ", tau_in_ns,'ns'
            tcm = construct_raw_tcm(new_cm,tau,nstates)  # construct transition count matrix based on tau
            np.save('tcm_%d_%d.npy'%(i,tau),tcm)
            # construct transition probability matrix
            print "constructing transition probability matrix..."
            tpm = MLE_tProb_reversible(tcm)    # using MLE estimators
            print "computing eigenvalues and eigenvectors..."
            try:
                    mu, eigenvectors = eig(tpm.transpose())    # compute eigenvalues and eigenvectors
                    print "mu", mu, "eigenvectors",eigenvectors
                    np.save('mu_%d_%d.npy'%(i,tau),mu)
                    for m in range(sm):
                        implied_timescale_in_ns = -1.0*tau_in_ns/np.log(mu[m+1])
                        outstr = '%6.3f\t%d\t%d\t%6.3f'%(tau_in_ns, i, m, implied_timescale_in_ns)  # implied timescales for specific tau for ith round bootstrap
                        print 'writing data...'
                        fout.write(outstr+'\n')
#                    sys.exit()
            except:
                    'Skipped'
                #fout.write(outstr+'\n')
#            sys.exit()
    print "Done!"
    fout.close()
