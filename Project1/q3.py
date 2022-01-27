# bruh....

# returns an 8 digit number corresponding to the zero position and the number permutation
def configureNum(zeroPos, numPerm):
    # t list with 8 slots
    t_list = ['', '', '', '', '', '', '', '']
    i_list = [0, 1, 2, 3, 4, 5, 6, 7]
    # add the zero positions
    for v in zeroPos:
        t_list[int(v)] = '0'
        i_list.remove(int(v))

    counter = 0
    for index in i_list:
        t_list[index] = numPerm[counter]
        counter = counter + 1
    t_str = ""
    for ele in t_list:
        t_str += ele
    return t_str

nums = [1, 2, 3, 4, 5, 6, 7]

perms = []
for a in nums:
    for b in nums:
        if a != b:
            for c in nums:
                if c != a and c != b:
                    for d in nums:
                        if d != a and d != b and d != c:
                            for e in nums:
                                if e != a and e != b and e != c and e != d:
                                    # print([a, b, c, d, e])
                                    perms.append([a, b, c, d, e])

zeroperms = []
positions = [0, 1, 2, 3, 4, 5, 6, 7]
for a in positions:
    for b in positions:
        if a != b:
            for c in positions:
                if c != a and c != b:
                    t_list = [a, b, c]
                    t_list.sort()
                    zeroperms.append(t_list)

zeroperms.sort()
fin_zero_perms = []
for x in zeroperms:
    if x not in fin_zero_perms:
        fin_zero_perms.append(x)
count = 0
# for each zero pattern, there is a configuration of permutations for the other number positions
for zeropattern in fin_zero_perms:
    for numpattern in perms:
        count = count + 1
        zpstr = ""
        npstr = ""
        for z in zeropattern:
            zpstr += str(z)
        for n in numpattern:
            npstr += str(n)
        final_perm = configureNum(zpstr, npstr)
        if count < 101:
            print("\item (num: " + str(count) + ") " + final_perm)


print("Final Count: " + str(count))
