
"""
Created on Sat Sep 11 20:58:43 2021

@author: andreaaparicio
"""

The notebook "General_Figs.nb" creates the plots in Figures 4, S6, S7.

Inputs: 

- List of network names (sys_name) to be analized specified in the field filenames 
- One .csv file for every realization "k" of every network to be analyzed, containting
  a list of the early-warning score of every species. These are saved
  in "data_GeneralFigs/" "as "sys_nameEWSk.csv"
- List of every species' sensor score, for every network in .mx format. This is 
  saved in "data_GeneralFigs/" as "SSall.mx"
- List of every species' degree, for every network in .mx format. This is 
  saved in "data_GeneralFigs/" as "Degree.mx"
- List of every network's MSS size in .mx format. This is 
  saved in "data_GeneralFigs/" as "MSSsize.mx"
- List of every network's highest sensor score, in .csv format. This is 
  saved in "data_GeneralFigs/" as "MaxSS.csv"
- List of every network's deviations from equilibrium, in .csv format. This is 
  saved in "data_GeneralFigs/" as "DevEq2.csv"
- List of every network's mean (q^* - q_rand), in .csv format. This is 
  saved in "Zqd.csv"
- List of every network's mean (r_1 - r_(1,rand), in .csv format. This is 
  saved in "Zrd.csv"

Outputs:

The plots in Figures 4, S6, S7.

To do all the calculations and create the plots, sequentially run all the 
initialization  cells in the notebook.