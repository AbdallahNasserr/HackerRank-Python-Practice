# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = []
for i in range(0,n):
    string = input()
    arr.append(string)
dictt = {}
for i in arr:
    if i not in dictt:
        dictt[i] = 1
    else:
        dictt[i] = dictt[i] +1
for i,j in dictt.items():
    print(i,j)
