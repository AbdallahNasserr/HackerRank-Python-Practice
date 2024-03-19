# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
order_dict = {}
n = int(input())
for i in range(0,n):
    s = input()
    indx = s.rfind(' ')
    num = int(s[indx+1:])
    item = s[:indx]
    if item not in order_dict:
        order_dict[item]=num 
    else:
        order_dict[item]=num + order_dict[item]
for i in order_dict:
    print(i,order_dict[i])
