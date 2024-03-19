temp = []
def fun(s):
    valid = True
    if ('@' not in s) or ('.' not in s):
        valid = False
        return
    if  len(s[s.index('.')+1:])>3 or not (s[s.index('.')+1:].isalpha()):
        valid = False
    if not s[s.index('.')+1:].isalpha():
        valid = False
    if not s[s.index('@')+1:s.index('.')].isalnum():
        valid = False
    username = s[:s.index('@')]
    if len(username)==0:
        valid = False
    for ch in username:
        if (not ch.isalnum()) and ( ch != '-') and (ch != '_'):
            valid = False
    if valid:
        return s


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
