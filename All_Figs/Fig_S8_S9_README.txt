"""
Created on Sat Sep 11 20:58:43 2021

@author: andreaaparicio
"""

The notebook “Fig_S8_S9.nb" creates the plots in Figure S8 and S9

Inputs: 

- List of network names (sys_name) to be analized specified in the field filenames 
- One .csv file for every realization "k" of every network to be analyzed, containing
  a list of the early-warning score of every species with nominal parameters. These are saved
  in "data_GeneralFigs/" "as "sys_nameEWS(k).csv"
- One .csv file for every realization "k" of every network to be analyzed, containing
  a list of the early-warning score of every species with parameter “P” at the high “val”=1 or low “val=0” 
  value. These are saved in "data_FigS8/EWSdata/“ "as “(sys_name)_EWS_(Pval)_(k).csv"
- List of every species' sensor score, for every network in .mx format. This is 
  saved in "data_GeneralFigs/" as "SSall.mx"
- List of every species' degree, for every network in .mx format. This is 
  saved in "data_GeneralFigs/" as "Degree.mx"
- List of every network's MSS size in .mx format. This is 
  saved in "data_GeneralFigs/" as "MSSsize.mx"
- List of every network’s q* metric when choosing species by sensor score, 
   for every realization and every parameter value. These are  saved in “data_FigS8/data_q_r1/“ as “Qs.csv”
- List of every network’s q* metric when choosing species at random, 
   for every realization and every parameter value. These are  saved in “data_FigS8/data_q_r1/“ as “Qr.csv”
- List of every network’s r1 metric when choosing species by sensor score, 
   for every realization and every parameter value. These are  saved in “data_FigS8/data_q_r1/“ as “Rs.csv”
- List of every network’s r1 metric when choosing species at random, 
   for every realization and every parameter value. These are  saved in “data_FigS8/data_q_r1/“ as “Rr.csv”
-List of every network’s deviations from the equilibrium, with parameter “P” at the high “val”=1 or low “val=0” 
  value. These are saved in “"data_FigS8/devEqData/“ as “Dev(Pval)a.mx"
-List of every network’s deviations from the equilibrium for every realization, with nominal parameters.
 These are saver in data_FigS8/devEqData/ as “(sys_name)_DevEqO2_reps.csv"

Outputs:
The plots in Figure S8 and S9

To do all the calculations and create the plots, sequentially run all the 
initialization  cells in the notebook.