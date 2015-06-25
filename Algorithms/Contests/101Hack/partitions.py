__author__ = 'ramvibhakar'

str = raw_input()
unique_chars =list(set(str))
unique_chars = [ x for x in unique_chars if x != str[0]]
cnt = 1
for ch in unique_chars:
    cnt += (str.count(ch)-1)
print cnt%1000