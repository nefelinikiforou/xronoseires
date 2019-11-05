# Κωνσταντίνος Ξυπολιτόπουλος - Χρονοσειρές και Στοχαστικές Διαδικασίες - 23/10/2019
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rvals = np.random.rand(100000) # random values
timevals = np.arange(0,200000,2) # time from 0 to 2000 in steps of 2
d = pd.Series(data=rvals, index=timevals) # stitch them into a pandas series object, with time position as the index, and the random value as the values of the series

gammaOfT = []
varIo = d.var() # this stays the same so we're calculating it here
window = range(1,50)
for w in window:
    gammaOfT.append((d.rolling(window=w).mean()).var()/varIo) # calculate γ(τ) = var(Iτ) / var(Iο) for all 50 windows then add it to the list

plt.scatter(window, gammaOfT, marker=".") # plot the γ(τ) values along with the τ (window) sizes
#plt.xscale("log")
#plt.yscale("log")
plt.xlabel("Window size (τ)")
plt.ylabel("$γ_τ$", rotation=0)




from numpy.polynomial.polynomial import polyfit
x = np.log(window)
y = np.log(gammaOfT)

# fitting with numpy polyfit
b, a = polyfit(x, y, 1) # "x,y" are the sample points - "1" is the degree of the fitting polynomial, here it's a first degree polymonial, a straight line.

plt.plot(x, y, '.')
plt.plot(x, a*x + b, '-') # Plot x and f(x)=ax+b
#plt.plot(x, -1*x + b, '-') # Plot -x+b
plt.xlabel("Window size (τ) (log)")
plt.ylabel("$γ_τ$ (log)", rotation=0)
plt.show()
print(a) # Coefficient of the line is ~-1
