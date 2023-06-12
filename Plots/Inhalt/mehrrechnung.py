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


t1auf=np.array([4.76,6.84,4.7,3.24,4.72,3.07,2.41,2.7,3.6,3.66,2.93,3.68,6.23,2.57,5.03,2.97,3.82,2.5,2.86,2.21,2.53,2.17])
t2auf=np.array([4.23,6.91,3.13,2.62,5.56,3.27,2.44,2.94,3.72,2.91,2.86,3.61,7.02,2.77,5.02,3.15,3.66,2.48,3.51,2.33,2.68,2.12])
t3auf=np.array([4.47, 5.6,3.33,2.72,5.77,3.16,2.54,2.86,4.09,3.01,2.91,3.72,7.49,2.93,5.31,3.17,3.82,2.43,2.96,2.4,2.75,2.05])
tab1=np.array([3.13,4.54,2.66,2.59,3.2,2.52,2.39,2.62 ,3.87,2.52,2.05,2.83,5.58,2.6,3.7,3.06,2.89,1.97,2.37,1.95,2.11,1.99])
tab2=np.array([3.15, 4.38,2.61,2.2,3.67,2.72,2.4,2.58,3.78,2.71,2.41,3.29,6.32,2.88,3.58,2.69,2.58,2.24,2.62,2.04,2.1,2.38])
tab3=np.array([3.22,4.13,2.59 ,2.5 ,3.52,2.7,2.38,2.43,3.7,2.58,2.26,3.24,5.47,2.61,3.58,2.82,2.97,2.4,2.96,2.14,2.25,2.28])

error=0.1

ut1auf=np.empty_like(t1auf, dtype=object)
ut2auf=np.empty_like(t1auf, dtype=object)
ut3auf=np.empty_like(t1auf, dtype=object)
utab1=np.empty_like(t1auf, dtype=object)
utab2=np.empty_like(t1auf, dtype=object)
utab3=np.empty_like(t1auf, dtype=object)

zeiten=[t1auf,t2auf,t3auf,tab1,tab2,tab3]
uzeiten=[ut1auf,ut2auf,ut3auf,utab1,utab2,utab3]

for n in range(0,6):
    for i, value in np.ndenumerate(zeiten[n]):
            uzeiten[n][i] = ufloat(value, error)


tabm=np.empty_like(t1auf, dtype=object)
taufm=np.empty_like(t1auf, dtype=object)

for i in range(0,22):
      tabm[i]=(utab1[i]+utab2[i]+utab3[i])/3
      taufm[i]=(ut1auf[i]+ut2auf[i]+ut3auf[i])/3
print(tabm)
print(taufm)
      
      

