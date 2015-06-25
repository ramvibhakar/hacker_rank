from datetime import datetime
#Runs on python 3 only

N = int(input())
for i in range(0,N):
    d1 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    d2 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    print(int(abs((d1-d2).total_seconds())))