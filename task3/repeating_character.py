def repeating(s):
    for i in s:
        count = 0

        for j in s:
            if i == j:
                count += 1

        if count == 1:
            return i
    return None  
print(repeating('aabbcdd'))
