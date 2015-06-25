__author__ = 'ramvibhakar'
def get_all_substrings(input_string):
  length = len(input_string)
  return [''.join(sorted(input_string[i:j+1])) for i in xrange(length) for j in xrange(i,length)]


T = input()
while T > 0:
    cnt = 0
    string = raw_input()
    sub_strings = get_all_substrings(string)
    for i in xrange(0,len(sub_strings)):
        count = sub_strings[i:len(sub_strings)].count(sub_strings[i])
        if count >1:
            cnt +=1
    print(cnt)
    T -= 1