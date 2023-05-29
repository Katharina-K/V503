import numpy as np
from numpy import sqrt
import pandas as pd
import scipy.constants as const
from scipy.optimize import curve_fit  
from scipy import special                      # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)
import matplotlib.pyplot as plt
import math 


poel=886
pluft=1.225
B=6.17*0.001*133.322
g=9.81
n=1.825*10**(-5)

v=np.array([0.05,0.04,0.03,0.05,0.03,0.02,0.04,0.05,0.02,0.04,0.03,0.03])
vauf1=np.array([0.11, 0.08,0.17,0.09,0.16,0.18])/1000
vauf2=np.array([0.16,0.17,0.14,0.1,0.16,0.22])/1000
vab1=np.array([0.16,0.11,0.21,0.14,0.19,0.2])/1000
vab2=np.array([0.19,0.22,0.16,0.14,0.19,0.25])/1000
E1=201/0.007625
E2=230/0.007625
r1=np.sqrt((9*n*v)/(4*g*(poel-pluft)))
p=1.013
q1=3*np.pi*n*np.sqrt((9/4)*(n/g)*((vab1-vauf1)/(poel-pluft)))*((vab1+vauf1)/E1)
q2=3*np.pi*n*np.sqrt((9/4)*(n/g)*((vab2-vauf2)/(poel-pluft)))*((vab2+vauf2)/E2)
q=np.hstack((q1,q2))

qn=(q**(2/3)*(1+(B/(p*r1))**(-1)))**(3/2)
print(qn*10**19)
#print(q1*10**19)
#print(q2*10**19)

a=[4.6705]
b=[5.2953, 5.9531]
c=[7.2989,7.6269,7.5178,7.5187]
d=[8.5683,8.6035]
e=[10.7862,10.8016,10.0977]
A=[4.6706]
B=[5.2621,5.9534]
C=[7.2999,7.6270,7.5189,7.5189]
D=[8.6037,8.5668]
E=[10.7863,10.8163,10.0984]

ua=ufloat(np.mean(a),np.std(a))
ub=ufloat(np.mean(b),np.std(b))
uc=ufloat(np.mean(c),np.std(c))
ud=ufloat(np.mean(d),np.std(d))
ue=ufloat(np.mean(e),np.std(e))

uA=ufloat(np.mean(A),np.std(A))
uB=ufloat(np.mean(B),np.std(B))
uC=ufloat(np.mean(C),np.std(C))
uD=ufloat(np.mean(D),np.std(D))
uE=ufloat(np.mean(E),np.std(E))
#print(ua,ub,uc,ud,ue)

d1=ub-ua
d2=uc-ub
d3=ud-uc
d4=ue-ud
diff=[d1,d2,d3,d4]
udiff=sum(diff)/4
#print(f'Diff= {udiff:.4f}')

D1=uB-uA
D2=uC-uB
D3=uD-uC
D4=uE-uD
Diff=[D1,D2,D3,D4]
uDiff=sum(Diff)/4
#print(f'Diff2= {uDiff:.4f}')
F=96485.339

N=F/udiff
NK=F/uDiff


print(f'N= {N:.4f}')
print(f'Nk= {NK:.4f}')