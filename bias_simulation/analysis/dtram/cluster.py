import numpy as np
from tools_box import *
nstates = 10
bin_min = 0.0
bin_max = 0.8

stride = 10

# cluster trajectories based on bin index
print "clustering..."
cm = []
t=np.load('../dataset/frames_%d/distance_sub.npy'%(int(200000./stride)))
for i in range(len(t)):
    print i
    a = cluster_bin(t[i],bin_min,bin_max, nstates)
    cm.append(a)
np.save('../dataset/frames_%d/clustered_matrix.npy'%(int(200000./stride)),cm)
print cm, np.array(cm).shape
print "Done!"
