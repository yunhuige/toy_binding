import sys, os
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
RT  = (1.381e-23 * 6.022e23 / 1000.0) * 300. # in kJ/mol
#stop = [37846, 94096, 28615, 145712, 51180, 169770, 100240, 119159, 125102, 104034, 118115, 51438, 94221, 100668, 58302, 83973, 64626, 101373, 118305, 119165]
#stop = [[764], [1891], [607], [3013], [1113], [3606], [2197], [2392], [2550], [2128], [2424], [2918], [1900], [4381], [3407], [1714], [1342], [2090], [2752], [2831]]
for r in range(20):
        print r
#       os.chdir('RUN%d'%r)
        os.chdir('%d'%r)
        with open('COLVAR','r') as f:
                lines = f.readlines()
        d = [[] for i in range(1)]
        t=[]
        bias = []
        for i in range(len(lines)):
                if lines[i][0] != '#':
                        #print i
                        #t.append(float(lines[i].split()[0]))
			#if float(lines[i].split()[1]) < 0.1:
                        bias.append(np.exp(float(lines[i].split()[2])/RT))
                        #for k in range(1):
                        #        d[k].append(float(lines[i].split()[k+1]))
	np.save('../acc%d.npy'%r,bias)
	os.chdir('../')	
if (0):
        plt.figure()
        acc = []
        for l in range(1,len(bias)+1):
            acc.append(np.mean(bias[:l]))
        acc = np.array(acc)
        for j in range(1):
                plt.plot(t,d[j],label='CV_%d'%j)
                plt.plot(t,acc,label='acc')
        plt.xlabel('time (ps)')
        plt.ylabel('dis (nm)')
        plt.legend(loc='best')
        #plt.ylim(0.0,0.4)
        plt.savefig('../CV_acc.png')
        plt.close()
        os.chdir('../')

