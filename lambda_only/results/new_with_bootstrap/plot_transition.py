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

lambdas = np.arange(0.5,1.0,0.1)
for data in range(1,2):
    P_mtx1 = []
    P_mtx2 = []
    all_P1 = []
    all_P2 = []
    all_pop1 = []
    all_pop2 = []
#    overlap = [[],[],[],[]]
#    overlap = np.zeros((2,2))
    for r in range(1):

#        print 'round', r
        os.chdir('cumu%d/%d/90/results'%(data,r))
        models = np.load('models.npy')
        common_active_set = np.intersect1d(models[0].active_set,models[1].active_set)
        P1_mtx = np.zeros((len(common_active_set),len(common_active_set)))
        P2_mtx = np.zeros((len(common_active_set),len(common_active_set)))

#        print 'common_active_set', common_active_set
        pop1 = models[0].pi[common_active_set]
        if pop1.sum() != 1.0:
            pop1 = pop1/pop1.sum()
#        np.save('test_pop1.npy',pop1)
        pop2 = models[1].pi[common_active_set]
#        np.save('test2_pop2.npy',pop2)
        if pop2.sum() != 1.0:
            pop2 = pop2/pop2.sum()
#        np.save('test_pop2.npy',pop2)
        ind1 = []
        ind2 = []
        for state in common_active_set:
            ind1.append(np.where(models[0].active_set == state)[0][0])
            ind2.append(np.where(models[1].active_set == state)[0][0])
        P_1 = np.zeros((len(common_active_set),len(common_active_set)))
        P_2 = np.zeros((len(common_active_set),len(common_active_set)))
#        print 'ind1', ind1, 'ind2', ind2
        for i in range(len(ind1)):
            for j in range(len(ind1)):
                P_1[i,j] = models[0].P[ind1[i],ind1[j]]
        for i in range(len(ind2)):
            for j in range(len(ind2)):
                P_2[i,j] = models[1].P[ind2[i],ind2[j]]
        norm_P1 = P_1/P_1.sum(axis=1,keepdims=True)
        norm_P2 = P_2/P_2.sum(axis=1,keepdims=True)
        P1 = np.nan_to_num(norm_P1)
        P2 = np.nan_to_num(norm_P2)
#        np.save('test_P1.npy',P1)
#        np.save('test_P2.npy',P2)
        if P1.sum(axis=1).any() not in[0.0,1.0]:
            print 'P1 is not row normalized to 1'
            exit()

        elif P2.sum(axis=1).any() not in [0.0,1.0]:
            print 'P2 is not row normalized to 1'
            exit()

        ttraj = np.load('../ttraj.npy')
        ttraj = np.concatenate(ttraj)
        N = np.bincount(ttraj)
        N1 = N[0]
        N2 = N[1]
        #print 'N1', N1, 'N2', N2
        for i in range(len(common_active_set)):
            for j in range(len(common_active_set)):
                P1_mtx[i,j] = pop1[i]*P1[i][j]
                P2_mtx[i,j] = pop2[i]*P2[i][j]
        P_mtx1.append(P1_mtx)
        P_mtx2.append(P2_mtx)
        all_P1.append(P1)
        all_P2.append(P2)
        all_pop1.append(pop1)
        all_pop2.append(pop2)
        os.chdir('../../../../')
    #print all_pop1
    plt.figure(figsize=(12,10))
    cmap=plt.get_cmap('Blues')
#    print 'P_mtx1',P_mtx1[0].view(type=np.matrix)
#    plt.pcolor(np.mean(P_mtx1,axis=2).T,cmap=cmap,vmin=0.0,vmax=1.0,edgecolors='none')
    plt.pcolor(P_mtx1[0],cmap=cmap,vmin=0.0,vmax=1.0,edgecolors='none')
    plt.colorbar()
    plt.xticks(np.arange(0.5,0.5+len(common_active_set)*1.0,1.0),common_active_set,fontsize=12)
    plt.yticks(np.arange(0.5,0.5+len(common_active_set)*1.0,1.0),common_active_set,fontsize=12)
    plt.savefig('P1_pi_cumu%d.pdf'%data)
    plt.close()

    plt.figure(figsize=(12,10))
    cmap=plt.get_cmap('Blues')
