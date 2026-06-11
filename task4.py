sentence = "python is easy and python is powerful"
word =sentence.split()

for i in range(len(word)):
    kkkk = False 

    for k in range(i):  
      if word[i] == word[k]:
        kkkk = True
        break               
    if kkkk:
     continue 
    count = 0

    for j in range(len(word)):
      if  word[i] == word[j]:
       count += 1

    print(word[i],count)      
 
 
 
 
 
 
 
  