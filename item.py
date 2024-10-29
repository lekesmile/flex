class item:
    
    all = []
    
    def __init__(self, name:str, price:float, quantity= 0):

        #Validation
        assert price >= 0, f"price {price} shoulbe be greater than 0"

        #Object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #Add all item into an array
        item.all.append(self)

     
    def calculate_total_price(self):
        return self.price * self.quantity
    

item1 = item("Phome", 100, 10)
print(item1.name)
print(item1.calculate_total_price())

item2 = item("Laptop", 500, 5)
print(item2.calculate_total_price())


item3 = item("Cable", 10, 5)
item4 = item("Mouse", 50, 5)
item5 = item("Keyboard", 75, 5)

print(item.all)

for x in item.all:
    print(x.name)