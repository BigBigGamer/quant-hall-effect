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


## Parazite Voltage

# Parazite = pd.read_csv('hall_data/Parazite_hall.tsv', delimiter = '\t')
# pz_I = Parazite['Iobr,mA'].tolist()
# pz_U = Parazite['U_h,mV'].tolist()

# pz_I = np.array(pz_I)
# pz_U = np.array(pz_U)
# U_err = np.ones(pz_U.shape)*0.1
# I_err = np.ones(pz_I.shape)*0.025*10
# I_err[0:7] = 0.025*3

# pp = np.polyfit(pz_I,pz_U,2)
# pf = np.poly1d(pp)

mA1 = pd.read_csv('hall_data/task 5.5(1mA).tsv', delimiter = '\t')
mA2 = pd.read_csv('hall_data/task 5.5(2mA).tsv', delimiter = '\t')
mA3 = pd.read_csv('hall_data/task 5.5(3mA).tsv', delimiter = ',')
mA7 = pd.read_csv('hall_data/task 5.5(7mA).tsv', delimiter = '\t')
B = 808 #gauss/amp
d = 3.3*10**(-4) #meters

mA1_I = np.array(mA1['I_h-field,A'].tolist())
mA1_Eh = np.array(mA1['E_Hall,mV'].tolist())
mA1_B = B*mA1_I
pp1 = np.polyfit(mA1_B,mA1_Eh,1)
pf1 = np.poly1d(pp1)
print('pp1 = ',pp1)
R1 = 10*(pp1[0])/(0.001) *d
print('R1 = ',R1)

mA2_I = np.array(mA2['I_h-field_A'].tolist())
mA2_Eh = np.array(mA2['E_Hall_mV'].tolist())
mA2_B = B*mA2_I
pp2 = np.polyfit(mA2_B,mA2_Eh,1)
pf2 = np.poly1d(pp2)
print('pp2 = ',pp2)
R2 = 10*(pp2[0])/(0.002) *d
print('R2 = ',R2)


mA3_I = np.array(mA3['I_h-field_A'].tolist())
mA3_Eh = np.array(mA3['E_Hall_mV'].tolist()) 
mA3_B = B*mA3_I
pp3 = np.polyfit(mA3_B,mA3_Eh,1)
pf3 = np.poly1d(pp3)
print('pp3 = ',pp1)
R3 = 10*(pp3[0])/(0.003) *d
print('R3 = ',R3)

mA7_I = np.array(mA7['I_h-field,A'].tolist())
mA7_Eh = np.array(mA7['E_Hall,mV'].tolist()) 
mA7_B = B*mA7_I
pp7 = np.polyfit(mA7_B,mA7_Eh,1)
pf7 = np.poly1d(pp7)
print('pp1 = ',pp1)
R7 = 10*(pp7[0])/(0.007) *d
print('R7 = ',R7)

plt.plot(mA1_B,pf1(mA1_B),'r--',lw=1)
plt.plot(mA2_B,pf2(mA2_B),'g--',lw=1)
plt.plot(mA3_B,pf3(mA3_B),'k--',lw=1)
plt.plot(mA7_B,pf7(mA7_B),'b--',lw=1)



plt.plot(mA1_B,mA1_Eh,'ro-',label = '$I_{sample}=1 mA$')
plt.plot(mA2_B,mA2_Eh,'g*-',label = '$I_{sample}=2 mA$')
plt.plot(mA3_B,mA3_Eh,'k^-',label = '$I_{sample}=3 mA$')
plt.plot(mA7_B,mA7_Eh,'bs-',label = '$I_{sample}=7 mA$')
plt.grid(which='minor', linestyle='-',color = 'lightgrey')
plt.grid(which='major', linestyle='-',color = 'black')
plt.legend()
plt.ylabel('$V_{Hall},mV$')
plt.xlabel('$B,Gauss$')
plt.minorticks_on()
# H1 = pd.read_csv('hall_data/task 5.6(0.75A).tsv', delimiter = '\t')
# H1_i = H1['Iobr,mA'].tolist()
# H1_Eh = H1['E_Hall,mV'].tolist()

# plt.figure(2)
# plt.grid(which = 'both')
# plt.title('H~600 gs')
# plt.xlabel('E_hall,mV')
# plt.ylabel('Iobr,mA')
# plt.plot(H1_Eh,H1_i)


plt.show()
