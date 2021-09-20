#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 23:24:59 2021

@author: andreaaparicio
"""

The notebook “Fig_S10-11-12.nb" creates the plots in Figure S10-S12.

Inputs: 

- List of every species' sensor score, for every network in .mx format. This is 
  saved in "data_GeneralFigs/" as "SSall.mx"
- List of every species' mean abundance and variance change, for every network
  analyzed and every value of "c", for the network's "tau". 
  These are saved in "data_FigS10S11S12/" as "(sys_name)_mean_(c)_(tau).csv,
- List of every species' mean early-warning score accross realizations. These
  are saved in "data_FigS10S11S12/" as "(sys_name)_EWSmean_.csv"
  
Outputs:

The plots in figures S10, S11, and S12