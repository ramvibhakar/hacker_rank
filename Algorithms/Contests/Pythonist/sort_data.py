__author__ = 'ramvibhakar'
#https://www.hackerrank.com/contests/pythonist/challenges/python-sort-sort

N,M = [int(num) for num in raw_input().split()]
arr = []
for i in xrange(0,N):
    arr.append([int(num) for num in raw_input().split()])
K = input()
sort_arr = sorted(arr, key=lambda entry: entry[K])
for i in xrange(0,N):
        print(" ".join(str(x) for x in sort_arr[i]))