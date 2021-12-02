# SensorSpecies

This is a repository for the paper "Structure-based identification of sensor species for anticipating critical transitions" by  Andrea Aparicio, Jorge X. Velasco, Claude H. Moog, Yang-Yu Liu, and Marco Tulio Angulo.

USER INSTRUCTIONS

##	I.	To calculate the sensor score, early-warning score and (q^*, r_1) predictions for a mutualistic system, and obtain the network diagram (Figure 2):
1.	Save in “data/“ the system’s interaction matrix in csv format ("sys_name.csv”). The matrix must be rectangular and have plants as rows and animals as columns.

3.	In “SensorScore_EWS_calc/Sensor_score_calc.nb” enter the filename (without the extension), in the field fn (for Genebra:).

![Screen Shot 2021-09-20 at 9 35 20 PM](https://user-images.githubusercontent.com/72633616/134099010-f72ca772-746c-4e3c-adc0-48b8815654ca.png)

3.	Run the main function. The results will be shown inline (for Genebra:).
	
![Screen Shot 2021-09-20 at 9 35 36 PM](https://user-images.githubusercontent.com/72633616/134099011-46e9a38f-5f73-4efe-ab70-0dfd65b06406.png)
![SS_calc_ex_out](https://user-images.githubusercontent.com/72633616/134098818-6158de3c-6140-4bc8-a72a-97620d2747f4.png)

##	II.	To simulate a critical transition in one or more realizations of a mutualistic system with the parameters in Table S3 (nominal parameters)		
1.	Save in “data/“ the system’s interaction matrix in csv format ("sys_name.csv”). The matrix must be rectangular and have plants as rows and animals as columns.

2.	Define     <br />
kStart  = initial realization number (must be > 0) <br />
kEnd = final realization number (must be > kStart)

3.	Run the script “SensorScore_EWS_calc/SS_solveGen.py” as:  
` python SS_solveGen.py sys_name kStart kEnd ` 

4.	Find the results in csv format in <br />
+	"data/data_sims/“:<br />
⁃	the variance of the abundance of every species at every \mu step ("sysname_var_reps_k.csv") <br />
⁃	the autocorrelation of the abundance of every species at every \mu step ("sysname_ac_reps_k.csv") <br />
⁃	the mean of the abundance of every species at every \mu step ("sysname_var_mean_k.csv") <br />
⁃	a sample of the abundance at every \mu step ("sysname_samp_reps_k.csv")

+	"data/data_EWS/"<br />
⁃	early-warning scores of every species (first plants and then animals) ("sysnameEWSk.csv") <br />

##	III.	To analyze the time-series obtained after simulating a critical transition on a mutualistic system, and obtain the plots in Figures 2 and 3

 1.	Make sure that the interaction matrix is saved as in I.1, that the data is stored as indicated in II.4, and have (kStart kEnd) from II.2 handy
 2.	Define kT: one particular realization to display (must be \in (kStart,kEnd])
 3.	In “SensorScore_EWS_calc/EW_score_calc.nb” enter <br />
     ⁃	the filename (without the extension), in the field fn 	<br />
     ⁃	kStart, KEnd and kT in the fields of the same name <br />
 4.	Run the main function. The results will be shown inline.

##	IV.	To generate the plots in Figure 1
 1.	Run the script “All_Figs/Toy_Mutualistic.py”

##	V.	To generate the plots in Figure 4 and Figures S6-S14, find the corresponding script using the list below, and follow the instructions on its README file:
 ⁃	Fig.4,      All_Figs/General_figs.nb    
 ⁃	Fig.S4,      SensorScore_EWS_calc/Sensor_score_calc.nb, SS_solveGen.py, EW_score_calc.nb    
 ⁃	Fig.S5,     SensorScore_EWS_calc/EW_score_calc.nb    
 ⁃	Fig.S6,     All_Figs/General_figs.nb    
 ⁃	Fig.S7,     All_Figs/General_figs.nb    
 ⁃	Fig.S8,     All_Figs/ Fig_S8_S9.nb    
 ⁃	Fig.S9,     All_Figs/ Fig_S8_S9.nb    
 ⁃	Fig.S10,     SensorScore_EWS_calc/ SS_solveGen.py, All_Figs/ Fig_S10-11-12.nb    
 ⁃	Fig.S11,     SensorScore_EWS_calc/ SS_solveGen.py, All_Figs/ Fig_S10-11-12.nb    
 ⁃	Fig.S12,     SensorScore_EWS_calc/ SS_solveGen.py, All_Figs/ Fig_S10-11-12.nb    
 ⁃	Fig.S13,     All_Figs/FigS13.nb    
 ⁃	Fig.S14,     All_Figs/FigS14.nb    

