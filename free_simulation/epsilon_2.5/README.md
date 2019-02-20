20 parallel runs were performed, each of them has 6000 ns data which yield 120 us in total.

# 2state_MSM

Construct a 2-state MSM using self prepared scripts based on the distance between the ligand and the center of the binding pocket (computed as the center of mass of atoms 1-8,10,11 gromacs indices). The problem is predicted implied timescales may return "nan" at some lagtime. Something is wrong and needs to be fixed in [this scripts](https://github.com/yunhuige/toy_binding/blob/master/free_simulation/epsilon_2.5/2state_MSM/build_MSM.ipynb).

# com

Computed distances between the ligand and the center of the binding pocket (computed as the center of mass of atoms 1-8,10,11 gromacs indices) for all 20 parallel simulations.

[1D_msm](https://github.com/yunhuige/toy_binding/tree/master/free_simulation/epsilon_2.5/com/1D_msm): Construct MSMs using self prepared scripts based on the distance between the ligand and the center of the binding pocket. Different number of states (10, 30, 50, 100, 200) are used. The problem is predicted implied timescales may return "nan" at some lagtime. 

[1D_msmbuilder](https://github.com/yunhuige/toy_binding/tree/master/free_simulation/epsilon_2.5/com/1D_msmbuilder): Construct MSMs using msmbuilder 3.5 based on the distance between the ligand and the center of the binding pocket (tICA is not used). Different number of states (10, 30, 50, 100, 200) are used. The problem is predicted implied timescales are not separated. 


