__author__ = 'ramvibhakar'
T = input()
for i in xrange(0,T):
    n,c,m = [int(num) for num in raw_input().split()]
    total_chocolates = n/c
    wrappers = n/c
    while wrappers >= m:
        chocolates = wrappers/m
        total_chocolates += chocolates
        wrappers = chocolates + wrappers%m
    print(total_chocolates)