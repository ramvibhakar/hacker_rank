__author__ = 'ramvibhakar'
T = input()
while T > 0:
    N = input()
    count = 0
    sN = str(N)
    length = len(sN)
    while length > 0:
        digit = int(sN[length-1])
        if digit != 0:
            if N%int(sN[length-1]) == 0:
                count += 1
        length -= 1
    T -= 1
    print count
