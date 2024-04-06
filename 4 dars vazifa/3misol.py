def yagona_raqam(num2):
    raqam = 0
    for num1 in num2:
        raqam ^= num1
    return raqam


num2 = [2, 2, 1, 4, 5, 4, 5, 8, 7, 7, 8]
result = yagona_raqam(num2)
print(result)