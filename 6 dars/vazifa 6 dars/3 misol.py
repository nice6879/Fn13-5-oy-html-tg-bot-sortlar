def x(n):
    year, month, day = map(int, n.split('-'))
    y = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        y[2] = 29

    q = sum(y[:month]) + day

    return q

z = "2019-03-29"
result = x(z)
print(result)
