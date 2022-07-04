import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from math import *
def phi(x):
    #'Cumulative distribution function for the standard normal distribution'
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

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

sample_sizes = [3, 9, 27, 81]
results = []
for samp_size in sample_sizes:
    sub_result = []
    for i in range(550):
        sub_result.append(monte_carlo(samp_size))
    results.append(sub_result)

# calculate stage
list_mus = []
list_variance = []
# calculate mu
for outcome in results:
    # outcome is list of values
    cur_sum = 0
    for ele in outcome:
       cur_sum = cur_sum + ele
    list_mus.append(cur_sum/len(outcome))

# calculate variance
index = 0
for outcome in results:
    cur_sum = 0
    for ele in outcome:
        cur_sum = math.pow(ele, 2) - math.pow(list_mus[index], 2)
    list_variance.append(cur_sum/len(outcome))
    index = index + 1

for i in range(len(list_mus)):
    print("---- n = {} ----".format(sample_sizes[i]))
    print("mu: {}".format(list_mus[i]))
    print("sqrt(var): {}".format(math.sqrt(list_variance[i])))

# Transform stage
index = 0
for outcome in results:
    t_index = 0
    for element in outcome:
        results[index][t_index] = (results[index][t_index] - list_mus[index]) / math.sqrt(list_variance[index])
        t_index = t_index + 1
    index = index + 1

for eq in results:
    print(eq)

z = [-1.4 , -1, -0.5, 0, 0.5, 1, 1.4]
phi_z = [1 - 0.9192, 1 - 0.8413, 1 - 0.6195, 0.5, 0.6195, 0.8413, 0.9192 ]
z_value_results = []
index = 0
for outcome in results:
    print("n={}".format(sample_sizes[index]))
    temp_z = []
    for z_j in z:
        count = 0
        for element in outcome:
            if element <= z_j:
                count = count + 1
        print("\[z = {}: {}\]".format(z_j, round(count/len(outcome), 3)))
        temp_z.append(count/len(outcome))
    z_value_results.append(temp_z)
    index = index + 1


print("j / n table")
count = 0
for ls in z_value_results:
    max = 0
    index = 0
    z_jIndex = 0
    print("---------- n: {}--------".format(sample_sizes[count]))
    for z_vals in ls:
        print("j {}: {}".format(index, abs(z_vals - phi_z[index])))
        if abs(z_vals - phi_z[index]) > max:
            max = abs(z_vals - phi_z[index])
            z_jIndex = index
        index = index + 1
    # print("z_jIndex value: {}".format(ls[z_jIndex]))
    print("max value {}".format(max))
    count = count + 1

Phi_Xvals = []
Phi_Yvals = []

curr_x = -2.5
increment = 0.01
while curr_x < 2.5:
    Phi_Xvals.append(curr_x)
    Phi_Yvals.append(phi(curr_x))
    curr_x = curr_x + increment

figure, axes = plt.subplots()
part1 = False
if part1:
    plt.plot(z, z_value_results[0], "-o", color="blue", label="blue: n=3")
    plt.axvspan(0.48545454545454547, 0.4046545454545455, color='blue', alpha=0.3, label="MAD3 interval")
    plt.plot(z, z_value_results[1],"-o", color="red", label="red: n=9")
    plt.axvspan(0.5727272727272728, 0.34647272727272727, color='red', alpha=0.3, label="MAD9 interval")
    plt.plot(z, z_value_results[2],"-o", color="green", label="green: n=27")
    plt.axvspan(0.4381818181818182, 0.3573818181818182, color='green', alpha=0.3, label="MAD27 interval")
    plt.plot(z, z_value_results[3],"-o", color="black", label="black: n=81")
    plt.axvspan(0.42727272727272725, 0.34647272727272727, color='black', alpha=0.3, label="MAD81 interval")
    plt.plot(Phi_Xvals, Phi_Yvals, color="black", label="Normal CDF Phi(z)")

    plt.title('Empericial CDF of Estimated Means, Normal CDF, and Probability Interval of MAD(n)')
    plt.xlabel('Standardized Z-Values')
    plt.ylabel('Probability')

    plt.legend()
    plt.xlim([-2.5, 2.5])
    plt.show()
else:
    print("HLLO")
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(z, z_value_results[0], '-o', color="blue", label="blue: n=3")
    axs[0, 0].plot(Phi_Xvals, Phi_Yvals, color="black", label="Normal CDF Phi(z)")
    axs[0, 0].set_title('Normal CDF vs. Estimated Samples (n=3)')

    axs[0, 1].plot(z, z_value_results[1], '-o', color="red", label="red: n=9")
    axs[0, 1].plot(Phi_Xvals, Phi_Yvals, color="black", label="Normal CDF Phi(z)")
    axs[0, 1].set_title('Normal CDF vs. Estimated Samples (n=9)')

    axs[1, 0].plot(z, z_value_results[2], '-o', color="green", label="green: n=27")
    axs[1, 0].plot(Phi_Xvals, Phi_Yvals, color="black", label="Normal CDF Phi(z)")
    axs[1, 0].set_title('Normal CDF vs. Estimated Samples (n=9)')

    axs[1, 1].plot(z, z_value_results[3], '-o', color="black", label="black: n=81")
    axs[1, 1].plot(Phi_Xvals, Phi_Yvals, color="black", label="Normal CDF Phi(z)")
    axs[1, 1].set_title('Normal CDF vs. Estimated Samples (n=9)')
    plt.show()
    for ax in axs.flat:
        ax.set(xlabel='x-label', ylabel='y-label')

    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()

