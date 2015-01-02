__author__ = 'ramvibhakar'
from fractions import gcd
T = input()
while T > 0:
    n = input()
    array = [int(num) for num in raw_input().split()]
    g_divisor = 0
    for num in array:
        g_divisor = gcd(g_divisor,num)
        if g_divisor == 1:
            print("YES")
            break
    if g_divisor != 1:
        print("NO")
    T -= 1
