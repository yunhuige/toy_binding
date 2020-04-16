PLUMED related files to run simulations can be found in each folder with different set-up. Comments in the file are copied from PLUMED tutorial and are not exact numbers used in the simulation. Below are explanation of important parameters and what numbers are actually used in each simulations.

h: Gaussian height (kJ/mol) (HEIGHT)

p: bias potential deposit rate step(2fs in this case)(PACE)

w: Gaussian width (CV unit, nm in this case) (SIGMA)

The actual simulation data are too big for Github. So I uploaded them to vav4 (server@vav4.ocis.temple.edu). People who can access to vav4 should also be able to access the data for analysis. The path of each simulation are listed below.

#h_0.01_1ps: h: 0.01, p:500, w: 0.01

900ns * 20 Runs = 18000 ns in total

An averaged free energy landscape is also plotted which can be found in the folder.

path: /array1/storage/Yunhui/metaD_toy/h_0.01


h_0.01_10ps: h: 0.01, p:5000, w: 0.01

100ns * 20 Runs = 2000 ns in total

path: /array1/storage/Yunhui/metaD_toy/h_0.01_pace_10ps


h_0.01_100ps: h: 0.01, p:50000, w: 0.01

100ns * 20 Runs = 20000 ns in total

path: /array1/storage/Yunhui/metaD_toy/h_0.01_pace_100ps


h_0.01_1000ps: h: 0.01, p:500000, w: 0.01

100ns * 20 Runs = 20000 ns in total

path: /array1/storage/Yunhui/metaD_toy/h_0.01_pace_1000ps


h_0.1_1ps: h: 0.1, p:500, w: 0.01

900ns * 20 Runs = 18000 ns in total

path: /array1/storage/Yunhui/metaD_toy/h_0.1


h_0.5_1ps: h: 0.5, p:500, w: 0.01
100ns * 20 Runs = 20000 ns in total

path: /array1/storage/Yunhui/metaD_toy/h_0.5


h_1.0_1ps: h: 1.0, p:500m w: 0.01

100ns * 20 Runs = 20000 ns in total

path: /array1/storage/Yunhui/metaD_toy/h_1.0


I only did massive simulations for some of the settings due to the time limit. But the files in the folder on vav4 should be enough for further extended simulations. 
The manuscript of the unbiased simulation analysis is under preparation. If anyone need the reference number in terms of the folded state population, free energy landscape, etc please let me know.
-- Yunhui Ge 04/2020
