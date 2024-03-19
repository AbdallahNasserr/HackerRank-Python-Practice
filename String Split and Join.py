def split_and_join(line):
    # write your code here
    temp = []
    for i in line:
        if i == ' ':
            temp.append('-')
        else:
            temp.append(i)      
        new = ''
    for i in temp:
        new += i
    return new

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
