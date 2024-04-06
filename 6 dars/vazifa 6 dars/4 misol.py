def x(s,t):
    z=''
    if len(s) > len(t):
        z+=s[len(t):]
    elif len(s) < len(t):
        z+=t[len(s):]
    return z
print(x(s = 'abcde' , t = 'abcd'))