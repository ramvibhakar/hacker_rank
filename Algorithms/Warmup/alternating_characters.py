__author__ = 'ramvibhakar'
T = input()
while T > 0:
    text = str(raw_input())
    prevChar = ''
    count = 0
    for i in range(0,len(text)):
        if prevChar == text[i]:
            count += 1
        prevChar = text[i]
    T -= 1
    print count
