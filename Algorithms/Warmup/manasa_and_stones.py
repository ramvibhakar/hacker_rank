__author__ = 'ramvibhakar'
T = input()
while T > 0:
    n = input()
    a = input()
    b = input()
    max_ab = max(a,b)
    min_ab = min(a,b)
    output = ""
    if min_ab != max_ab:
        for i in xrange(1,n+1):
            output += str((n-i)*min_ab+(i-1)*max_ab) + " "
    else:
        output = str((n-1)*min_ab)
    print(output)
    T -= 1