__author__ = 'ramvibhakar'
T = input()
while T > 0:
    height = 1
    N = input()
    for i in range(0,N):
        if i%2 == 0:
            height *= 2
        else:
            height += 1
    print height
    T -= 1
