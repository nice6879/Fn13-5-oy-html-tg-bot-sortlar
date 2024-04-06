def f(x):
    num1 = set()
    num2 = []
    for num in x:
        if num not in num1:
            num1.add(num)
            num2.append(num)
    num2.sort()  
    while len(num2) < len(x):  
        num2.append("_")
    return num2


x = [4, 1, 5, 1, 8, 5, 4,8,7,6]
print(f(x))