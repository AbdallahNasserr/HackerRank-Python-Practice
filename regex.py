import regex
import re
import os 
os.chdir(r'C:\Users\acer\downloads')
with open('regex.txt') as file:
    read = file.read()
    for line in read:
        pass
        # print(line)
# print(read)
string = '123456 adsfer 123 654'
match = re.findall(r'[0-9]+',string=read)
match = [int(x) for x in match]
summ =0
for num in match:
    summ+=num
print(summ)
