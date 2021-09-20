#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 22:05:16 2021

@author: andreaapariciomartinez

This code simulates the system in Figure 1a for the perturbed case, and induces a critical transition to the unperturbed case. It creates the plots in Figure 1c-f. 

"""
import numpy as np
from matplotlib import pyplot as plt
import sdeint
import scipy.integrate as scint
import pandas as pd
import math as mt
#%% PARAMETERS
x0 = [.7,2,1.8]
h=0.1
kp1 = 4
ka1 = 2
ka2 = 2
tau = 1
g0 = 8*tau
gp11 = g0/kp1
gp12 = -g0/kp1
ga11 = g0/ka1
ga21 = g0/ka2
alfp1 = -.1
alfa1 = -.1
alfa2 = -.5
bp1 = 1
bp2 = 1
bp3 = 1
#perturbations
p1_1=1
p1_2=2
p2_1=1.6
p2_2=-1
p3_1=-.5
p3_2=1
#% noise
center = 0.0
sigmax=24e-3
sigmay = .02
#%plots
colors=['m', 'c', 'tab:orange'] 
labels = ['P3', 'A1', 'A2']
colors2 = ['darkmagenta','darkcyan','chocolate']
ticksp = np.arange(0,110,25) 
#% critical transition
chsteps = 200
tch = 300

#%% DYNAMICS

#%% Defines the perturbations. 
def p_fun(t):
    p2=0
    p3=0
    p1=0
    if t > 25:
        if t<27:
            p1=p1_1
    if t>50:
        if t<52:
            p1=p1_2
            p2=p2_1
            p3=p3_1
           
    if t >75:
        if t<77:
            p2=p2_2
            p3=p3_2
    return [p1,p2,p3]
#%% Defines the interaction strenght for every step

def disc_fun(t):
        disc2 = 1-((1/chsteps)*mt.floor((t)/tch))
        if disc2<0:
            disc2=0
        return disc2
#%% Mutualist dynamics 
#perturbation on A1 and A2
    
def mutual_eq(x,t):
    
    P3 = x[0]
    A1 = x[1]
    A2 = x[2]
    
    
    if P3<0:
        P3 = 0
    if A1<0:
        A1=0
    if A2<0:
        A2=0
    
    if sim == "CT":
        [p1,p2,p3] = [0,0,0]
        d1 = disc_fun(t)
    
    if sim == "none":
        [p1,p2,p3] = [0,0,0]
        d1 = 1
        
    if sim == "pert":
        [p1,p2,p3]=p_fun(t)
        d1 = 1
        
    gp11 = d1*g0/kp1
    ga11 = d1*g0/ka1

    dP3 = P3*(alfp1 -bp1*P3 + (gp11*A1 + gp12 * A2)/(1+h*(gp11*A1 + gp12 * A2)))+10e-5
    dA1 = A1*(alfa1 -bp1*A1 + (ga11*P3)/(1+h*ga11*P3))+p1+10e-5
    dA2 = A2*(alfa2 -bp3*A2 + (ga21*P3)/(1+h*ga21*P3))+p2+10e-5    
    return np.array([dP3, dA1, dA2])
#%% Mutualist dynamics 
#perturbation on A1 and P3
def mutual_eq2(x,t):
    
    P3 = x[0]
    A1 = x[1]
    A2 = x[2]
    
    
    if P3<0:
        P3 = 0
    if A1<0:
        A1=0
    if A2<0:
        A2=0
    
    if sim == "CT":
        [p1,p2,p3] = [0,0,0]
        d1 = disc_fun(t)
    
    if sim == "none":
        [p1,p2,p3] = [0,0,0]
        d1 = 1
        
    if sim == "pert":
        [p1,p2,p3]=p_fun(t)
        d1 = 1
        
    gp11 = d1*g0/kp1
    ga11 = d1*g0/ka1

    dP3 = P3*(alfp1 -bp1*P3 + (gp11*A1 + gp12 * A2)/(1+h*(gp11*A1 + gp12 * A2)))+p3+10e-5
    dA1 = A1*(alfa1 -bp1*A1 + (ga11*P3)/(1+h*ga11*P3))+p1+10e-5
    dA2 = A2*(alfa2 -bp3*A2 + (ga21*P3)/(1+h*ga21*P3))+10e-5    
    return np.array([dP3, dA1, dA2])
#%% additive noise
def addN_eq(x,t):
    g1 = sigmax
    g2 = sigmax
    g3 = sigmax
    
    return np.diag([g1, g2, g3])
#%% Assigns a zero value to negative abundances.
    
def clean(x):

    for i in range(len(x)):
        for j in range(3):
            if x[i,j]<0:
                x[i,j]=0
    return x
#%% SIMULATIONS

#%% PERTURBATION    
#%% Simulation parameters
tmax = 100 #final time
st = .1 #step size
t = np.arange(0,tmax,st) 
sim = "pert"
#%%solve
mut_add1 = sdeint.itoint(mutual_eq, addN_eq, x0, t)
mut_add2 = sdeint.itoint(mutual_eq2, addN_eq, x0, t)
#%% plot perturbation time series
plt.figure(figsize=[5,5.5])
plt.subplot(2,1,1)
for i in range(3):
    plt.plot(t,mut_add1[:,i], color = colors[i], label = labels[i])
plt.xlabel("time")
plt.ylabel("abundance")
plt.xticks(ticksp)
plt.yticks([1,2,3])
plt.legend()
plt.subplot(2,1,2)
for i in range(3):
    plt.plot(t,mut_add2[:,i], color = colors[i], label = labels[i])
plt.xlabel("time")
plt.ylabel("abundance")
plt.xticks(ticksp)
plt.legend()
plt.yticks([1,2,3])
plt.tight_layout()
   
#%% CRITICAL TRANSITON
sim = "CT"
#%% Simulation parameters
st = .1
pmin=.6
actsteps = chsteps-(pmin/(1/chsteps))
tmaxd = tch*actsteps 
td = np.arange(0.0,tmaxd,st)
dch2 = np.arange(1.0,disc_fun(tmaxd),- (st)/(chsteps*tch))
chmea = np.arange(1,pmin,-1/chsteps)
#%% solve
mut_d_add = sdeint.itoint(mutual_eq, addN_eq, x0, td)
#%%
mut_d_add = clean(mut_d_add)
#%% Gets the mean at every step
meanN = np.zeros((int(actsteps),len(mut_d_add.T)))
for i in range(int(actsteps)):
    for j in range(3):
        temp = pd.Series(mut_d_add[i*int(tch/st):(i*int(tch/st))+int(tch/st)-1,j])
        meanN[i,j] = pd.DataFrame.mean(temp)
        if i > 0:
            if meanN[i,j] < meanN[i-1,j]/2:
                if meanN[i,j]>.05:
                    temp = pd.Series(mut_d_add[i*int(tch/st):(i*int(tch/st))+int(tch/st/10)-1,j])
                    meanN[i,j] = pd.DataFrame.mean(temp)
#%% Gets the variance of the last pextra points at every step
varN = np.zeros((int(actsteps),len(mut_d_add.T)))
pextra = 100
for i in range(int(actsteps)):
    for j in range(3):
        tempN = pd.Series(mut_d_add[i*int(tch/st)+pextra:(i*int(tch/st))+int(tch/st)-1,j])
        varN[i,j] = pd.DataFrame.var(tempN)        
        
#%% PLOTS

ticks1 = np.arange(1,0,-.05)
ticks2 = np.arange(1,0,-.1)
ticks3 = np.arange(0,3,1)
#time series
plt.figure(figsize=[3,6.5])
plt. subplot(2,1,1) 
for i in range(3):
    plt.plot(dch2,mut_d_add[:,i],color=colors[i],alpha=.6)

for i in range(3):
    plt.plot(chmea,meanN[:,i],color="white",linewidth=2, alpha=1)
plt.ylabel("abundance")
plt.xticks(ticks2)
plt.xlim(1,.83)
plt.ylim(-.1,2.3)
plt.yticks(ticks3)
#variance
plt. subplot(2,1,2) 
for i in range(3):
    plt.plot(chmea,varN[:,i],color=colors[i],linewidth=2, alpha=1,label=labels[i])
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,.001))
plt.ylabel("variance")
plt.xlabel("interaction strenght")
plt.xticks(ticks2)
plt.ylim(-.1e-2,2.6e-2)
plt.xlim(1,.8)
plt.legend()