import sys, os
import numpy as np
from matplotlib import pyplot as plt
a=np.load('tica_eigenvectors.npy')

"""   
** - 1DUM : C9 -- 1DUM : C12 values: -2.08338543124
1DUM : C5 -- 1DUM : C12 values: 1.96019445206
1DUM : C7 -- 1DUM : C12 values: 1.64539809473
1DUM : C1 -- 1DUM : C12 values: 1.49248560684
1DUM : C11 -- 1DUM : C12 values: 1.34631306619
1DUM : C2 -- 1DUM : C12 values: 1.31124034549
* 1DUM : C4 -- 1DUM : C12 values: 0.447154787449
* 1DUM : C8 -- 1DUM : C12 values: 0.214721168248
* 1DUM : C10 -- 1DUM : C12 values: 0.205772044765
* 1DUM : C3 -- 1DUM : C12 values: -0.0612740415702   
* 1DUM : C6 -- 1DUM : C12 values: 0.0217240269125
* = at the lip of the pocket
** = opposite the pocket entrance
"""
color=['green','green','green','green','green','red','green','red','blue','red','green']
label = ['r','cos_theta_r','cos_phi_r','sin_phi_r']
plt.figure( figsize=(6,8) )  # fig size in inches
for i in range(4):
#    value=[]
#    label=[]
#    colors=[]
#    f = open('tIC%d.dat'%(i+1),'r')
#    lines = f.readlines()
#    f.close()
#    for j in range(len(lines)):
#        value.append(lines[j].split()[8])
#        label.append('%s_%s'%(lines[j].split()[2],lines[j].split()[6]))
#    for k in range(len(label)):
#        colors.append(color[int(label[k].split('_')[0][1:])-1])
    plt.subplot(4,1,i+1)
    plt.bar(range(0,4),a[:,i],color=color[i])
    plt.xticks(np.arange(0.5,4.5,1.0),label,rotation=75)
    plt.title('tICA eigenvector $\phi_%d$'%(i+1))
plt.tight_layout()
#plt.show()
plt.savefig('eigenvectors_yunhui.pdf')
