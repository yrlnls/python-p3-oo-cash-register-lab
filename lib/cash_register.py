#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0):
    self.total = 0
    self.items = []
    self.discount = discount
    self.last_transaction = 0

  def add_item(self,title,price,quantity=1):
    item_total = price * quantity
    items_to_add = [(title) for _ in range(quantity)]
    self.items.extend(items_to_add)
    self.total += item_total
    self.last_transaction = item_total
    
  def apply_discount(self):
    if self.discount:
      discount_amount = (self.discount / 100) * self.total
      self.total -= discount_amount
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
    
  def void_last_transaction(self):
    self.total -= self.last_transaction
    self.last_transaction = 0
