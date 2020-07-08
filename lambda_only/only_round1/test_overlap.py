import sys, os
import numpy as np
from matplotlib import pyplot as plt

def O_KL(N1,N2,pop1,pop2,P1,P2):
    if N1 == 0 or N2 == 0 or pop1 ==0 or pop2 == 0 or P1 == 0 or P2 == 0:
        return 0
    else:
        return N1*pop1*pop2*P1*P2/(N1*pop1*P1 + N2*pop2*P2)

n_states = 18

VERBOSE = False

lambdas = np.arange(0.5,1.0,0.1)
for data in range(1,6):
    overlap = [[],[],[],[]]
#    overlap = np.zeros((2,2))
    for r in range(10):
#        print 'round', r
        os.chdir('cumu%d_sub/0/100/results'%(data))
        models = np.load('models.npy')
        common_active_set = np.intersect1d(models[0].active_set,models[1].active_set)
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
        overlap11 = 0
        for i in range(len(common_active_set)):
            for j in range(len(common_active_set)):
                if VERBOSE:
                    print '    i,j =', i,j, N1,N2,pop1[i],pop1[i],P1[i][j],P1[i][j], 'overlap:', tmp
                if N1*pop1[i]*P1[i][j]+N2*pop2[i]*P2[i][j] == 0:
                    overlap11 += 0.
                else:
                    overlap11 += N1*pop1[i]*P1[i][j]*pop1[i]*P1[i][j]/(N1*pop1[i]*P1[i][j]+N2*pop2[i]*P2[i][j])
        overlap[0].append(overlap11)


        overlap12 = 0
        for i in range(len(common_active_set)):
            for j in range(len(common_active_set)):
                if VERBOSE:
                    print '    i,j =', i,j, N1,N2,pop1[i],pop2[i],P1[i][j],P2[i][j], 'overlap:', tmp
                overlap12 += O_KL(N1,N2,pop1[i],pop2[i],P1[i][j],P2[i][j])
        overlap[1].append(overlap12)

        overlap21 = 0
        for i in range(len(common_active_set)):
            for j in range(len(common_active_set)):
                if VERBOSE:
                    print '    i,j =', i,j, N2,N1,pop2[i],pop1[i],P2[i][j],P1[i][j], 'overlap:', tmp
                overlap21 += O_KL(N2,N1,pop2[i],pop1[i],P2[i][j],P1[i][j])
        overlap[2].append(overlap21)

        overlap22 = 0
        for i in range(len(common_active_set)):
            for j in range(len(common_active_set)):
                #tmp = O_KL(N1,N2,pop1[i],pop2[i],P1[i][j],P2[i][j])
                if VERBOSE:
                    print '    i,j =', i,j, N2,N2,pop2[i],pop2[i],P2[i][j],P2[i][j], 'overlap:', tmp
                if N1*pop1[i]*P1[i][j]+N2*pop2[i]*P2[i][j] == 0:
                    overlap22 += 0.
                else:
                    overlap22 += N2*pop2[i]*P2[i][j]*pop2[i]*P2[i][j]/(N1*pop1[i]*P1[i][j]+N2*pop2[i]*P2[i][j])
        overlap[3].append(overlap22)


        os.chdir('../../../../')
        if VERBOSE:
            print 'overlap11', overlap11, 'overlap12', overlap12,'overlap21', overlap21,'overlap22', overlap22,
            print 'overlap11+overlap12',overlap11+overlap12, 'overlap21+overlap22', overlap21+overlap22
#    print 'data: lambda=1.0 lambda=', lambdas[data-1], 'overlap', np.mean(overlap,axis=1)
    overlap_mtx = np.zeros((2,2))
    overlap_mtx[0,0]=np.mean(overlap,axis=1)[0]
    overlap_mtx[0,1]=np.mean(overlap,axis=1)[1]
    overlap_mtx[1,0]=np.mean(overlap,axis=1)[2]
    overlap_mtx[1,1]=np.mean(overlap,axis=1)[3]
    plt.figure(figsize=(12,10))
    cmap=plt.get_cmap('Blues')
    plt.pcolor(overlap_mtx,cmap=cmap,vmin=0.0,vmax=1.0,edgecolors='none')
    plt.colorbar()
    plt.annotate("%.3f"%overlap_mtx[0,0],xy=(0.4,0.5),fontsize=10,color='black',weight='bold')
    plt.annotate("%.3f"%overlap_mtx[0,1],xy=(1.4,0.5),fontsize=10,color='black',weight='bold')
    plt.annotate("%.3f"%overlap_mtx[1,0],xy=(0.4,1.5),fontsize=10,color='black',weight='bold')
    plt.annotate("%.3f"%overlap_mtx[1,1],xy=(1.4,1.5),fontsize=10,color='black',weight='bold')
    plt.xticks([0.5,1.5],['lambda=1.0','lambda=%s'%lambdas[data-1]],fontsize=12)
    plt.yticks([0.5,1.5],['lambda=1.0','lambda=%s'%lambdas[data-1]],fontsize=12)
    plt.savefig('overlap_cumu%d.pdf'%data)
    plt.close()


#    print np.mean(overlap,axis=1)
#    print 'data: lambda=1.0 lambda=', lambdas[data-1] , 'overlap11', np.mean(overlap[0]), 'overlap12', np.mean(overlap[1]), 'overlap21', np.mean(overlap[2]),'overlap22', np.mean(overlap[3]),'sum (off/diag)', (np.mean(overlap[1])+np.mean(overlap[3]))/((np.mean(overlap[0])+np.mean(overlap[2])))
#    print 'sum (off/diag) normalized', (np.mean(overlap[1])/(np.mean(overlap[0])+np.mean(overlap[1]))+np.mean(overlap[3])/(np.mean(overlap[2])+np.mean(overlap[3])))/((np.mean(overlap[0])/(np.mean(overlap[0])+np.mean(overlap[1]))+np.mean(overlap[2])/(np.mean(overlap[2])+np.mean(overlap[3]))))
