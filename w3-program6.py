# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 17:16:00 2025

@author: rgukt
"""

#ploting estimates made by the croud

import statistics
import matplotlib .pyplot as plt
Estimates = [1000.1010,1786,2000,1500,1500,100,120,150,150,200,350,300,256,374,376,299,800,375,400,600,830,100,20,365,90]
#plt.plot(Estimates)
# if you not given x values. python generates its x values on its own
# i jest want show estimates.
# i will keep constatant y values. for taht i create another array y[]
y = []
'''for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates,y,'r--')
'''
# no wwnat to plot mean and median , that i got to know that which values or nearer to the actuval value
Estimates.sort()
tv=int(0.1*(len(Estimates)))
Estimates=Estimates[tv:]
Estimates=Estimates[:len(Estimates)-tv] # array obtain from trimmed values to len of estimates - trimmed value
for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates,y,'r--')  # shows trimmed plot
#show nearer to actual value
plt.plot([statistics.mean(Estimates)],[5],'ro')
plt.plot([statistics.median(Estimates)],[5],'bs')
plt.plot([450],[5],'g^')


