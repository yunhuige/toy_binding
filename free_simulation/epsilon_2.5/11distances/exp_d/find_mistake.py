import numpy as np
a=np.load('tica.npy')
for i in range(len(a)):
	for j in range(len(a[i])):
		#if (a[i][j][0] > 0.0) and (a[i][j][0]<0.05):
                if (a[i][j][0] < 0.0) and (a[i][j][0]>-0.1):
                    print 'traj', i, 'frame', j
		    break
