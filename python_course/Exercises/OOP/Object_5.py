# Product class
class Product:
    def __init__(self, name, production_cost, sale_price):
        self.name = name
        self.production_cost = production_cost
        self.sale_price = sale_price
    
    # method to calculate profit
    def calculate_profit(self):
        profit = self.sale_price - self.production_cost
        return profit
    
class Clothing:
    
    def __init__(self, name, production_cost, sale_price, material):
        self.product = Product(name, production_cost, sale_price)
        self.name = self.product.name
        self.production_cost = self.product.production_cost
        self.sale_price = self.product.sale_price
        self.material = material
    # uses Product class method
    def calculate_profit(self):
        return self.product.calculate_profit()
    
class GuaranteedClothing:
    
    def __init__(self, name, production_cost, sale_price, warranty):
        self.product = Product(name, production_cost, sale_price)
        self.name = self.product.name
        self.production_cost = self.product.production_cost
        self.sale_price = self.product.sale_price
        self.warranty = warranty
    # uses Product class method
    def calculate_profit(self):
        return self.product.calculate_profit()
   
class Factory:
    
    def __init__(self, inventory, prod):
        self.inventory = inventory
        self.prod = prod
        
    def add_product(self, prod, quantity):
        self.inventory[prod.name] = quantity

    def sell_product(self, prod, quant):
        if prod.name in self.inventory and self.inventory[prod.name] >= quant:
            old_quant = self.inventory[prod.name]
            self.inventory[prod.name] -= quant
            gain = old_quant - self.inventory[prod.name]
            return self.prod.calculate_profit() * gain
        else:
            print("Quantity or product type not available")
    
    def return_product(self, prod, quant):
        if prod.name in self.inventory:
            self.inventory[prod.name] += quant
        else:
            print("Product not found in inventory")