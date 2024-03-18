t = int(input())
for i in range(0,t):
    n = int(input())
    A = list(map(int,input().split()))
    n = int(input())
    B = list(map(int,input().split()))
    found = True
    for i in A:
        if i not in B:
            found = False
    print(found)
