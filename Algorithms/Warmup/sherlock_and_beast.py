__author__ = 'ramvibhakar'
def isDecent(five_count, three_count):
    is_available = five_count !=0 or three_count != 0
    if is_available and five_count % 3 == 0 and three_count % 5 == 0:
        return True
    return False
T = input()
while T > 0:
    n = input()
    found = False
    str = ""
    for i in xrange(0,n):
        str += "5"
    five_count = n
    three_count = 0
    str_list = list(str)
    if isDecent(five_count,three_count):
        found = True
        print("".join(str_list))
    else:
        for i in xrange(n-1,-1,-1):
            str_list[i]="3"
            three_count += 1
            five_count -= 1
            if isDecent(five_count,three_count):
                found = True
                print("".join(str_list))
                break
    if not found:
        print("-1")
    T -= 1