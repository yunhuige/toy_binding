import sys, os
for i in range(1,20):
	print i
	os.chdir('%d'%i)
	os.system('plumed sum_hills --hills HILLS --min 0.0 --max 3.0 --bin 100')
	os.chdir('../')
