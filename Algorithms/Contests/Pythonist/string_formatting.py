__author__ = 'ramvibhakar'
#https://www.hackerrank.com/contests/pythonist/challenges/python-string-formatting

N = int(input())
space = len(bin(N)[2:]) + 1
for i in xrange(1, N+1):
    d = str(i)
    o = str(oct(i)[1:])
    h = str(hex(i)[2:]).upper()
    b = str(bin(i)[2:])
    print(' '*(space-len(d)-1)+d+' '*(space-len(o))+o+' '*(space-len(h))+h+' '*(space-len(b))+b)