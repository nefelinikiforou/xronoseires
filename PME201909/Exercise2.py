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

### SINGLE RUNS - GRAPHS ###

#Weiner
mylist = [0]
for x in enumerate(range(0,10000)):
    mylist.append(mylist[-1] + s*rnd.randint(-1,1)) # we don't give a fuck about x's current value here

plt.grid()
plt.title("Weiner")
plt.plot(mylist)
plt.show()

# Ornstein
gamma = 2
mylist = [0]
for x in enumerate(range(0,200)):
    mylist.append(mylist[-1] - gamma*mylist[-1] + s*rnd.randint(-1,1)) # we don't give a fuck about x's current value here 
    
plt.close()
plt.grid()
plt.title("Ornstein")
plt.plot(mylist)
plt.show()
