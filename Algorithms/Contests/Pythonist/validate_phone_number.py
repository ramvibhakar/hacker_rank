__author__ = 'ramvibhakar'
#https://www.hackerrank.com/contests/pythonist/challenges/regex-1-validating-the-phone-number

import re
N = int(input())
pat = re.compile('[7|8|9]\d{9}$')
for i in xrange(0,N):
    if(pat.match(str(raw_input())) != None):
        print('YES')
    else:
        print('NO')