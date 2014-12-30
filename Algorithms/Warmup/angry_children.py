__author__ = 'ramvibhakar'
n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()
min_diff = candies[k-1]-candies[0]
for i in range(1,n-k):
    diff = candies[i+k-1]-candies[i]
    if diff < min_diff:
        min_diff = diff
print min_diff
