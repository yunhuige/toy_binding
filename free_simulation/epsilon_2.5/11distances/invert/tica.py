from msmbuilder.featurizer import DihedralFeaturizer
from msmbuilder.dataset import dataset
import numpy as np
from matplotlib import pyplot as plt
import mdtraj as md
import os,sys, glob
import msmbuilder.utils
import pickle
from msmbuilder.utils import load
from msmbuilder.cluster import KMeans
from msmbuilder.cluster import KCenters
from msmbuilder.cluster import KMedoids
from msmbuilder.cluster import MiniBatchKMeans
from msmbuilder.msm import implied_timescales
from msmbuilder.msm import ContinuousTimeMSM, MarkovStateModel
from itertools import combinations
from msmbuilder.featurizer import AtomPairsFeaturizer
from msmbuilder.decomposition import tICA
from sklearn.pipeline import Pipeline
from msmbuilder.example_datasets import fetch_met_enkephalin
from matplotlib import pyplot as plt
from sklearn.externals import joblib
#os.system('mkdir tICA')
#Featurization
#trajs = md.load('traj0.xtc',top='conf.gro')
#Ind = trajs.topology.select("all")
#trajs1=trajs.atom_slice(Ind)
distances=[]
#os.chdir('8662/distance')
#file=glob.glob('*npy')
#list1=sorted(file,key=lambda x: int(os.path.splitext(x.split("distance")[1])[0]))
#print list1
#os.chdir('../../')
#sys.exit()
#for i in list1:
#	b=np.load('8662/distance/%s'%i)
#os.chdir('8662/29bind+9RUNs/')
#allFiles=glob.glob('*npy')
#list1=sorted(allFiles, key=lambda x: int(os.path.splitext(x.split("distance")[1])[0]))
#print len(list1)
#sys.exit()
#for i in list1:
#traj=[]
#for i in range(20):
#	a=np.load('distance%d.npy'%i)
#	if len(a) >= 1001:
#		traj.append(i)
#for i in range(200,1000):
#        a=np.load('distance%d.npy'%i)
#        if len(a) >= 1001:
#                traj.append(i)
#np.save('traj.npy',traj)
#sys.exit()
for i in range(20):
	b=np.load('invert_dis_%d.npy'%i)
	distances.append(b)
#np.save('test.npy',distances)
#sys.exit()
#distances=np.load('test.npy')
#for j in range(78,192):
#	b=np.load('distance%d.npy'%j)
#        distances.append(b)
#os.chdir('../../')
#for i in range(33):	#first 9 RUNs
#	b=np.load('8662/29bind+9RUNs/distance%d.npy'%i)
#	distances.append(b)
#for k in range(34,66):
#        d=np.load('8662/29bind+9RUNs/distance%d.npy'%k)
#        distances.append(d)

#for l in range(67,119):
#        e=np.load('8662/29bind+9RUNs/distance%d.npy'%l)
#        distances.append(e)

#for m in range(120, 142):
#        f=np.load('8662/29bind+9RUNs/distance%d.npy'%m)
#        distances.append(f)

#for n in range(143,213):
#        g=np.load('8662/29bind+9RUNs/distance%d.npy'%n)
#        distances.append(g)

#for j in range(465):
#	c=np.load('8617/feat/distance%d.npy'%j)
#	distances.append(c)
#print distances.shape()
#distances=np.load('TrpLoop2.npy')
#distances=[np.load('test%d.npy'%i) for i in range(2)]
tica_model = tICA(lag_time=50,n_components=4)
tica_fit = tica_model.fit(distances)
output=open('tica_model.npy','wb')
pickle.dump(tica_model,output)
output.close()
tica_transformed = tica_fit.transform(distances)
output=open('tica_eigenvectors.npy','wb')
pickle.dump(tica_model.eigenvectors_,output)
output.close()

#output=open('tica_components.npy','wb')
#pickle.dump(tica_model.components_,output)
#output.close()
#tica_ev = tica_model.eigenvectors_


#output =open('tica_model.npy','wb')
#pickle.dump(tica_model,output)
#output.close()



#print tica_ev
#np.save('tica_ev.npy',tica_ev)


#tica_transformed = tICA(lag_time=50,n_components=4).fit_transform(distances)
np.save('tica.npy',tica_transformed)
