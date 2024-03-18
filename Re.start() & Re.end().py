s = input()
k = input()
found = 0
temp  = ''
l = 0
r = len(k)-1
while r < len(s):
    if s[l:r+1]==k:
        print(f'({l}, {r})')
        found =1
    r = r+1
    l = l+1
if not found:
    print('(-1, -1)')
