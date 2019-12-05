import sys, os
import numpy as np
from matplotlib import pyplot as plt

def O_KL(N1,N2,pop1,pop2,P1,P2):
    if N1 == 0 or N2 == 0 or pop1 ==0 or pop2 == 0 or P1 == 0 or P2 == 0:
        return 0
    else:
        return N1*pop1*pop2*P1*P2/(N1*pop1*P1 + N2*pop2*P2)

n_ensembles = 11
n_states = 18

VERBOSE = False

lambdas = np.arange(0.0,1.0,0.1)
for data in range(1,11):
    os.chdir('cumu%d/100/results'%data)
    models = np.load('models.npy')
    common_active_set = np.intersect1d(models[0].active_set,models[1].active_set)
    pop1 = models[0].pi[common_active_set]
    pop2 = models[1].pi[common_active_set]
    ind1 = []
    ind2 = []
    for state in common_active_set:
        ind1.append(np.where(models[0].active_set == state)[0][0])
        ind2.append(np.where(models[1].active_set == state)[0][0])
    P1 = models[0].P[ind1]
    P2 = models[1].P[ind2]
#    np.save('../../../test.npy', P1)
    ttraj = np.load('../ttraj.npy')
    ttraj = np.concatenate(ttraj)
    N = np.bincount(ttraj)
    N1 = N[0]
    N2 = N[1]
    print 'Calculating O_12'
    overlap1 = 0
    for i in range(len(common_active_set)):
        for j in range(len(common_active_set)):
            tmp = O_KL(N1,N2,pop1[i],pop2[i],P1[i][j],P2[i][j])
            if VERBOSE:
                print '    i,j =', i,j, N1,N2,pop1[i],pop2[i],P1[i][j],P2[i][j], 'overlap:', tmp
            overlap1 += O_KL(N1,N2,pop1[i],pop2[i],P1[i][j],P2[i][j])

    print 'Calculating O_21'
    overlap2 = 0
    for i in range(len(common_active_set)):
        for j in range(len(common_active_set)):
            tmp = O_KL(N2,N1,pop1[i],pop2[i],P1[i][j],P2[i][j])
            if VERBOSE:
                print '    i,j =', i,j, N1,N2,pop1[i],pop2[i],P1[i][j],P2[i][j], 'overlap:', tmp
            overlap2 += tmp


    print 'data: lambda=1.0 lambda=', lambdas[data-1] , 'overlap1', overlap1, 'overlap2', overlap2, 'sum', overlap1+overlap2
    os.chdir('../../../')




