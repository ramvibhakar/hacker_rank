__author__ = 'ramvibhakar'
def maxXor(_l,_r):
    q = _l ^ _r
    a = 1
    while q > 0:
        q /= 2
        a <<= 1
    return a-1
_l = int(raw_input())
_r = int(raw_input())
res = maxXor(_l, _r)
print(res)