__author__ = 'ramvibhakar'

import re
N = int(input())
arr = []
pat = re.compile(r'[a-zA-Z0-9_-]+\@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$')
for i in xrange(0,N):
    arr.append(raw_input())
new_arr = list(filter(lambda x: pat.match(x)!= None, arr))
print(sorted(new_arr,key=lambda x:x.split('@')[0].lower()))