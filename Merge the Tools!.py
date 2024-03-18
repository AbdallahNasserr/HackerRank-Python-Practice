def merge_the_tools(string, k):
    temp = []
    for i in range(0,len(string),k):
        temp.append(string[i:i+k])
    for s in temp:
        temp_stringtring=''
        for j in s:
            if j not in temp_stringtring:
                temp_stringtring = temp_stringtring + j 
        print(temp_stringtring)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
