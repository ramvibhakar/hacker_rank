__author__ = 'ramvibhakar'
T = input()
while T > 0:
    text = str(raw_input())
    prevChar = ''
    count = 0
    for i in range(0,len(text)/2):
        count += abs(ord(text[i])-ord(text[len(text)-1-i]))
    T -= 1
    print count
