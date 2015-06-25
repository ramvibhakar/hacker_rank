__author__ = 'ramvibhakar'
#https://www.hackerrank.com/contests/pythonist/challenges/regex-2-validate-a-roman-number
import re
#pat = re.compile(r'^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$')
pat = re.compile(r'^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
if(pat.match(raw_input())!= None):
    print('True')
else:
    print('False')
