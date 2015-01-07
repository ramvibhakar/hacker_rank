__author__ = 'ramvibhakar'
T = input()
while T > 0:
    a_count,b_count = [int(num) for num in raw_input().split()]
    a_cost, b_cost, ab_cost = [int(num) for num in raw_input().split()]
    costs = []
    costs.append(a_cost*a_count+b_cost*b_count)
    costs.append(a_cost*a_count+(a_cost+ab_cost)*b_count)
    costs.append((b_cost+ab_cost)*a_count+b_cost*b_count)
    costs.sort()
    print(costs[0])
    T -= 1