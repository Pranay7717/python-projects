class Wallet:
  def __init__(self, own, balance):
      self.own = own
    self.__balance = balance
  @property
  def g_balance(self):
    return self.__balance
  @g_balance.setter
  def g_balance(self, amount):
    if amount > 0:
     self.__balance = amount
    else:
      print("Invalid amount")
  def add_money(self, amount):
    self.__balance += amount
m_w = Wallet("pranay", -5)
print(m_w.own)
print(m_w.g_balance)