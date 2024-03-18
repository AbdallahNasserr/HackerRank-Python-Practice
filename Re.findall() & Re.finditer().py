# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
found =0
vowel = 'aeiouAEIOU'
counter = 0
temp =''
flag1=0
flag2=0
for i in range(0,len(s)):
    if s[i] not in vowel:
       if not flag1:
            flag1 = 1
       elif flag1:
           if len(temp)>1:
                found = 1
                print(temp)
           flag1 =1
           flag2=0
           counter =0
           temp =''
    else:
        if flag1:
            temp = temp + s[i]
if not found:
    print(-1)
