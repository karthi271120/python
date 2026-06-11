num = [10,20,30,20,40,10,50,30]
unique =[]
for i in num:
    if i not in unique:
        unique.append(i)
print('unique value:',unique)        
print(len(unique))