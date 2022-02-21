class Product:
    
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = abs(price)
        self.quantity = abs(quantity)
        
    def value(self):
        value =  (self.price) * (self.quantity)
        print("The current value of ", self.name, "inventory is: $", value)
    
    def add_inv(self,add):
        
        if add < 0:
            print("Please enter valid restock amount!")
            
        else:
            self.quantity = (self.quantity) + (add)
            print(add, self.name, "have been added to stock. Current inventory is: ", self.quantity)
    
    def sub_inv(self,sub):
        
        if sub > self.quantity:
            print("Not enogh inventory!")
        
        else:
            self.quantity = (self.quantity) - (sub)
            print(sub, self.name, "have been removed from stock. Current inventory is: ", self.quantity)
        

nike_tops = Product("Nike Shirts",20,50)

nike_tops.value()