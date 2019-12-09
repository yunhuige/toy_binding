#!/bin/sh
#PBS -l walltime=24:00:00
#PBS -N mbar_fep
#PBS -q normal 
#PBS -l nodes=1:ppn=20
#PBS -o mbar_fep 
#PBS 


cd $PBS_O_WORKDIR


cd 10/mbar
python compute_mbar.py &
cd ../../


cd 20/mbar
python compute_mbar.py &
cd ../../


cd 30/mbar
python compute_mbar.py &
cd ../../


cd 40/mbar
python compute_mbar.py &
cd ../../


cd 50/mbar
python compute_mbar.py &
cd ../../


cd 60/mbar
python compute_mbar.py &
cd ../../

cd 70/mbar
python compute_mbar.py &
cd ../../


cd 80/mbar
python compute_mbar.py &
cd ../../


cd 90/mbar
python compute_mbar.py &
cd ../../


wait

