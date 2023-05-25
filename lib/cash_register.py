#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, product_name, price, quantity=1):
    for _ in range(quantity):
      self.items.append(product_name)
    self.total += price * quantity
    self.last_object = ({'items': product_name, 'price': price, 'quantity': quantity})

  def apply_discount(self):
    if self.discount:
      self.total *= ((100 - self.discount) / 100)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
    
  def void_last_transaction(self):
    self.total -= self.last_object.get('price') * self.last_object.get('quantity')
    for _ in range(self.last_object.get("quantity")): 
      self.items.pop()

cash_register = CashRegister()
cash_register.add_item("tomato", 5, 2)
print(cash_register.items)
  
