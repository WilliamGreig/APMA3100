# circles for q3.

import matplotlib.pyplot as plt
import math
import numpy as np

tau = 57
a = 1 / tau

# x axis values
x = []
for i in range(0, 350):
    x.append(i)

figure, axes = plt.subplots()

# takes probability and returns distance
def inverse(p):
    x = (-2) * np.log(1 - p) / math.pow(a, 2)
    return math.sqrt(x)

Drawing_uncolored_circle1 = plt.Circle( (0, 0),
                                      inverse(0.5),
                                      fill = False,
                                        color="blue")

Drawing_uncolored_circle2 = plt.Circle( (0, 0),
                                      inverse(0.7),
                                      fill = False,
                                        color="red")


Drawing_uncolored_circle3 = plt.Circle( (0, 0),
                                      inverse(0.9),
                                      fill = False,
                                        color="green")

max_dist = 150
plt.xlim([0, max_dist])
plt.ylim([0, max_dist])



axes.legend([Drawing_uncolored_circle1, Drawing_uncolored_circle2, Drawing_uncolored_circle3], ['blue: p=0.5', 'red: p=0.7', 'green: p=0.9'])
# axes.set_aspect( 1 )
axes.add_artist( Drawing_uncolored_circle1 )
axes.add_artist( Drawing_uncolored_circle2 )
axes.add_artist( Drawing_uncolored_circle3 )

print(inverse(0.5))
plt.title( 'Probability of Drone Delivery within Specified Distance from Origin' )
plt.xlabel('X Distance away from T (inches)')
plt.ylabel('Y Distance away from T (inches)')

plt.show()
