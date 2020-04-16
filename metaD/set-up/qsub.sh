#!/bin/bash
#PBS -l walltime=24:00:00
#PBS -N metaD_toy_0.01
#PBS -q normal 
#PBS -l nodes=1:ppn=18
#PBS -o metaD_toy_0.01 
#PBS 

cd $PBS_O_WORKDIR
export OMP_NUM_THREADS=1
module load gromacs/2016.3-plumed
module load mpi/openmpi

gmx grompp -f prod_fah.mdp -c snapshot.gro -p pocket.top -n index.ndx -o topol.tpr
mpirun mdrun -v -s topol.tpr -c prod.gro -plumed plumed.dat

