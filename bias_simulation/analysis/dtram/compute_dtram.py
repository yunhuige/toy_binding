import sys, os
import numpy as np
from pyemma.thermo import dtram
from pyemma import msm
import pyemma


stride = 100
os.system('mkdir frames_%d/'%(int(200000./stride)))
interval = 0.002*stride  # in ns
nstates = 10
bin_min = 0.0
bin_max = 0.8
dx=(bin_max-bin_min)/nstates
pmf_distances=np.arange(bin_min,bin_max+dx,dx)
bincenters = (pmf_distances[0:-1]+pmf_distances[1:])/2.0

assign = np.load('../dataset/frames_%d/clustered_matrix.npy'%(int(200000./stride)))
K = assign.shape[0] # termodynamic states
if stride == 10000:
    lagtimes = np.array([1,2,3,4,5])
elif stride == 1000:
    lagtimes = np.array([1,5,10,20,30,40,50])
elif stride == 100:
    lagtimes = np.array([1,15,50,100,200,300,400,500])
elif stride == 10:
    lagtimes = np.array([1,20,50,100,200,500,800,1000,2000,3000,4000,5000,6000,7000,8000])

bias = np.load('../dataset/frames_%d/bias.npy'%(int(200000./stride)))

total_its = []
bootstrap = False

if bootstrap:
	fold = 5
	st = int(assign.shape[1]/fold)
	for i in range(fold):
    		if i != fold-1:
    			ass = np.concatenate((assign[:,:st*(i+1)],assign[:,st*(i+1)+st:]),axis=1)
    		else:
        		ass = assign[:,st:]
    		ttrajs = []
    		dtrajs = []
    		for k in range(K):
        		ttrajs.append(k*np.ones(ass.shape[1],dtype=int))
        		dtrajs.append(ass[k])
        		#print('ttrajs',ttrajs)
        		#print('dtrajs',dtrajs)
        		#print('bias',bias)
    		motion = 4
    		dtram_obj = dtram(ttrajs, dtrajs, bias, lagtimes, unbiased_state=int(assign.shape[0])-1) # the unbiased ensemble is the last one
#print('len(dtram_obj)',len(dtram_obj))
#print('dtram_obj',dtram_obj)
#print('len(dtram_obj[0].models)',len(dtram_obj[0].models))
#sys.exit()
#dtram_obj.save('test_dtram.npy',dtram_obj)
#print dtram_obj.msm.timescales(4)
#sys.exit()
		its=[[] for m in range(motion)]
#    print 'its',its
	        for j in range(len(lagtimes)):
        		time = dtram_obj[j].msm.timescales(motion)
#	print 'time',time
        		for l in range(motion):
#	    print 'l',l
            			its[l].append(time[l])
    # print('its',its)
    		total_its.append(its)

	np.save('total_its.npy',total_its)
else:
	ttrajs = []
	dtrajs = []
	for k in range(K):
		ttrajs.append(k*np.ones(assign.shape[1],dtype=int))
		dtrajs.append(assign[k])
	motion = 4
	dtram_obj = dtram(ttrajs, dtrajs, bias, lagtimes, unbiased_state=int(assign.shape[0])-1) # the unbiased ensemble is the last one
	its=[[] for m in range(motion)]
	for j in range(len(lagtimes)):
		time = dtram_obj[j].msm.timescales(motion)
		for l in range(motion):
			its[l].append(time[l])
	import matplotlib
	matplotlib.use('Agg')
	from matplotlib import pyplot as plt
        plt.figure()
        for m in range(motion):
            plt.plot(interval*lagtimes,[n*interval for n in its[m]])
    	plt.xlabel('lagtime (ns)')
    	plt.ylabel('implied timescale (ns)')
    	plt.yscale('log')
   	plt.savefig('frames_%d/implied_timescales.pdf'%(int(200000./stride)))
    	plt.close()




sys.exit()
if (0):
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib import pyplot as plt
    its=[[] for k in range(motion)]
#    for i in range(K):
#        its=[[] for k in range(motion)]
    for j in range(len(lagtimes)):
       time = dtram_obj[j].msm.timescales(motion)
       for l in range(motion):
            its[l].append(time[l])
    print('its',its)
    plt.figure()
    for m in range(motion):
        plt.plot(interval*lagtimes,[n*interval for n in its[m]])
    plt.xlabel('lagtime (ns)')
    plt.ylabel('implied timescale (ns)')
    plt.yscale('log')
    plt.savefig('frames_%d/implied_timescales.pdf'%(int(200000./stride)))
    plt.close()
sys.exit()
        
#print(len(dtram_obj))
#sys.exit()
#np.save('dtram_obj.log_likelihood.npy',dtram_obj.log_likelihood())
#np.save('dtram_obj.count_matrices.npy',dtram_obj.count_matrices)
#np.save('dtram_obj.stationary_distribution.npy',dtram_obj.stationary_distribution)
#print('dtram_obj.log_likelihood()',dtram_obj.log_likelihood())
#print('dtram_obj.count_matrices',dtram_obj.count_matrices)
#print('dtram_obj.stationary_distribution',dtram_obj.stationary_distribution)

if (0):
    from matplotlib import pyplot as plt
    plt.figure()
    plt.xlabel('distance (nm)')
    #plt.xlabel('bin index')
    plt.ylabel('pop (%)')
    for i in range(len(lagtimes)):
        plt.plot(bincenters,dtram_obj[i].stationary_distribution*100.0, '-',label='lagtime=%.3f ns'%(stride*lagtimes[i]))
    plt.legend(loc='best')
    plt.savefig('stationary_distribution(dtram).pdf')
#    plt.show()
#print(dtram_obj.models[0].timescales(4))
#print(dtram_obj.models[1].timescales(4))
#pyemma.plots.plot_memm_implied_timescales(
    #dtram_obj.models[0], nits=8, annotate=False, marker='x')

for i in range(len(lagtimes)):
    print('dtram_obj[i].stationary_distribution',dtram_obj[i].stationary_distribution*100.0)
