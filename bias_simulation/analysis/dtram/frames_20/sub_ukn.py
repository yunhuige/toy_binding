import sys, os
import numpy as np

ukn=np.load('u_kn.npy')
dis=np.load('distance_sub.npy')
new_ukn=[]
new_dis=[]
for i in range(88):
    new_ukn.append(ukn[i])
    new_dis.append(dis[i])
for i in range(176,187):
    new_ukn.append(ukn[i])
    new_dis.append(dis[i])
np.save('sub_ukn.npy',new_ukn)
np.save('sub_dis.npy',new_dis)
