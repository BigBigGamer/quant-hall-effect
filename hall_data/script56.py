import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from matplotlib.backends.backend_pdf import PdfPages
plt.rc('text', usetex = True)
plt.rc('font', size=13, family = 'serif')
plt.rc('text.latex',unicode=True)
plt.rc('legend', fontsize=14)
plt.rc('text.latex', preamble=r'\usepackage[russian]{babel}')


# Parazite Voltage

Parazite = pd.read_csv('hall_data/Parazite_hall_mod.tsv', delimiter = ',')
pz_I =np.array( Parazite['Iobr_mA'].tolist())
pz_U = np.array(Parazite['U_h_mV'].tolist())

# pz_I = np.array(pz_I)
# pz_U = np.array(pz_U)
# U_err = np.ones(pz_U.shape)*0.1
# I_err = np.ones(pz_I.shape)*0.025*10
# I_err[0:7] = 0.025*3

# pp = np.polyfit(pz_I,pz_U,2)
# pf = np.poly1d(pp)

mA1 = pd.read_csv('hall_data/task 5.6(0.25A).tsv', delimiter = ',')
mA2 = pd.read_csv('hall_data/task 5.6(0.5A).tsv', delimiter = ',')
mA3 = pd.read_csv('hall_data/task 5.6(0.75A).tsv', delimiter = ',')
mA7 = pd.read_csv('hall_data/task 5.6(1.0A).tsv', delimiter = ',')
B = 808 #gauss/amp
d = 3.3*10**(-4) #meters

mA1_I = np.array(mA1['Iobr_mA'].tolist())
mA1_Eh = np.array(mA1['E_Hall_mV'].tolist()) - pz_U
weights = np.zeros(mA1_I.shape)
weights[0:5] = 1
pp1,residuals, rank, singular_values, rcond = np.polyfit(mA1_I,mA1_Eh,1,w = weights, full = True)
pf1 = np.poly1d(pp1)
print('pp1 = ',pp1)
R1 = (pp1[0])/(202*10**(-4)) *d
print('R1 = ',R1)
r_sq = residuals/np.mean(mA1_Eh)
print('err,% = ',r_sq*100)


mA2_I = np.array(mA2['Iobr_mA'].tolist())
mA2_Eh = np.array(mA2['E_Hall_mV'].tolist())- pz_U
pp2,residuals, rank, singular_values, rcond = np.polyfit(mA2_I,mA2_Eh,1,w = weights, full = True)
pf2 = np.poly1d(pp2)
print('pp2 = ',pp2)
R2 = (pp2[0])/(404*10**(-4)) *d
print('R2 = ',R2)
r_sq = residuals/np.mean(mA2_Eh)
print('err,% = ',r_sq*100)



mA3_I = np.array(mA3['Iobr_mA'].tolist())
mA3_Eh = np.array(mA3['E_Hall_mV'].tolist()) - pz_U
pp3,residuals, rank, singular_values, rcond = np.polyfit(mA3_I,mA3_Eh,1,w = weights, full = True)
pf3 = np.poly1d(pp3)
print('pp3 = ',pp3)
R3 = (pp3[0])/(606*10**(-4)) *d
print('R3 = ',R3)
r_sq = residuals/np.mean(mA3_Eh)
print('err,% = ',r_sq*100)



mA7_I = np.array(mA7['Iobr_mA'].tolist())
mA7_Eh = np.array(mA7['E_Hall_mV'].tolist()) - pz_U
pp7,residuals, rank, singular_values, rcond = np.polyfit(mA7_I,mA7_Eh,1,w = weights, full = True)
pf7 = np.poly1d(pp7)
print('pp7 = ',pp7)
R7 = (pp7[0])/(808*10**(-4)) *d
print('R7 = ',R7)
r_sq = residuals/np.mean(mA7_Eh)
print('err,% = ',r_sq*100)


plt.plot(mA1_I,pf1(mA1_I),'r--',lw=1)
plt.plot(mA2_I,pf2(mA2_I),'g--',lw=1)
plt.plot(mA3_I,pf3(mA3_I),'k--',lw=1)
plt.plot(mA7_I,pf7(mA7_I),'b--',lw=1)



plt.plot(mA1_I,mA1_Eh,'ro-',label = '$B_{1}=200 ~Gs$')
plt.plot(mA2_I,mA2_Eh,'g*-',label = '$B_{2}=400 ~Gs$')
plt.plot(mA3_I,mA3_Eh,'k^-',label = '$B_{3}=600 ~Gs$')
plt.plot(mA7_I,mA7_Eh,'bs-',label = '$B_{4}=800 ~Gs$')
plt.grid(which='minor', linestyle='-',color = 'lightgrey')
plt.grid(which='major', linestyle='-',color = 'black')
plt.legend()
plt.ylabel('$V_{Hall},mV$')
plt.xlabel('$I_{sample},mA$')
plt.minorticks_on()


plt.show()
