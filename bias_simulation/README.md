# analysis
Samplping information:

21 lambdas in total (400 ns for each), scaling vdw from 0.0 (no vdw) to 1.0 (full vdw) (increment of 0.05).

21 lambdas x 8 umbrellas x 2 directions (pull/push) = 168 x 2 ensembles.

Concatenating two directions together yield 168 ensembles in total.

Only the second half lambdas are used (11/21 lambdas) in current analysis (11 x 8 = 88 ensembles).

Original xtc files are saved every 100ps (4000 frames). However the distance information (pullx.xvg) is saved every 1 ps and free energy difference information (dhdl.xvg) is saved every 2 ps so to match up with each other I extracted distance information every 2 ps.

p.s pullx.xvg includes the COM distance (nm) between the ligand and the center of 10 atoms (not 11 atoms!).


# fep
FEP simulations of 1/ligand only and 2/ligand and pocket. 21 lambdas in total (400 ns for each), scaling vdw from 0.0 (no vdw) to 1.0 (full vdw) (increment of 0.05).

