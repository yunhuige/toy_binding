import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm


#tica_transformed = np.load('tica_2a.npy')
#tica_transformed = np.concatenate(tica_transformed) 
a=np.load('tica1.npy')

#a=np.concatenate(a)
print len(a)
b=np.load('tica2.npy')
#b=np.concatenate(b)
c=np.load('cluster_centers.npy')
d=[]
e=[]
for i in range(len(c)):
        d.append(c[i][0])
        e.append(c[i][1])

plt.figure()
plt.hist2d(a,b,bins=300,norm=LogNorm())
#plt.hist2d(tica_transformed[:,0],tica_transformed[:,1],bins=300,norm=LogNorm())
#plt.xlim(-3.5,1.5)
#plt.ylim(-1.8,2.5)
plt.xlim(-2.8,1.0)
plt.ylim(-4.0,3.0)
plt.xlabel("tIC1")
plt.ylabel("tIC2")
for i in range(len(c)):
        plt.plot(d[i],e[i],"o",color='red')
        plt.annotate('%s'%i,xy=(d[i],e[i]),fontsize=7)

#plt.xlim(-1.0,2.0)
#plt.ylim(-4.0,9.0)
#plt.title("tICA Heatmap 13733")
plt.savefig("tica1v2_cluster.pdf")
plt.show()
#plt.savefig("tica1v2_plot.pdf")

