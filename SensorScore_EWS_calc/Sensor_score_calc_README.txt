
"""
Created on Sat Sep 11 20:13:07 2021

@author: andreaaparicio
"""

For a mutualistic system, the notebook "Sensor_score_calc.nb": plots the system's interaction matrix  
calculates the sensor score of every species and relevant network properties, 
draws  a network diagram showing the sensor score of plants and animals, and makes
predictions for the metrics q^* and Subscript[r, 1]*. 

This notebook needs the file "DimRedFunDS.mx", in "functions/".

Inputs: 
- sys_name = the name of a .csv file saved in "data/" containing the system's interaction matrix ("sys_name.csv").
  The matrix must be rectangular and have plants as rows and animals as columns.

Instructions:
To run enter the interaction matrix filename "sys_name.csv" (without the extension) in the field fn, 
and run the main function.