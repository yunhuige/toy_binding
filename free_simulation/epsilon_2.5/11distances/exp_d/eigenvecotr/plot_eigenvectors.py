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

# Make bar plots of the eigenvectors color-coded
# by the type pocket atom

plt.figure( figsize=(6,8) )  # fig size in inches

for i in range(0,4):
    panel = i+1
    plt.subplot(4, 1, panel)
    plt.bar([0], a[0,i], label='opposite e', color='blue')
    plt.bar(range(1,6), a[1:6,i], label='backrow', color='g')
    plt.bar(range(6,11), a[6:11,i], label='lip', color='r')

    plt.title('tICA eigenvector $\phi_%d$'%i)
plt.tight_layout()

#plt.show()
plt.savefig('plot_eigenvectors.pdf')

