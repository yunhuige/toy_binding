import sys, os
import numpy as np

stride=10
nstates=10
bias = np.zeros((187,nstates))   # 11*8*2+11
unbias = np.loadtxt('../dataset/frames_%d/mbar_98_sub.dat'%(int(200000./stride)))
for i in range(88):	# 11*8
	pmf = np.loadtxt('../dataset/frames_%d/mbar_%d_sub.dat'%((int(200000./stride)),i))
	for j in range(1,len(pmf)):
		bias[i,j] = pmf[j][1] - unbias[j][1]
		bias[i+88,j] = pmf[j][1] - unbias[j][1]
for i in range(88,99):
	pmf = np.loadtxt('../dataset/frames_%d/mbar_%d_sub.dat'%((int(200000./stride)),i))
        for j in range(1,len(pmf)):
                bias[i+88,j] = pmf[j][1] - unbias[j][1]

np.save('../dataset/frames_%d/bias.npy'%(int(200000./stride)),bias)
