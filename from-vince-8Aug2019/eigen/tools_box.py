import sys, os
import numpy as np


def construct_raw_tcm(assignment, tau, nstates): 

    # determine if it is a numpy array or a file name to load

    if type(assignment) == str:
        ass = np.load(assignment)
    else:
	ass = assignment
    # check if this is one trajectory or multiple trajectories
    if len(ass) == 1:
        tcm = np.zeros((nstates, nstates))
        for j in range(len(ass)-tau):
            tcm[ass[j],ass[j+tau]]+=1
    else:
        tcm= np.zeros((nstates, nstates)) # make transition count matrix nstates x nstates
        for i in range(len(ass)): #loop through all traj
            if len(ass[i]) > tau:  # check if traj length is longer than the lagtime
                for j in range(len(ass[i])-tau):  # sliding windows
                    tcm[ass[i][j],ass[i][j+tau]] += 1  # add transition count
            else:
                pass
    return tcm

