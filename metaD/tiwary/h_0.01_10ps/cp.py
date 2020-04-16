import sys, os

for i in range(20):
	print i
	os.system('mkdir -p %d'%i)
	os.system('cp -r qsub.sh index.ndx plumed.dat plumed_ex.dat pocket.top snapshot.gro prod_fah.mdp amber99sbnmr1-ildn.ff %d/'%i)
