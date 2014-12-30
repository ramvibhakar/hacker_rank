__author__ = 'ramvibhakar'
sn,sm = raw_input().split()
N = int(sn)
M = int(sm)
total = 0
for i in xrange(0,M):
    a,b,k = [int(num) for num in raw_input().split()]
    total += ((b-a)+1)*k
print(total/N)