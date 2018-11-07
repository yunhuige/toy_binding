import sys, os
import numpy as np


def compute_bias(x1, x2, xi, k):
    """
    Parameters:
    x1    first bias potential position (nm)
    x2    second bias potential position (nm)
    xi    snapshots position (nm)
    k     bias potential (kJ mol^-1 nm^-2)
    """
    b0 = k*0.5*((x1 - xi)**2.)
    b1 = k*0.5*((x2 - xi)**2.)
    return b1 - b0

def compute_bias_with_dhdl(x1, x2, xi, k, du):
    """ 
    Parameters:
    x1    first bias potential position (nm)
    x2    second bias potential position (nm)
    xi    snapshots position (nm)
    k     bias potential (kJ mol^-1 nm^-2)
    du    energy difference between different lambdas from dhdl.xvg file
    """
    b0 = k*0.5*((x1 - xi)**2.)
    b1 = k*0.5*((x2 - xi)**2.)
    return du + b1 - b0

def cluster_bin(traj, xmin, xmax, nbins):
    if type(traj) == str:
        t = np.load(traj).astype(dtype='float64')
    else:
        t = traj
    if not isinstance(t, np.ndarray):
        t = np.array(t)

    dx = (xmax - xmin)/nbins
    edges = np.arange(xmin, xmax+dx, dx)
    ind = ((t - xmin)*nbins/(xmax - xmin)).astype(int)
    ind2 = np.minimum((nbins-1)*np.ones(t.shape,dtype=int),ind)
    ind3 = np.maximum(np.zeros(ind.shape,dtype=int),ind2)
    return ind3
        
def construct_raw_tcm(count_mtx, tau, nstates): 
    if type(count_mtx) == str:
        ctm = np.load(count_mtx)
    else:
        ctm = count_mtx
    if len(ctm.shape) == 1:
        tcm = np.zeros((nstates, nstates))
        for j in range(len(ctm)-tau):
            tcm[ctm[j],ctm[j+tau]]+=1
    else:
        tcm= np.zeros((nstates, nstates))
        for i in range(len(ctm)):
    #        print i
            for j in range(len(ctm[i])-tau):
    #            print j
                tcm[ctm[i][j],ctm[i][j+tau]] += 1
    return tcm

def construct_tpm(raw_tcm):
    if type(raw_tcm) == str:
        tcm = np.load(raw_tcm)
    else:
        tcm = raw_tcm
    transpose = tcm.transpose()
    raw = (tcm + transpose)*0.5
    tpm = np.zeros((tcm.shape[0],tcm.shape[0]))
    for i in range(len(raw)):
        for j in range(len(raw[i])):
            tpm[i,j] = raw[i][j]/sum(raw[i])
    return tpm

def distance2bin(x, pmf_distances):
    """Given an array of pmf distance edges, return the bin index that the distance is closest to."""

    return  np.argsort(np.abs(pmf_distances - x))[0]
