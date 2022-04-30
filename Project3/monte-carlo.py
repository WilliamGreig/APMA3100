import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

x_0 = 1000
a = 24693
c = 3967
K = math.pow(2, 18)

x_list = [x_0]
u_list = []

def rng():
    # get most recent value
    i = len(x_list)
    value = a * x_list[i - 1] + c
    remainder = value % K
    x_list.append(remainder)
    u_list.append(x_list[i] / K)
    return u_list[len(u_list) - 1]

""" Numbers for Report:
u_51: 0.19949
u_52: 0.20005
u_53: 0.04691
"""

# takes probability and returns distance -- inverse of CDF of X
def inverse(p):
    tau = 57
    a_0 = 1 / tau
    q = (-2) * np.log(1 - p) / math.pow(a_0, 2)
    return math.sqrt(q)

# performs monte_carlo simulation on n different realizations of X
def monte_carlo(s):
    xSum = 0
    for i in range(s):
        # realization of X
        X = inverse(rng())
        xSum = xSum + X
    samp_mean = xSum / s
    return samp_mean

# performs n monte carlo simulations for a sample size of s
def repeated_monte_carlo(n, s):
    esti_sum = 0
    for i in range(n):
        monte_result = monte_carlo(s)
        esti_sum = esti_sum + monte_result
    estimated_mean = esti_sum / n

    return estimated_mean

realizations = 110
list_of_samples = [10, 140, 50, 100, 250, 500, 1000]
# n -- number of samples
x_axis = []
# m_n -- result of monte-carlo
y_axis = []
count = 0
for x in list_of_samples:
    # x is sample size, realizations is the number of repeated monte carlo simulations
    for i in range(realizations):
        y_axis.append(monte_carlo(x))
        x_axis.append(x)
        count = count + 1

colors = ["red", "orange", "green", "blue", "purple", "pink", "black"]
figure, axes = plt.subplots()
scatter_dots10 = plt.scatter(x_axis[0 : 110], y_axis[0:110], color=colors[0])
scatter_dots30 = plt.scatter(x_axis[110 : 220], y_axis[110:220], color=colors[1])
scatter_dots50 = plt.scatter(x_axis[220 : 330], y_axis[220 : 330], color=colors[2])
scatter_dots100 = plt.scatter(x_axis[330 : 440], y_axis[330 : 440], color=colors[3])
scatter_dots250 = plt.scatter(x_axis[440 : 550], y_axis[440 : 550], color=colors[4])
scatter_dots500 = plt.scatter(x_axis[550 : 660], y_axis[550 : 660], color=colors[5])
scatter_dots1000 = plt.scatter(x_axis[660 : 770], y_axis[660 : 770], color=colors[6])
mux = plt.axhline(y=71.4389, color='black', linestyle='-')
mux2 = plt.axhline(y=71.4389 + 10, color='black', linestyle='-')
mux3 = plt.axhline(y=71.4389 - 10, color='black', linestyle='-')
axes.legend([scatter_dots10, scatter_dots30, scatter_dots50, scatter_dots100, scatter_dots250, scatter_dots500, scatter_dots1000, mux], ['red: n = 10',
                                                                                                                                    'orange: n = 30',
                                                                                                                                    'green: n = 50',
                                                                                                                                    'blue: n = 100',
                                                                                                                                    'purple: n = 250',
                                                                                                                                    'pink: n = 500',
                                                                                                                                    'black: n = 1000',
                                                                                                                                         "u_x=71.4389"])



axes.add_artist( scatter_dots10 )
axes.add_artist( scatter_dots30 )
axes.add_artist( scatter_dots50 )
axes.add_artist( scatter_dots100 )
axes.add_artist( scatter_dots250 )
axes.add_artist( scatter_dots500 )
axes.add_artist( scatter_dots1000 )
axes.add_artist( mux2 )
axes.add_artist( mux3 )


# naming the x axis
plt.xlabel('Number of Samples')
# naming the y axis
plt.ylabel('Sample Estimation of X (inches)')


# giving a title to my graph
plt.title('Monte Carlo Sample Estimations across Various Sample Sizes')

# function to show the plot
# plt.show()

for x in list_of_samples:
    # x is sample size, realizations is the number of repeated monte carlo simulations
    val = repeated_monte_carlo(realizations, x)
    round_val = round(val, 3)
    # print("\[est. \hspace[2pt] mean (n={}): {}\]".format(x, round_val))

# calculate 7.
succ = 0
total = 0

for i in range(10000):
    val = monte_carlo(140)
    abs_val = val - 71.4389
    print(abs_val)
    if abs(abs_val) < 10:
        succ = succ + 1
    total = total + 1
print(succ)
print(total)
print("estimation: {}".format(succ/total))
