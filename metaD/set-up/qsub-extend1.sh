#!/bin/sh
#PBS -l walltime=24:00:00
#PBS -N toy_ex_0.1
#PBS -q normal 
#PBS -l nodes=1:ppn=18
#PBS -o toy_ex_0.1
#PBS 

cd $PBS_O_WORKDIR
export OMP_NUM_THREADS=1
module load gromacs/2016.3-plumed
module load mpi/openmpi
gmx convert-tpr -s topol.tpr -extend 200000.000000 -o topol1.tpr -f traj.trr

mpirun mdrun -s topol1.tpr -c confout1.gro -cpi -plumed plumed_ex.dat -v

