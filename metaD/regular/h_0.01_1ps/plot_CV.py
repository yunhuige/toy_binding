import sys, os
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
for r in range(20):
        print r
#       os.chdir('RUN%d'%r)
        os.chdir('%d'%r)
        with open('COLVAR','r') as f:
                lines = f.readlines()
        d = [[] for i in range(1)]
        t=[]
        for i in range(1,len(lines)-1):
                if lines[i][0] != '#':
                        #print i
                        t.append(float(lines[i].split()[0]))
                        for k in range(1):
                                d[k].append(float(lines[i].split()[k+1]))
        plt.figure()
        for j in range(1):
                plt.plot(t,d[j],label='CV_%d'%j)
        plt.xlabel('time (ps)')
        plt.ylabel('dis (nm)')
        plt.legend(loc='best')
        plt.savefig('../CV_%d.png'%r)
        plt.close()
        os.chdir('../')

