# from itertools import combinations

# def find_missing_number(number):
#     digits = [int(digit) for digit in str(number)]
#     for a in digits:
#         for b in digits:
#             if a * b == sum(digits) - a - b:
#                 return a, b
#     return None

# # Test
# number = 324
# result = find_missing_number(number)
# if result:
#     print(f"Teng a va b topildi: {result}")
# else:
#     print("Teng a va b topilmadi")




# def find_factors(number):
#     for i in range(10, 100):
#         for j in range(10, 100):
#             if i * j == number:
#                 return i, j
#     return None

# def find_factors_of_product(number):
#     digits = [int(digit) for digit in str(number)]
#     if len(digits) != 3:
#         return None
#     return find_factors(number)

# # Test
# number = 210
# result = find_factors_of_product(number)
# if result:
#     print(f"{number} ning b va c sonlari: {result}")
# else:
#     print(f"{number} ning b va c sonlari topilmadi")



def find_factors_of_product(number):
    digits = [int(digit) for digit in str(number)]
    if len(digits) != 3:
        return None
    factors = []
    for i in range(1, 100):
        for j in range(1, 100):
            if i * j == number:
                factors.append((i, j))
    return factors

# Test
number = 171

result = find_factors_of_product(number)
if result:
    print(f"{number} ning b va c sonlari: {result}")
else:
    print(f"{number} ning b va c sonlari topilmadi")




