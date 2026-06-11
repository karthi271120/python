cart = [ {"name": "Laptop", "price": 50000},
                    {"name": "Mouse", "price": 500}, 
                    {"name": "Keyboard", "price": 1500} 
                    ] 

total =0

for i in cart:
    total += i['price']
print(total)    