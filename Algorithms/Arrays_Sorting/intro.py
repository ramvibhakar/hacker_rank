__author__ = 'ramvibhakar'
def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x:
            hi = mid
        else:
            return mid
    return -1
V = input()
n = input()
ar = [int(num) for num in raw_input().split()]
print(binary_search(ar,V))

