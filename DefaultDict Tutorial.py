from collections import defaultdict
listt = list(map(int,input().split()))
n1 = listt[0]
n2 = listt[1]
defdic = defaultdict(list)
for i in range(0,n1):
    ch = input()
    defdic[ch].append(i+1)
for i in range(0,n2):
    ch = input()
    if len(defdic[ch]) == 0:
        print(-1)
    else:
        for j in range(0,len(defdic[ch])-1):
            print(defdic[ch][j],end = ' ')
        print(defdic[ch][-1])
        
