def bruteCheck(bin_str): # function to check condition (three 0's and five 1's)
    zeroC = 0
    oneC = 0
    for dig in bin_str:
        if dig in "0":
            zeroC += 1
        else:
            oneC += 1
    if zeroC == 3 and oneC == 5:
        return True
    return False
def convertIntToBin(value): # converts integer value to binary -- max 8 bits
    power = 8
    bin_list = ['0', '0', '0', '0', '0', '0', '0', '0']
    while value > 0:
        if value / pow(2, power) < 1:
            power = power - 1
        else:
            bin_list[len(bin_list) - power - 1] = '1'
            value = value - pow(2, power)
    bin_str = ""
    for dig in bin_list:
        bin_str = bin_str + dig
    return bin_str
valueCounter = 0
cond_counter = 0
while valueCounter < 256:
    bin_num = convertIntToBin(valueCounter)
    if bruteCheck(bin_num):
        cond_counter = cond_counter + 1
        print("\item " + bin_num)
    valueCounter = valueCounter + 1
print(cond_counter)

