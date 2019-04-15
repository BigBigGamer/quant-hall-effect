import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from matplotlib.backends.backend_pdf import PdfPages
plt.rc('text', usetex = True)
plt.rc('font', size=13, family = 'serif')
# plt.rc('text.latex',unicode=True)
plt.rc('legend', fontsize=14)
plt.rc('text.latex', preamble=r'\usepackage[russian]{babel}')


## Parazite Voltage

Parazite = pd.read_csv('hall_data/Parazite_hall.tsv', delimiter = '\t')
pz_I = Parazite['Iobr,mA'].tolist()
pz_U = Parazite['U_h,mV'].tolist()

pz_I = np.array(pz_I)
pz_U = np.array(pz_U)
U_err = np.ones(pz_U.shape)*0.1
I_err = np.ones(pz_I.shape)*0.025*10
I_err[0:7] = 0.025*3

pp = np.polyfit(pz_I,pz_U,2)
pf = np.poly1d(pp)
plt.figure(0)

plt.plot(pz_I,pf(pz_I),'-',color = 'k')
plt.errorbar(pz_I,pz_U,yerr = U_err,xerr =I_err  ,color = 'k',linestyle='',capsize = 2)
plt.plot(pz_I,pz_U,'o',color = 'red')
plt.grid(which='minor', linestyle='-',color = 'lightgrey')
plt.grid(which='major', linestyle='-',color = 'black')
plt.ylabel('$U_{parazite},mV$')
plt.xlabel('$I_{sample},mA$')
plt.minorticks_on()
# plt.savefig('graphs/paraz.png',dpi=500)

## Parazite Voltage


# Volt-Amp

# va = pd.read_csv('hall_data/task 5.2.tsv', delimiter = '\t')
# I = va['I,mA'].tolist()
# U = va['Uobr,V'].tolist()
# I = np.array(I)
# U = np.array(U)
# U_err = np.ones(U.shape)*0.05
# I_err = np.ones(I.shape)*0.025*10
# # I_err[0:7] = 0.025*3
# R1 = 1621
# U = U - 0.001*I*R1 
# print(I,U)
# pp2 = np.polyfit(U,I,1)
# pf2 = np.poly1d(pp2)
# print(pp2)

# plt.plot(U,pf2(U),'-',color = 'k')
# plt.errorbar(U,I,yerr = I_err,xerr =U_err  ,color = 'k',linestyle='',capsize = 2)
# plt.plot(U,I,'ro')
# plt.grid(which='minor', linestyle='-',color = 'lightgrey')
# plt.grid(which='major', linestyle='-',color = 'black')
# plt.xlabel('$U_{sample},V$')
# plt.ylabel('$I_{sample},mA$')
# plt.minorticks_on()
# plt.savefig('graphs/voltamp.png',dpi=500)

## Volt-Amp



# mA1 = pd.read_csv('hall_data/task 5.5(2mA).tsv', delimiter = '\t')
# mA1_I = mA1['I_h-field,A'].tolist()
# mA1_Eh = mA1['E_Hall,mV'].tolist()


# plt.figure(1)
# plt.grid(which = 'both')
# plt.title('Iobr = 2mA')
# plt.xlabel('E_hall,mV')
# plt.ylabel('I_h,A')
# plt.plot(mA1_Eh,mA1_I)

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
