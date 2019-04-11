Clustering cannot work and get this error .....

```
File "/Users/yunhuige/anaconda/lib/python2.7/site-packages/msmbuilder/cluster/base.py", line 165, in transform
    return self.predict(sequences)
  File "/Users/yunhuige/anaconda/lib/python2.7/site-packages/msmbuilder/cluster/base.py", line 113, in predict
    predictions.append(self.partial_predict(X))
  File "/Users/yunhuige/anaconda/lib/python2.7/site-packages/msmbuilder/cluster/base.py", line 135, in partial_predict
    return super(MultiSequenceClusterMixin, self).predict(X)
  File "/Users/yunhuige/anaconda/lib/python2.7/site-packages/msmbuilder/cluster/kcenters.py", line 119, in predict
    X, self.cluster_centers_, metric=self.metric)
  File "msmbuilder/libdistance/libdistance.pyx", line 127, in msmbuilder.libdistance.assign_nearest (msmbuilder/libdistance/libdistance.cpp:2932)
  File "msmbuilder/libdistance/libdistance.pyx", line 385, in msmbuilder.libdistance._assign_nearest_double (msmbuilder/libdistance/libdistance.cpp:6401)
IndexError: Out of bounds on buffer access (axis 0)
```

And this is the clustering scripts:

```
tica_transformed=np.load('tica.npy')
assignments=KCenters(n_clusters=20).fit(tica_transformed)
centers=assignments.cluster_centers_
np.save('cluster_centers.npy',centers)
ass=assignments.transform(tica_transformed)

np.save('Assignments.npy',ass)

lagtimes = np.array([1,5,10,15,30,100,150,200,300,600,1000,1200,1500,2000,2500,5000,8000,10000,15000,20000, 30000,40000,50000])
msmts = []
for lagtime in lagtimes:
        print "\tLagtime: %d"%lagtime
        msm = MarkovStateModel(lag_time=lagtime).fit(ass)
        msmts.append(msm.timescales_)
np.save('test_msmts.npy', msmts)



ns_per_frame = 0.001
import matplotlib.pyplot as plt
plt.figure()
for j in range(4):
        print j
        plt.plot(ns_per_frame*lagtimes,[ns_per_frame*msmts[i][j] for i in range(len(lagtimes))])

plt.xlabel('lagtime (ns)')
plt.ylabel('implied timescale (ns)')
plt.yscale('log')
plt.savefig('lagtime_transform.pdf')
plt.show()

```
