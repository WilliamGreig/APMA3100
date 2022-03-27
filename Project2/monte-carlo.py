import math
import numpy as np
import matplotlib.pyplot as plt

x_0 = 1000
a = 24693
c = 3517
K = math.pow(2, 17)

x_list = [x_0]
u_list = []

# return a random number
def rng():
    # get most recent value
    i = len(x_list)
    value = a * x_list[i - 1] + c
    remainder = value % K
    x_list.append(remainder)
    u_list.append(x_list[i] / K)
    return u_list[len(u_list) - 1]

# returns waiting time value of busy signal
def busy_signal():
    # busy_signal + hang up
    return 3 + 1

def customer_unavail():
    # customer_unavail (25s) + hang up
    return 25 + 1

# returns the seconds taken by customer (max) given a probability
def inverse_funct(prob):
    return round(-12 * np.log(1 - prob), 2)

# performs a calling process and returns the waiting time for one given process
def calling_process():
    wait_time = 0
    failures = 0
    while failures < 4:
        # dial customer
        wait_time = wait_time + 6
        # generate probability to detect busy signal, customer available, or customer unavailable -- cap (customer available probability)
        cap = rng()
        if 0 <= cap < 0.2:      #busy signal
            wait_time = wait_time + busy_signal()
        elif 0.2 <= cap < 0.5:  # customer unavailable
            wait_time = wait_time + customer_unavail()
        else:   # customer available
            # generate a new probability -- customer picks up phone < 25 about 0.8755
            ans_prob = rng()
            if ans_prob <= 0.8755: # customer picks up phone in time
                # from the probability, use inverse function to find particular waiting time value!
                wait_time = wait_time + inverse_funct(ans_prob)
                break   # immediately break/end calling process
            else:   # customer takes too long to pick up phone
                wait_time = wait_time + customer_unavail()
        failures = failures + 1
    return wait_time




# call this function to execute n number of calling processes
# returns "W" -- waiting time -- for n number of calling processes
def perform_simulation(n):
    waiting_results = []
    for i in range(n):
        wait_time = calling_process()
        waiting_results.append(wait_time)
    return waiting_results


n = 1000
results = perform_simulation(n)
for i in range(len(results)):
    print("Trial {}: {}".format(i, results[i]))

est_mean = sum(results)/len(results)
results.sort()
est_first_q = results[int(len(results) * 0.25)]
est_third_q = results[int(len(results) * 0.75)]

# returns estimation of prob. CDF of some w (for RV W)
def CDF_W(results, w):
    count = 0
    for ele in results:
        if ele >= w:
            break
        else:
            count = count + 1
    return count / len(results)


# probability of events:
CDF_15 = CDF_W(results, 15)
print("CDF_15: {}".format(CDF_15))

CDF_20 = CDF_W(results, 20)
print("CDF_20: {}".format(CDF_20))

CDF_30 = CDF_W(results, 30)
print("CDF_30: {}".format(CDF_30))

CDF_R_40 = 1 - CDF_W(results, 40)
print("CDF_R_40: {}".format(CDF_R_40))

CDF_R_60 = 1 - CDF_W(results, 60)
print("CDF_R_60: {}".format(CDF_R_60))

CDF_R_80 = 1 - CDF_W(results, 80)
print("CDF_R_80: {}".format(CDF_R_80))

CDF_R_100 = 1 - CDF_W(results, 100)
print("CDF_R_100: {}".format(CDF_R_100))

plt.hist(x=results, bins=30)
plt.show()
