import matplotlib.pyplot as plt
import random
import statistics

a = [0] # χρονοσειρα με 1 στοιχειο μονο, η αρχικη θεση ειναι 0
s=1     # παραγοντας που αλλαζει τη διασπορα
for x in range(1,10000):  #για  1-10000 τιμες
    a.append(a[-1] + s * random.randint(-1,1)) #dx=x+x1-γ*t α(-1) ειναι η τελευταια θεση που ειχα
print(statistics.mean(a)) #μεση τιμη 
print(statistics.variance(a))   #διασπορα

plt.plot(a)  #γραφημα
plt.show()


a = [0] # χρονοσειρα με 1 στοιχειο μονο, η αρχικη θεση ειναι 0
g = 2   #γ παραμετρος
s = 1
for x in range(1,1000):
    a.append(a[-1] - (g * a[-1]) + s * random.randint(-1,1)) #χt+1=xt-γ*xt+σ*dw
print(statistics.mean(a)) #μεση τιμη 
print(statistics.variance(a))   #διασπορα

plt.plot(a)
plt.show()
