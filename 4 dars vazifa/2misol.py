def farqini_topish(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    farqi = (set1 | set2) - (set1 & set2)
    return ''.join(sorted(farqi))

print(farqini_topish("abcdeoiy", "abcd"))  