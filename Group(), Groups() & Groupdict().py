# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
found = -1
for i in range(0,len(s)-1):
    if i == len(s)-1:
        pass
    else:
        if (s[i] == s[i+1] and s[i].isalnum()):
            found = s[i]
            break
print(found)
