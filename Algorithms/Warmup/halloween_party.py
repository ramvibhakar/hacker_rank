__author__ = 'ramvibhakar'
import math
T = input()
while T > 0:
    sum = input()
    a = math.ceil(sum/2)
    b = sum - a
    chocolates = int(a*b)
    print(chocolates)
    T -= 1
