# # 3. Scenario Task: Inventory Management for a Retail Store

# Imagine you are tasked with developing an inventory management system for a retail store. 
# The system should keep track of the products available in the store, their quantities, and prices. 
# You need to design a Python program using classes and objects to manage this inventory.

# Question:

# You are the software developer responsible for building an inventory management system for a 
# retail store. Your task is to design a Python program that will help the store keep track of its 
# products, quantities, and prices, allowing employees to add, update, sell, and restock items 
# efficiently.

# Here are the specific requirements for your program:

# Create a class Product with the following attributes:

# product_id (an identifier for the product).
# name (the name of the product).
# price (the price of the product).
# quantity (the quantity of the product in stock).

# Create a class Inventory to manage the store's inventory. 
# This class should have the following methods:

# add_product(product): a method that takes a Product object and adds it to the inventory.
# update_product(product_id, new_price, new_quantity): a method that updates the price and 
# quantity of a product by its product_id.

# sell_product(product_id, quantity_sold): a method that sells a specified quantity of a product, 
# reducing the product's quantity in stock.

# restock_product(product_id, quantity_restocked): a method that restocks a product with a specified 
# quantity, increasing its quantity in stock.

# calculate_revenue(): a method that calculates and returns the total revenue generated 
# from the products sold.

# display_inventory(): a method that displays the current state of the inventory, 
# showing product details (name, price, quantity).

# Now, create an instance of the Inventory class and demonstrate how it can be used to manage the 
# store's inventory efficiently. You should be able to add products, update their information, 
# sell products, restock items, and calculate the total revenue.

# Ensure your solution showcases proper class design, object instantiation, and method usage, 
# while also addressing the real-life scenario of retail inventory management





class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def update_product(self, product_id, new_price, new_quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.price = new_price
                product.quantity = new_quantity
                print(f'Product {product_id}, successfully updated')
                return
            print(f'product not found.')

    def sell_product(self, product_id, quantity_sold):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity -= quantity_sold
                print(f'You sold {product.quantity} units of {product_id}')
                return
            print(f'{product_id} is not in stock')

    def restock_product(self, product_id, quantity_restocked):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity += quantity_restocked
                print(f'{quantity_restocked} units of {product_id} restocked')
                return
            print(f'{product_id} not found.')

    def calculate_revenue(self, product_id, quantity_sold, initial_price, final_price):
        for product in self.products:
            if product.product_id == product_id:
                if product.quantity >= quantity_sold:
                    items = sum(product.price * (initial_price - final_price))
                    print(items)


    # def display_inventory(self):
    #     inventory_info = "\n".join([f"PRODUCT_ID: {product['product_id']}, NAME: {product['name']}, PRICE: {product['price']}, QUANTITY: {product['quantity']}" for product in self.products])
    #     return inventory_info



    # def display_inventory(self):
    #     inventory_info = "\n".join(f"Product_id: {product['product_id']} Product_Name: {product['name']} Product_price: {product['price']} Product_Quantity: {product['quantity']}" for product in self.products)
    #     return inventory_info


Beverages = Product('012345', 'Cocoa', 'sh314', 200)
Wheat = Product('034521', "Bread", "sh100", 100)
Detergents = Product('4536748', "Toss", "sh350", 50)
Cereal = Product('032456', "Cornflakes", "sh420", 50)
Meat = Product('536421', 'Stake', '480', 20)



My_Inventory = Inventory()
My_Inventory.add_product(Beverages)
My_Inventory.add_product(Cereal)
My_Inventory.add_product(Wheat)


My_Inventory.update_product('012345', 'sh100', "100 tins")
My_Inventory.update_product("032456", "sh380", "100 boxes")
My_Inventory.update_product("034521", "sh80", "150 loaves of Bread")

# My_Inventory.display_inventory()































# Can puth hem in a dictionary?? For example in the beverage saection, can I just put all the beverages in
# a Dictionary.