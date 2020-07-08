import os, sys
import numpy as np
from os import path
#from math import *
import pymbar # multistate Bennett acceptance ratio
from pymbar import timeseries # timeseries analysis
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
######## Functions #############
def plotOverlapMatrix(O,K,):
    """Plots the probability of observing a sample from state i (row) in state j (column).
      For convenience, the neigboring state cells are fringed in bold."""
    max_prob = O.max()
    fig = plt.figure(figsize=(K/2.,K/2.))
    fig.add_subplot(111, frameon=False, xticks=[], yticks=[])

    for i in range(K):
       if i!=0:
          plt.axvline(x=i, ls='-', lw=0.5, color='k', alpha=0.25)
          plt.axhline(y=i, ls='-', lw=0.5, color='k', alpha=0.25)
       for j in range(K):
          if O[j,i] < 0.005:
             ii = ''
          elif O[j,i] > 0.995:
             ii = '1.00'
          else:
             ii = ("%.2f" % O[j,i])[1:]
          alf = O[j,i]/max_prob
          plt.fill_between([i,i+1], [K-j,K-j], [K-(j+1),K-(j+1)], color='k', alpha=alf)
          plt.annotate(ii, xy=(i,j), xytext=(i+0.5,K-(j+0.5)), size=8, textcoords='data', va='center', ha='center', color=('k' if alf < 0.5 else 'w'))

    ks = range(K)
    for i in range(K):
       plt.annotate(ks[i], xy=(i+0.5, 1), xytext=(i+0.5, K+0.5), size=10, textcoords=('data', 'data'), va='center', ha='center', color='k')
       plt.annotate(ks[i], xy=(-0.5, K-(j+0.5)), xytext=(-0.5, K-(i+0.5)), size=10, textcoords=('data', 'data'), va='center', ha='center', color='k')
    plt.annotate('$umb$', xy=(-0.5, K-(j+0.5)), xytext=(-0.5, K+0.5), size=10, textcoords=('data', 'data'), va='center', ha='center', color='k')
    plt.plot([0,K], [0,0], 'k-', lw=4.0, solid_capstyle='butt')
    plt.plot([K,K], [0,K], 'k-', lw=4.0, solid_capstyle='butt')
    plt.plot([0,0], [0,K], 'k-', lw=2.0, solid_capstyle='butt')
    plt.plot([0,K], [K,K], 'k-', lw=2.0, solid_capstyle='butt')

    cx = sorted(2*range(K+1))
    cy = sorted(2*range(K+1), reverse=True)
    plt.plot(cx[2:-1], cy[1:-2], 'k-', lw=2.0)
    plt.plot(np.array(cx[2:-3])+1, cy[1:-4], 'k-', lw=2.0)
    plt.plot(cx[1:-2], np.array(cy[:-3])-1, 'k-', lw=2.0)
    plt.plot(cx[1:-4], np.array(cy[:-5])-2, 'k-', lw=2.0)

    plt.xlim(-1, K)
    plt.ylim(0, K+1)
#    plt.savefig(os.path.join(P.output_directory, 'O_MBAR.pdf'), bbox_inches='tight', pad_inches=0.0)
    plt.savefig('O_MBAR1.pdf', bbox_inches='tight', pad_inches=0.0)
    plt.close(fig)
    return

N_k = np.load('Nk1.npy')
u_kln = np.load('ukn1.npy')
K = len(u_kln)
print "Running MBAR..."
mbar = pymbar.MBAR(u_kln, N_k, verbose = True)
overlap = mbar.computeOverlap()[2]
np.save('overlap1.npy',overlap)
plotOverlapMatrix(overlap,K)



