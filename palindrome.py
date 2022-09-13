# valid palindrome (Stirng)
def fun():
    s = "0P"
    s = s.replace(' ', '')
    if s == '':
        return True
    s = s.lower()
    new = ''
    for i in range(0, len(s)):
        if (ord(s[i]) >= 97 and ord(s[i]) <= 122) or (ord(s[i]) >= 48 and ord(s[i]) <= 57):
            new = new+s[i]

    print(new)
    mid = len(new)//2
    a = new[0:mid]
    print(a)
    if len(new) % 2 == 0:
        b = new[len(new):mid-1:-1]
        print(b)
    else:
        b = new[len(new):mid:-1]
        print(b)
    if a == b:
        return True
    else:
        return False


n = fun()
print(n)
