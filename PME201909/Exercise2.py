# Κωνσταντίνος Ξυπολιτόπουλος - Χρονοσειρές και Στοχαστικές Διαδικασίες - 11/5/2019
import numpy as np
import pandas as pd
import random as rnd
import math
import statistics as st
import matplotlib.pyplot as plt

#Weiner
for s in range(1,20,4):
    overall_mean = 0
    overall_variance = 0
    for times in range(0,100): # 100 repetitions for statistical mean/variance
        mylist = [0]
        for x in enumerate(range(0,10000)):
            mylist.append(mylist[-1] + s*rnd.randint(-1,1)) # we don't care about x's current value here
        overall_mean += st.mean(mylist)
        overall_variance += st.variance(mylist)
    print(f"s:{s}, mean:{overall_mean}, variance:{math.sqrt(overall_variance)}")

# Ornstein
for s in range(1,20,4):
    gamma = 2
    overall_mean = 0
    overall_variance = 0
    for times in range(0,100): # 100 repetitions for statistical mean/variance
        mylist = [0]
        for x in enumerate(range(0,1000)):
            mylist.append(mylist[-1] - gamma*mylist[-1] + s*rnd.randint(-1,1)) # we don't care about x's current value here 
        overall_mean += st.mean(mylist)
        overall_variance += st.variance(mylist)
    print(f"s:{s}, mean:{overall_mean}, variance:{math.sqrt(overall_variance)}")

### SINGLE RUNS ###

#Weiner
s=1
mylist = [0]
for x in enumerate(range(0,10000)):
    mylist.append(mylist[-1] + s*rnd.randint(-1,1)) # we don't give a fuck about x's current value here

plt.grid()
plt.title("Weiner")
plt.plot(mylist)
plt.show()
plt.close()

# Autocorrelation
rvals = np.array(mylist)
timevals = np.arange(0,10001)
d = pd.Series(data=rvals, index=timevals)
gammaOfT = []
varIo = d.var()
window = range(1,50)
for w in window:
    gammaOfT.append((d.rolling(window=w).mean()).var()/varIo)

plt.scatter(window[1:-1], gammaOfT[1:-1], marker=".")
plt.xlabel("Window size (τ)")
plt.ylabel("$γ_τ$", rotation=0)
plt.title("Autocorrelation of Weiner process")
plt.show()
plt.close()

from numpy.polynomial.polynomial import polyfit

x = window[1:-1] 
y = gammaOfT[1:-1] 
b, a = polyfit(x, y, 1)
plt.plot(x, y, '.')
plt.plot(x, a*x + b, '-')
plt.xlabel("Window size (τ)")
plt.ylabel("$γ_τ$", rotation=0)
plt.title("(Linear) Autocorrelation of a Weiner process")
plt.show()
print(f"Coefficient of the line: {a}")

# Linear autocorrelation is a telltale sign of a wiener process random walker



# Dragon Slayer Ornstein
s=1
plt.close()
gamma = 2
mylist = [0]
for x in enumerate(range(0,9999)):
    mylist.append(mylist[-1] - gamma*mylist[-1] + s*rnd.uniform(-1, 1)) # we don't give a fuck about x's current value here 
    
plt.grid()
plt.title("Ornstein")
plt.plot(mylist)
plt.show()
plt.close()

# Autocorrelation
rvals = np.array(mylist)
timevals = np.arange(0,10000)
d = pd.Series(data=rvals, index=timevals)
gammaOfT = []
varIo = d.var()
window = range(1,50)
for w in window:
    gammaOfT.append((d.rolling(window=w).mean()).var()/varIo)

plt.scatter(window[1:-1], gammaOfT[1:-1], marker=".")
plt.xlabel("Window size (τ)")
plt.ylabel("$γ_τ$", rotation=0)
plt.title("Autocorrelation of Ornstein process")
plt.show()
plt.close()

from numpy.polynomial.polynomial import polyfit
x = window[1:-1]  #np.log(window)
y = gammaOfT[1:-1] #np.log(gammaOfT)
b, a = polyfit(x, y, 1)
plt.plot(x, y, '.')
#plt.plot(x, a*x + b, '-')
plt.xlabel("Window size (τ)")
plt.ylabel("$γ_τ$", rotation=0)
plt.show()
print(f"Coefficient of the line: {a}")

#print(x)
#print(y)
plt.close()

# Some observations:
# If we set Gamma(γ)=0 it eliminates the extra term and turns this into a Weiner process with linear autocorrelation.
# If we also set Gamma(γ)=1 it becomes a random process with a power law distribution (because: χ - γ*χ + σ*dW= σ*dW)
