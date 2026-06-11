user =[ {"username": "admin", "password": "1234"},
  {"username": "john", "password": "abcd"} ]

username =input('enter username:')
password =input('inter password:')

found = False
for users in user:
    if users ['username']==username:
        found = True
    if users ['password'] == password:
        print('login succesfuly')
    else:
        print('invalid')  
    break    

if found == False:
    print('invalid username')          