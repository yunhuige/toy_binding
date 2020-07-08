#!/bin/sh
#PBS -l walltime=24:00:00
#PBS -N tram_fep 
#PBS -q normal 
#PBS -l nodes=1:ppn=20
#PBS -o tram_fep 
#PBS 


cd $PBS_O_WORKDIR

cd 10/
python compute_tram_1.py &
cd ../

cd 20/
python compute_tram_1.py &
cd ../

cd 30/
python compute_tram_1.py &
cd ../

cd 40/
python compute_tram_1.py &
cd ../

cd 50/
python compute_tram_1.py &
cd ../

cd 60/
python compute_tram_1.py &
cd ../

cd 70/
python compute_tram_1.py &
cd ../

cd 80/
python compute_tram_1.py &
cd ../

cd 90/
python compute_tram_1.py &
cd ../

wait