#    plt.pcolor(np.mean(P_mtx2,axis=2).T,cmap=cmap,vmin=0.0,vmax=1.0,edgecolors='none')
    plt.pcolor(P_mtx2[0],cmap=cmap,vmin=0.0,vmax=1.0,edgecolors='none')
    plt.colorbar()
    plt.xticks(np.arange(0.5,0.5+len(common_active_set)*1.0,1.0),common_active_set,fontsize=12)
    plt.yticks(np.arange(0.5,0.5+len(common_active_set)*1.0,1.0),common_active_set,fontsize=12)
    plt.savefig('P2_pi_cumu%d.pdf'%data)
    plt.close()

    plt.figure(figsize=(12,10))
    cmap=plt.get_cmap('Blues')
#    plt.pcolor(np.mean(all_P1,axis=2).T,cmap=cmap,vmin=0.0,vmax=1.0,edgecolors='none')
    plt.pcolor(all_P1[0],cmap=cmap,vmin=0.0,vmax=1.0,edgecolors='none')
    plt.colorbar()
    plt.xticks(np.arange(0.5,0.5+len(common_active_set)*1.0,1.0),common_active_set,fontsize=12)
    plt.yticks(np.arange(0.5,0.5+len(common_active_set)*1.0,1.0),common_active_set,fontsize=12)
    plt.savefig('P1_cumu%d.pdf'%data)
    plt.close()
    plt.figure(figsize=(12,10))
    cmap=plt.get_cmap('Blues')
#    plt.pcolor(np.mean(all_P2,axis=2).T,cmap=cmap,vmin=0.0,vmax=1.0,edgecolors='none')
    plt.pcolor(all_P2[0],cmap=cmap,vmin=0.0,vmax=1.0,edgecolors='none')
    plt.colorbar()
    plt.xticks(np.arange(0.5,0.5+len(common_active_set)*1.0,1.0),common_active_set,fontsize=12)
    plt.yticks(np.arange(0.5,0.5+len(common_active_set)*1.0,1.0),common_active_set,fontsize=12)
    plt.savefig('P2_cumu%d.pdf'%data)
    plt.close()

    plt.figure(figsize=(12,10))
#    cmap=plt.get_cmap('Blues')
#    plt.pcolor(all_pop1[0],cmap=cmap,vmin=0.0,vmax=1.0,edgecolors='none')
#    plt.colorbar()
    plt.bar(np.arange(0.5,0.5+len(common_active_set)*1.0,1.0),all_pop1[0])
    plt.xticks(np.arange(0.75,0.75+len(common_active_set)*1.0,1.0),common_active_set,fontsize=12)
#    plt.yticks(np.arange(0.5,0.5+len(common_active_set)*1.0,1.0),common_active_set,fontsize=12)
    plt.savefig('pi1_cumu%d.pdf'%data)
    plt.close()

    plt.figure(figsize=(12,10))
#    cmap=plt.get_cmap('Blues')
#    plt.pcolor(all_pop2[0],cmap=cmap,vmin=0.0,vmax=1.0,edgecolors='none')
#    plt.colorbar()
    plt.bar(np.arange(0.5,0.5+len(common_active_set)*1.0,1.0),all_pop2[0])
    plt.xticks(np.arange(0.75,0.75+len(common_active_set)*1.0,1.0),common_active_set,fontsize=12)
#    plt.yticks(np.arange(0.5,0.5+len(common_active_set)*1.0,1.0),common_active_set,fontsize=12)
    plt.savefig('pi2_cumu%d.pdf'%data)
    plt.close()

