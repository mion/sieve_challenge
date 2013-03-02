import re

class Price:

  def __init__(self, amount, cents=0):
    self.amount = amount
    self.cents = cents

  def __eq__(self, other):
    return self.amount == other.amount and self.cents == other.cents

  def __str__(self):
    return str(self.amount) + "," + str(self.cents)
    
  @staticmethod
  def parse(s, money_sym='$'):
    separators = [",", "."]
    amount = ""
    cents = ""
    cents_flag = False
    cents_counter = 0
    beg = s.find(money_sym)

    if beg == -1:
      return None

    for i in range (beg, len(s)):
      if cents_counter >= 2: break # stop after reading 2 cents digits

      if s[i].isdigit():
      	if not cents_flag:
          amount += s[i]
        else:
          cents += s[i]
          cents_counter += 1
      elif s[i] in separators:
          cents_flag = True
 
    return Price(int(amount), int(cents) if cents_flag else 0)
