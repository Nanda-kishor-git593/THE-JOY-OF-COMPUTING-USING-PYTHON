


from statistics import mean
from scipy import stats
Estimates = [1000.1010,1786,2000,1500,1500,100,120,150,150,200,350,300,256,374,376,299,800,375,400,600,830,100,20,365,90]
Estimates.sort()
m = stats.trim_mean(Estimates,0.1)
print(m)

'''tv =int(0.1*len(Estimates))
Estimates=Estimates[tv:]
for i in range(len(Estimates)):
    print(Estimates[i])
Estimates=Estimates[:len(Estimates)-tv]
print(mean(Estimates))
'''

