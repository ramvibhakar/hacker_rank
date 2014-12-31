__author__ = 'ramvibhakar'
import math
T = input()
for i in xrange(0,T):
    a,b = [int(num) for num in raw_input().split()]
    count = 0
    print(int(math.sqrt(b))-int(math.sqrt(a-1)))