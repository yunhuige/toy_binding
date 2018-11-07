#!/bin/sh
#PBS -l walltime=24:00:00
#PBS -N dtram_20000 
#PBS -q normal 
#PBS -l nodes=1:ppn=10
#PBS -o dtram_20000 
#PBS 

cd $PBS_O_WORKDIR

python compute_dtram.py
