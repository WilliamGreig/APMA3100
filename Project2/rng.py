import math

x_0 = 1000
a = 24693
c = 3517
K = math.pow(2, 17)

x_list = [x_0]
u_list = []

for i in range(100):
    if i == 0:
        pass
    else:
        value = a * x_list[i - 1] + c
        remainder = value % K
        x_list.append(remainder)
        u_list.append(x_list[i] / K)


for ui in range(len(u_list)):
    print("u_{}: {}".format(ui, round(u_list[ui], 4)))

# results for report
"""
u_51: 0.4273
u_52: 0.7682
u_53: 0.0933
"""
