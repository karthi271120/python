products =[
           {'id':1,'name':'laptop'},
           {'id':2,'name':'mobile'},
           {'id':3,'name':'keyborad'}
           ]
name = input('enter the name:')
found =False
for a in products:
    if a ['name'] == name:
        print('products found')
        print('id',a['id'])
        print('name',a['name'])
        found = True
        break
if found == False:
    print('procut not found')    
    

