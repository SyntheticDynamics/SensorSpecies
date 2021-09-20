
"""
Created on Sat Sep 11 20:58:43 2021

@author: andreaaparicio
"""

The notebook "EW_score_calc.nb" analyzes the time-series obtained after simulating a 
critical transition on a mutualistic system. 
For a specific realization it plots 
 - the mean abundance for every step of \mu
 - the early-warning score vs sensor score of every species. 
For all the realizations it plots 
 - the median early-warning score vs sensor score of every species
 - the early-warning score ratio by degree, by sensor score and at random
 - the distribution of the early-warning score ratio by degree and by sensor score
 compared to random
 
Inputs: 
- sys_name = the name of a .csv file saved in "data/" containing the system's interaction matrix ("sys_name.csv").
                The matrix must be rectangular and have plants as rows and animals as columns.
- kStart initial realization number for which time-series metrics data exist (must be >= 0)
- kEnd = final realization number for which time-series metrics data exist (must be > kStart)
- kT = one particular realization to display (must be \in (kStart,kEnd]))

Outputs: 
- the plots specified above

Instructions:
To run enter the interaction matrix filename "sys_name.csv" (without the extension) in the field fn, 
the kStart, KEnd and kT values in the fields of the same name, and run the main function.

Note: If the Sensor Score and Vertex Degree have been calculated before and  saved in "data/data_sensor/",  
as "fn_SS.scv" and "fn_VD.csv", respectively,  comment the indicated line to avoid re -calculating them 
and overwriting the files