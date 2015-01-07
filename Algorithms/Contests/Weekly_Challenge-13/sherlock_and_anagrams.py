__author__ = 'ramvibhakar'
import collections
import math
T = input()
while T > 0:
    string = raw_input()
    count = collections.Counter(string)
    pairs = [int(num/2) for num in count.values()]
    total = sum(pairs)
    if total == 0:
        print(0)
    else:
        number = 0
        for i in xrange(0, total+1):
            number += math.factorial(i)
        print(number)
    T -= 1