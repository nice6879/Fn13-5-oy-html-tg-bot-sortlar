def sonni_topish(num1):
    n = len(num1) + 1
    num2 = n * (n + 1) // 2
    num3 = sum(num1)
    return num2 - num3


num1 = [8,7,6,5,4,3,2,9]
x = sonni_topish(num1)
print(f"etishmayotgan son: {x}")