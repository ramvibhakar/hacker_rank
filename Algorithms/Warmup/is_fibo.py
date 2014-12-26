__author__ = 'ramvibhakar'
def is_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True

def isFib(N):
    if is_square((5*N*N)+4) or is_square((5*N*N)-4):
        return True
    return False
T = input()
while T > 0:
    N = input()
    if isFib(N):
        print("IsFibo")
    else:
        print("IsNotFibo")
    T -= 1