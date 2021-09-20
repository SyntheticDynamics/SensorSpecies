#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 23:24:59 2021

@author: andreaaparicio
"""

The notebook “Fig_S14.nb" creates the plots in Figure S14

Inputs: 

- List of every species' sensor score, for every network in .mx format. This is 
  saved in "data_GeneralFigs/" as "SSall.mx"
- List of every species' degree, for every network in .mx format. This is 
  saved in "data_GeneralFigs/" as "Degree.mx"
- List of every species' early-warning score based on the indicators "ind" = ("ac","cv","var"),
  accross realizations (reps), and for every network (sys_name), with additive noise. 
  These are saved in "data_FigS14/" as "(sys_name)_(ind)_reps_(rep)add_ewV.csv"
- List of every species' early-warning score based on the indicators "ind" = ("ac","cv","var"),
  accross realizations (reps), and for every network (sys_name), with multiplicative noise. 
  These are saved in "data_FigS14/" as "(sys_name)_(ind)_reps_(rep)mult_ewV.csv"
    
Outputs:

The plots in figure S14

To do all the calculations and create the plots, sequentially run all the 
initialization  cells in the notebook.