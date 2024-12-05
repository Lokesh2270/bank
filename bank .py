class InventoryItem:
    def __init__(self, name, quantity, price_per_unit):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        
    def update_quantity(self, amount):
         self.quantity = amount

    def update_price_per_unit(self):
        self.price_per_unit  

    def calculate_total_value(self):
         return self.quantity * self.price_per_unit

    def __str__(self):
        return f"Item: {self.name}, Quantity: {self.quantity}, Price/Unit: ${self.price_per_unit:.2f}, Total Value: ${self.calculate_total_value():.2f}"
   
item1 = InventoryItem(name="Television", quantity=10, price_per_unit=56000)
print(item1)
item2 = InventoryItem(name="iron", quantity=33, price_per_unit=560.00)
print(item2)
item1.update_quantity(2)
print(item1)
item2.update_quantity(1)
print(item2)
total_value = item1.calculate_total_value()
print(f"The total value of {item1.name} inventory is: ${total_value:.2f}")

def add_item(self, item):
    self.items[item.name] = item 
    
def remove_item(self, name):
    if name in self.items:
            del self.items[name]
    else:
            print(f"Item '{name}' not found in inventory.")
           
def get_total_inventory_value(self):
     return sum(item.calculate_total_value() for item in self.items.values())

def display_inventory(self):
    if not self.items:
            print("Inventory is empty.")
    else:
            print("Current Inventory:")
            for item in self.items.values():
                print(item)

def item_exists(self, name):
     return name in self.items

InventoryItem = InventoryItem(name= "Television",quantity=20,price_per_unit=56000)
InventoryItem = InventoryItem(name="iron",quantity=30,price_per_unit=560)

item1 = InventoryItem(name="Television", quantity=10, price_per_unit=56000)
item2 = InventoryItem(name="iron", quantity=50, price_per_unit=560)

InventoryItem.add_item(item1)
InventoryItem.add_item(item2)

InventoryItem.display_Inventoryitem()

inventory = InventoryItem()
item1 = InventoryItem(name="Television", quantity=10, price_per_unit=56000)
item2 = InventoryItem(name="iron", quantity=30, price_per_unit=19.99)
inventory.add_item(item1)
inventory.add_item(item2)
total_inventory_value = inventory.get_total_inventory_value()
print(f"The total value of the entire inventory is: ${total_inventory_value:.2f}")

InventoryItem = InventoryItem()
item1 = InventoryItem(name="Television", quantity=10, price_per_unit=56000)
item2 = InventoryItem(name="iron", quantity=50, price_per_unit=560)
InventoryItem.add_item(item1)
InventoryItem.add_item(item2)
print("Before removal:")
InventoryItem.display_inventory()
InventoryItem.remove_item("Mouse")
print("\nAfter removal:")
InventoryItem.display_inventory()
InventoryItem.remove_item("Keyboard")

inventory = InventoryItem()

item1 = InventoryItem(name="Television", quantity=10, price_per_unit=56000)
item2 = InventoryItem(name="iron", quantity=50, price_per_unit=560)

inventory.add_item(item1)
inventory.add_item(item2)

print("Does 'Television' exist in the inventory?", inventory.item_exists("Telervision"))
print("Does 'iron' exist in the inventory?", inventory.item_exists("iron"))

inventory = InventoryItem()

item1 = InventoryItem(name="Television", quantity=10, price_per_unit=56000)
item2 = InventoryItem(name="iron", quantity=50, price_per_unit=560)

inventory.add_item(item1)
inventory.add_item(item2)

print("Does 'Television' exist in the inventory?", inventory.item_exists("Television"))
print("Does 'iron' exist in the inventory?", inventory.item_exists("iron"))


