import sys, os
for i in range(20):
        print i
        os.chdir('%d/'%i)
#        os.system('qsub qsub.sh')
	os.system('python extend.py')
        os.chdir('../')
