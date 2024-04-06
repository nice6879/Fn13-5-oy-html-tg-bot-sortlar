def reverse(n):
    x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    y = [i for i in n if i in x]
    join = ''.join(y[::-1])
    javob = ''
    list = 0
    for i in n:
        if i in x:
            javob += join[list]
            list+=1
        else:
            javob += i
    return javob
print(reverse("he-ll/o, Wo?rl.d"))