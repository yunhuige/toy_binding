# free simulation/all_epsilon README

We kept the original σ parameter (for carbon) the same (0.339967 nm), and varied the ε value from 0.0 to 9.5 kJ/mol in increments of 0.5 kJ/mol (the original value was 0.457730 kJ/mol).  For each value of epsilon, we simulated 10 trajectories of length 1 µs, resulting in a total of 200 µs of aggregate trajecory data.  Snapshots were recorded every 100 ps.  

# distance calculations

In the [distances](distances) directory are numpy arrays containing the distance between the ligand and the center of the binding pocket (computed as the center of mass of atoms 1-8,10,11 gromacs indices) for each frame.


