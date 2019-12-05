#!/bin/sh
#PBS -l walltime=48:00:00
#PBS -N tram_umb200 
#PBS -q medium 
#PBS -l nodes=1:ppn=16
#PBS -o tram_umb200 
#PBS 



cd $PBS_O_WORKDIR

python compute_tram_1.py &

python compute_tram_10.py &

python compute_tram_30.py &

python compute_tram_50.py &

python compute_tram_80.py &

python compute_tram_100.py &

python compute_tram_200.py &

python compute_tram_300.py &

python compute_tram_500.py &

python compute_tram_800.py &

python compute_tram_1000.py &

python compute_tram_2000.py &

python compute_tram_3000.py &

python compute_tram_4000.py &

cd dtram/
python compute_bias_dtram.py &

cd ../mbar/
python compute_mbar.py &
cd ../

wait

cd dtram/
python compute_dtram.py
