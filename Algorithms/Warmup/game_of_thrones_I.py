__author__ = 'ramvibhakar'
string = raw_input()

found = True
length = len(string)
count = [0]*26
oddCount = 0
for i in range(0,length):
    count[ord(string[i])-ord('a')] +=1
for cnt in count:
    if length%2==1 and oddCount>1:
        found=False
        break
    elif length%2==0 and oddCount>0:
        found=False
        break
    if cnt%2 != 0:
        oddCount +=1
if not found:
    print("NO")
else:
    print("YES")
