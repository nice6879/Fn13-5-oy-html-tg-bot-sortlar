def x(y):
    toq = [x for x in y if x % 2 != 0]
    juft = [x for x in y if x % 2 == 0]
    
    toq.sort()
    
    result = []
    toq_index = 0
    juft_index = 0
    for num in y:
        if num % 2 != 0:
            result.append(toq[toq_index])
            toq_index += 1
        else:
            result.append(juft[juft_index])
            juft_index += 1
    return result

print(x([7, 1]))  
print(x([5, 8, 6, 3, 4]))  
print(x([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))  