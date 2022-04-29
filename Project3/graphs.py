# PDF of X

import matplotlib.pyplot as plt
import math

tau = 57
a = 1 / tau

# x axis values
x = []
for i in range(0, 350):
    x.append(i)

# corresponding y axis values
y = []
for i in x:
    exp_term = (-1/2) * math.pow(a, 2) * math.pow(i, 2)
    y.append(math.pow(a, 2) * i * math.exp(exp_term))

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('Distance away from T (inches)')
# naming the y axis
plt.ylabel('Probability')


# giving a title to my graph
plt.title('Probability of Drop Distance away from Origin Point T')

# function to show the plot
plt.show()
