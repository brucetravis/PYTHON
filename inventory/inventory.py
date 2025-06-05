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
