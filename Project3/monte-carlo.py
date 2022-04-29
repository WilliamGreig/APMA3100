import math

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

for i in range(20):
    print("u_{}: {}".format(i, rng()))
