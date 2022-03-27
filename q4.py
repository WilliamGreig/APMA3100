# part (b.)
from itertools import permutations

def createCountingPerms():
    p_list = []
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                p_list.append([a, b, c])
    uniq = []
    for ele in p_list:
        if sum(ele) == 5:
            uniq.append(ele)

    for x in uniq:
        print("\item[] $(" + str(x) + "$)")

    return uniq

def factorial(num):
    prod = 1
    while num > 1:
        prod = prod * num
        num = num - 1
    return prod

def computePermutations(num_list):
    aCount = num_list[0]
    bCount = num_list[1]
    cCount = num_list[2]
    if max(num_list) == 3:
        # formula 1
        count = factorial(5) / factorial(3)
    else:
        # formula 2
        count = factorial(5) / (2 * 2)
    aStr = "A" * aCount
    bStr = "B" * bCount
    cStr = "C" * cCount
    total_str = aStr + bStr + cStr
    print("total string: {}".format(total_str))
    p = permutations(total_str)
    unique_entries = []
    for j in list(p):
        if j not in unique_entries:
            unique_entries.append(j)
    count = len(unique_entries)
    print("Count: {}".format(count))
    return count

u = createCountingPerms()
perm_count = 0
for ele in u:
    perm_count = perm_count + computePermutations(ele)

print(perm_count)
