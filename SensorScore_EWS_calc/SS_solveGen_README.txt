"""
Created on Sat Sep 11 16:25:29 2021

@author: andreaaparicio
"""

The script SS_solveGen.py builds a model for a mutualistic system, defines its parameters, simulates a critical transition, calculates and saves metrics of the resulting time-series, and calculates and saves the early-warning scores. 

Run it from the console typing 
python SS_solveGen.py sys_name kStart kEnd

Inputs: 
- sys_name = the name of a .csv file saved in "data/" containing the system's interaction matrix ("sys_name.csv").
                The matrix must be rectangular and have plants as rows and animals as columns.
- kStart  = initial realization number (must be > 0)
- kEnd = final realization number (must be > kStart)

The script will run kTot = (kEnd - kStart - 1) times producing kTot realizations

Outputs: 
For every k \in [kStart,kEnd) 
 -saved in "data/data_sims/"):
  	-the variance of the abundance of every species at every \mu step ("sysname_var_reps_k.csv") 
  	-the autocorrelation of the abundance of every species at every \mu step ("sysname_ac_reps_k.csv") 
  	-the mean of the abundance of every species at every \mu step ("sysname_var_mean_k.csv") 
  	-a sample of the abundance at every \mu step ("sysname_samp_reps_k.csv") 
 -saved in "data/data_EWS/"
	-early-warning scores of every species (first plants and then animals) ("sysnameEWSk.csv") 
  	