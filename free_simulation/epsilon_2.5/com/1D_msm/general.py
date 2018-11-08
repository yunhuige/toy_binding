import sys, os
import numpy as np
from numpy.linalg import eig
from tools_box import *
from estimators import *

nstates = 100
bin_min = 0.0 
bin_max = 0.8
# cluster trajectories based on bin index
if (1):
    print "clustering..."
    cm = []
    for i in range(20):
        t = np.load('../distance_%d.npy'%i)
        print i
        a = cluster_bin(t,bin_min,bin_max, nstates)
        cm.append(a)
    cm = np.array(cm)
    np.save('clustered_matrix.npy',cm)
    print cm, np.array(cm).shape
    print "Done!"

# bootstrap trajectories


fout = open('implied_timescales.dat','w')
header = '# tau(ns)\tround\timplied_timescale(ns)'
#print header
fout.write(header+'\n')

# construct raw transition count matrix
bootstrap = True
r = 2
sm = 4
#cm = np.load('new_clustered_matrix.npy')
if (1):
    if bootstrap:
        for i in range(r):
            new_cm = []
            traj = np.random.choice(cm.shape[0],cm.shape[0])
            print traj
            for j in traj:
                new_cm.append(cm[j])
            new_cm = np.array(new_cm)
    
            print "constructing transition count matrix..."
        #    tau_values = [2,5,10,25,50,100,250,500,1000,2000]
        #    tau_values = [2,5]
            tau_values = [1,10,100,150,200,300,400,500,600,1000,1500,2000,2500,3000]
            for tau in tau_values:
                tau_in_ns = tau*0.1
                print "lagtime = ", tau_in_ns,'ns'
                tcm = construct_raw_tcm(new_cm,tau,nstates)
                tcm[tcm==0.] = 1.   # add pseudocount if there is any zero count
                np.save('raw_tcm_tau%d_r%d.npy'%(tau,i),tcm)
                # construct transition probability matrix
                print "constructing transition probability matrix..."
#                tpm = construct_tpm(tcm)
                tpm = MLE_tProb_reversible(tcm)
                np.save('tpm_%d.npy'%tau,tpm)
                print "computing eigenvalues and eigenvectors..."
                try:
                    mu, eigenvectors = eig(tpm.transpose())
                    #print "mu", mu, "eigenvectors",eigenvectors
                    for j in range(sm):
                        implied_timescale_in_ns = -1.0*tau_in_ns/np.log(mu[j+1])
                        outstr = '%6.3f\t%d\t%6.3f'%(tau_in_ns, i, implied_timescale_in_ns)
                        fout.write(outstr+'\n')
                except:
                    'Skipped'
                #fout.write(outstr+'\n')
        fout.close()
    else:
        k = 1
        print "constructing transition count matrix..."
    #    tau_values = [2,5,10,25,50,100,250,500,1000,2000]
    #    tau_values = [2,5]
        tau_values = [1,10,100,150,200,300,400,500,600,1000,1500,2000,2500,3000]
        for tau in tau_values:
            tau_in_ns = tau*0.1
            print "lagtime = ", tau_in_ns,'ns'
            cm = 'clustered_matrix.npy'
            tcm = construct_raw_tcm(cm,tau,nstates)
            np.save('raw_tcm_%d.npy'%tau,tcm)
            # construct transition probability matrix
            print "constructing transition probability matrix..."
#            tpm = construct_tpm(tcm)
            tpm = MLE_tProb_reversible(tcm)
            np.save('tpm_%d.npy'%tau,tpm)
            print "computing eigenvalues and eigenvectors..."
            try:
                mu, eigenvectors = eig(tpm.transpose())
              #  print "mu", mu, "eigenvectors",eigenvectors
                for j in range(sm):
                    implied_timescale_in_ns = -1.0*tau_in_ns/np.log(mu[j+1])
                    outstr = '%6.3f\t%d\t%6.3f'%(tau_in_ns, k, implied_timescale_in_ns)
                    fout.write(outstr+'\n')
            except:
                'Skipped'
            #fout.write(outstr+'\n')
        fout.close()

#sys.exit()
# plot implied timescales
print "plotting figures..."
from matplotlib import pyplot as plt


color=['red','blue','green','magenta']
if bootstrap:
    data = np.loadtxt('implied_timescales.dat')
    tau_values = [1,10,100,150,200,300,400,500,600,1000,1500,2000,2500,3000]
    lagtime=[[] for i in range(sm)]
    implied=[[] for i in range(sm)]
    err=[[] for i in range(sm)]
    for j in range(sm):
        for i in range(len(tau_values)):
            lagtime[j].append(data[(j+i*sm)::len(tau_values)*sm][0][0])
            implied[j].append(np.mean(data[(j+i*sm)::len(tau_values)*sm][::,2]))
            err[j].append(np.std(data[(j+i*sm)::len(tau_values)*sm][::,2]))

    for i in range(sm):
        plt.plot(lagtime[i],implied[i],color=color[i])
        plt.fill_between(lagtime[i],np.array(implied[i])+np.array(err[i]),np.array(implied[i])-np.array(err[i]),color=color[i],alpha=0.2)
        plt.yscale('log')
        plt.xlabel('lag time (ns)')
        plt.ylabel('implied timescale (ns)')
        plt.savefig('implied_timescale.pdf')
    print 'Done!'

else:
    data = np.loadtxt('implied_timescales.dat')
    lagtime=[[] for i in range(sm)]
    implied=[[] for i in range(sm)]
    err=[[] for i in range(sm)]
    for j in range(sm):
        for i in range(len(tau_values)):
            lagtime[j].append(data[(j+i*sm)::len(tau_values)*sm][0][0])
            implied[j].append(np.mean(data[(j+i*sm)::len(tau_values)*sm][::,2]))
            err[j].append(np.std(data[(j+i*sm)::len(tau_values)*sm][::,2]))

    for i in range(sm):
        plt.plot(lagtime[i],implied[i],color=color[i])
        plt.yscale('log')
        plt.xlabel('lag time (ns)')
        plt.ylabel('implied timescale (ns)')
        plt.savefig('implied_timescale.pdf')
    print 'Done!'


