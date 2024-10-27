class item:
   
    
    def __init__(self, name:str, price:float, quantity= 0):

        #Validation
        assert price >= 0, f"price {price} shoulbe be greater than 0"
        
        #Object
        self.name = name
        self.price = price
        self.quantity = quantity

      
    def calculate_total_price(self):
        return self.price * self.quantity

item1 = item("Phome", 100, 10)
print(item1.name)
print(item1.calculate_total_price())

item2 = item("Laptop", 500, 5)
print(item2.calculate_total_price())

