# first_10percent

Truncated dataset (first 10% = 40 ns) of each ensemble (21 lambdas x 8 umbrellas x 2 directions = 336 ensembles).

There are extra 21 ensembles (only FEP lambda scaling no umbrellas simulations) in the folder [special](https://github.com/yunhuige/toy_binding/tree/master/bias_simulation/analysis/dataset/first_10percent/special).

# frames_200/frames_2000/frames_20000/frames_200000

Each ensemble simulation has 200000 frames in total. Subsampling from the original data with stride of 1/10/100/1000 yields 200000/20000/2000/200 frames.

These folders have hitogram and traces of distance between the ligand and the center of pocket (10 atoms not 11!).


# compute_ukn.ipynb

Key scripts used to compute ukn matrix using MBAR.

# get_distances.ipynb

Get distance between the ligand and the center of pocket (output from pulling simulations). Mainly used for subsampling dataset.

# mapping.dat

Information of umbrella and lambda for each ensemble.

# plot_figures_bias.ipynb

Scripts of plotting histogram and traces for each ensemble.

