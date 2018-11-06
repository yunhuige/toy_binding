import sys, os
import numpy as np

umbrella = np.arange(0.0,0.8,0.1)
lambdas = np.arange(0.0,1.05,0.05)
rvalues = []
lams = []
for k in range(2):
    for i in umbrella:
        for j in range(len(lambdas)):
                rvalues.append(i)
for j in range(len(lambdas)):
    rvalues.append(float(-1))
for k in range(2):
    for i in range(len(umbrella)):
        for j in range(len(lambdas)):
            lams.append(j)
for j in range(len(lambdas)):
    lams.append(j)
sub_rvalues=[]
for i in range(17):
    for j in range(10,21):
        sub_rvalues.append(j+i*21)

for i in range(len(sub_rvalues)):
	print 'ensemble', i, '-->', 'umbrella',rvalues[sub_rvalues[i]], 'lambda', lams[sub_rvalues[i]]
