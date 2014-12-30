__author__ = 'ramvibhakar'
sn,sm = raw_input().split()
N = int(sn)
M = int(sm)
topics= []
for i in range(0,N):
    topics.append(int(raw_input(),2))
maxtopics = 0
count_max = 0
for i in range(0,N):
    for j in range(i+1,N):
        topics_known = bin(topics[i] | topics[j]).count('1')
        if topics_known >= maxtopics:
            if topics_known == maxtopics:
                count_max += 1
            else:
                maxtopics = topics_known
                count_max = 1
print(maxtopics)
print(count_max)