import sys, os
import numpy as np
ukn=np.load('u_kn.npy')
distance=np.load('distance_sub.npy')
new_ukn=[]
new_distance=[]
for i in range(88):
    a=np.concatenate((ukn[i],ukn[i+88]))
    new_ukn.append(a)
#    b=np.concatenate((distance[i],distance[i+88]))
#    new_distance.append(b)
for i in range(176,187):
    a=np.concatenate((ukn[i],ukn[i]))
    new_ukn.append(a)
#    b=np.concatenate((distance[i],distance[i]))
#    new_distance.append(b)
for i in range(2):
    for j in range(len(distance)):
        new_distance.append(distance[j])
np.save('new_ukn.npy',new_ukn)
np.save('new_distance.npy',new_distance)

