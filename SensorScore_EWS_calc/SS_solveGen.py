#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 18:37:26 2021

@author: andreaapariciomartinez
"""
#%%
import numpy as np
import sdeint
import csv
import pandas as pd
import sys
import math as mt
# from scipy import integrate as scint
fn = int(sys.argv[1]) #to run for a specific network, without passing parameters from the console, comment this line and uncomment the next one
# fn = "M_SD_002" #If uncommented, enter the network matrix csv filename here. The matrix must be rectangular and have plants as rows and animals as columns

#%% simulation parameters 
chsteps = 70 # parameter goes from 1 to 0 in these many steps
tch = 50 # sims run for this amount of time before changing the parameter
tini = 0.0 #initial time
st = .01 #step size
tmax= tch*chsteps+(2*tch) #final time 
tarray=np.arange(tini,tmax,st)
dch = np.zeros(len(tarray)) #stores the values of the parameter for plots
for i in range(len(dch)):
    dch[i] = 1-((1/chsteps)*np.floor((tarray[i])/tch))
dchc=np.arange(1,0,-1/len(tarray))
p_start=1 #value to start the decreasing parameter
selfW = -1 #self loop

#%% model parameters
B0 = 2 #nominal
# B0 = 1 #low
# B0 = 3 #High
delta = 0.5 #nominal 
# delta = 0.25 #low
# delta = 1 #high
g0 = 120 #nominal
# g0 = 80 #low
# g0 = 160 #high
#**** g0 for secuential extintions
# c = 3 # 15 # 75
# tau = 0.31 #Missim
# tau = 0.41 #Genebra
# tau = 0.43 #Calton
# g0 = c*tau
#****
h = .01 # nominal
# h = 0.001 #low
# h = 0.1 #high
omegax = 10 #nominal
# omegax = 0.1 #very low
# omegax = 1 # low
#%% folders
folderd = "data/" #data destination folder

#%% build bin matrix
def buildMat_f(file_n, save=0):

    with open(folderd+file_n+'.csv') as csvfile:
             mutnet = list(csv.reader(csvfile,quoting=csv.QUOTE_NONNUMERIC)) #mutualistic network
    MutNet = np.array(mutnet)        
    
    #% build community network from mutualistic matrix
    At = np.zeros((np.sum(MutNet.shape),np.sum(MutNet.shape)))
    
#    sp_num = len(At) #number of species
    P_num = MutNet.shape[0] #number of plants (rows)
    A_num = MutNet.shape[1] #number of animals (columns)
    
    # add plant-animal interactions first plants and then animals
    for i in range(P_num):
        for j in range(A_num):
            if MutNet[i,j] != 0:
                At[i,j+P_num] = MutNet[i,j]

    
    # add mutualistic interactions
    As= At+At.T 
    Abin = np.zeros(As.shape)
    
    #make a binary matrix
    for i in range(As.shape[0]):
        for j in range(As.shape[1]):
            if At[i,j]!=0:
                Abin[i,j]=int(1)              
    Abins = Abin+Abin.T
    
    ##%% save files
    if save ==1:
        np.savetxt(file_n+"_Anotsym.csv",Abin)
        np.savetxt(file_n+'_A.csv',As)
        np.savetxt(file_n+'_Ab.csv',Abins)
        
#    return [As, Abins]
    return Abins

#%% build competition matrix    
def compMat_f(Abin, P_num, A_num):

    MutNet = Abin[0:p_num, p_num:]
    compM = np.zeros((Abin.shape))
    
    # add  plant-plant competition
    for i in range(P_num):
        for j in range(A_num):
            if MutNet[i,j] !=0:
                for k in range(i+1,P_num,1):
                    if MutNet[k,j]!=0:
                        compM[i,k]=-1
    
    # add  animal-animal competition
                        
    for j in range(A_num):
        for i in range(P_num):
            if MutNet[i,j]!=0:
                for k in range(j+1,A_num,1):
                    if MutNet[i,k]!=0:
                        compM[j+P_num,k+P_num]=-1    

    return [compM, P_num, A_num]

#%% Function to change a parameter from p_start to 0, in chsteps of tch time length
def calc_d(t):
    d = p_start-((p_start/chsteps)*np.floor((t)/tch)) 
    if d<0:
        d=0
    return d

#%% calculate variance, autocorrelation, means and take a sample of timeseries
    #saves the data in the specified folder
def calcs_ts(Muts1,k,fn):

    posr=100
    pextra = 200 #skips these steps after every change to avoid transitory jumps
    int(tch/st)-1
    ind = np.arange(0,int(tch/st)-1-pextra,int((int(tch/st)-1-pextra)/posr+1))
    
    varM = np.zeros((int(chsteps),len(Muts1.T)))
    meanM = np.zeros((int(chsteps),len(Muts1.T)))
    sampM = np.zeros((int(chsteps*posr),len(Muts1.T)))
    acM = np.zeros((int(chsteps),len(Muts1.T)))

    
    for i in range(int(chsteps)):
        for j in range(len(Muts1.T)):
            tempM = pd.Series(Muts1[i*int(tch/st)+pextra:(i*int(tch/st))+int(tch/st)-1,j])
            varM[i,j] = pd.DataFrame.var(tempM)
            meanM[i,j] = pd.DataFrame.mean(tempM)
            sampM[(i*posr):(i*posr)+posr,j] =  np.array(tempM[ind])
            acM[i,j] = tempM.autocorr()

#% save data

    np.savetxt(folderd+"data_sims/"+fn+"_var_reps_"+str(k)+".csv", varM)
    np.savetxt(folderd+"data_sims/"+fn+"_mean_reps_"+str(k)+".csv", meanM)
    np.savetxt(folderd+"data_sims/"+fn+"_samp_reps_"+str(k)+".csv", sampM)
    np.savetxt(folderd+"data_sims/"+fn+"_ac_reps_"+str(k)+".csv", acM)
    
    print(["saved ts metrics",fn,k])
    
    calc_EWS(varM,k,fn)
    
#%% Mutualistic dynamics
def Mut_eq(x,t):    
    dx = np.zeros(len(A))
   
    d = calc_d(t) #parameter that changes

    x[x<0]=0
    
    for i in range(len(A)): #system dynamics
        dx[i] = x[i]*(r[i]+selfW*x[i]-np.matmul(Ac[i,:],x)+((d*np.matmul(A[i,:],x))/(1+h*d*np.matmul(A[i,:],x))))
    
    return dx
    
#%% additive noise 
def addN_eq(x,t):
    gv=omegax*np.ones(len(x))
    return np.diag(gv)


#%%
def defRealiz(Abin,compM,pn,an, r_sp):
##%% Add weights to interactions matrix
  
    At = np.zeros(Abin.shape)
    for i in r_sp:
        for j in r_sp:
            if Abin[i,j]!=0:
                At[i,j] = g0*Abin[i,j]/((np.sum(Abin[i,:])/2)**delta)
##%% Add weights to competition matrix
    Ac = np.zeros(compM.shape)
    Bp = 1/pn
    Ba = 1/an
    
    #add competition 
    for i in range(pn):
        for j in range(pn):
            if compM[i,j]!=0:
                Ac[i,j] =  np.random.uniform(.005, B0*Bp)
    for i in range(pn,sp_n,1):
        for j in range(pn,sp_n,1):
            if compM[i,j]!=0:
                Ac[i,j] =  np.random.uniform(.005, B0*Ba) 
   ##%% get random initial conditions 
    x0m = 0 #minimum
    x0M = 10 #maximum
    x0 = (x0M-x0m)*np.random.random_sample(len(At))+x0m
    x0 = x0.T 
##%% get random growth rate
    rmin = -.5
    rmax = -.1
    r = (rmin-rmax)*np.random.random_sample(len(At))+rmin 

    A=At
    
    return [A,Ac,x0,r]

#%%
def calc_EWS(varM0,k,fn):   
    sp = len(varM0.T)    
    chsteps = len(varM0)
    
##%% calculate slope for a rolling window
    win = mt.ceil(chsteps/3)
    polyf0 = np.zeros((chsteps-win,sp))
    a=range(win)
    for i in range(chsteps-win):
        for j in range(sp):
            polyf0[i,j] = np.polyfit(a,varM0[i:i+win,j],1)[0]
  
##%% calculate Early Warning Score (when slope is never negative again)
    detection0t = win*np.ones(sp)
 
    for j in range(sp):
        for i in range(chsteps-win):
            if polyf0[chsteps-win-1-i,j]<=0:
                detection0t[j] = chsteps-i
                break

    detection0 = 1-detection0t/chsteps
    
    np.savetxt(folderd+"data_EWS/"+fn+"EWS"+str(k)+".csv", detection0)
    
    print(["saved EWS",fn,k])
#%% get bin matrix
Abin = buildMat_f(fn,0)

#%% get network params
sp_n = len(Abin)
r_sp = range(sp_n)      
p_num = int(np.argwhere(Abin[0]==1)[0].flatten())
a_num = sp_n - p_num

#%%
kini = int(sys.argv[2])
kfin = int(sys.argv[3])

for k in range(kini,kfin):
    ## %%
    # k=100 
    print("realiz"+str(k))
    [compM, pn, an] = compMat_f(Abin, p_num, a_num) #get competition matrix and number of plants and animals
    ##%% solve stochastic system
    [A,Ac,x0,r] = defRealiz(Abin,compM,pn,an,r_sp)
    # solve deterministic system
    # Muts1=scint.odeint(Mut_eq,x0,tarray)    
    print("sim "+str(k)+" start")
    Muts1 = sdeint.itoSRI2(Mut_eq, addN_eq, x0, tarray)
    print("sim "+str(k)+" done")
    #calculations
    calcs_ts(Muts1,k,fn)
    print(str(k)+" saved")     
