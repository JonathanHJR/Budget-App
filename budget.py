class Category:
  
  def __init__(self, name): # set parameters are always used EXACTLY, not in quotations
    self.name = name # naming of category
    self.ledger = list() 

  def __str__(self): # creating the main object printed output
    title = f"{self.name:*^30}\n" # f string, center aligning with * filling + 30 characters condition
    transactions = ""
    total = 0
    for transaction in self.ledger:                # not sure why the below format works to define index range
      transactions += f"{transaction['description'][0:23]:23}" + f"{transaction['amount']:>7.2f}\n" # description from dict only 23 characters long and amount is right aligned 7 spaces with 2 dp, all within 30 characters max with 23 reserved for desc
      total += transaction['amount']
    output = title + transactions + "Total: " + str(total)
    return output
    
  def deposit(self, amount, description = ""):
    self.ledger.append({'amount': amount, 'description': description}) # append dict key values to self.ledger list

  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({'amount': -amount, 'description': description}) # same but for negative values
      return True
    return False
    
  def get_balance(self):
    total_balance = 0
    for transaction in self.ledger:
      total_balance += transaction['amount']
    return total_balance

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    return False

  def check_funds(self, amount):
    if self.get_balance() >= amount:
      return True
    return False

  def get_withdrawals(self):
    total_withdrawals = 0
    for transaction in self.ledger: # for loop only self is used, 'amount' != amount
      if transaction['amount'] < 0:
        total_withdrawals += transaction['amount']
    return total_withdrawals

def truncate(self):  # test replace n with self
  multiplier = 10
  return int(self * multiplier) / multiplier
  
def get_totals(categories):
  all_totals = 0
  breakdown = list()
  for category in categories: # for loop only categories is used and required input that leads to a return value
    all_totals += category.get_withdrawals()
    breakdown.append(category.get_withdrawals())
  rounded = list(map(lambda x: truncate(x / all_totals), breakdown)) # try rounded arithmetic formula # map = Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.) The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .
  return rounded
    
def create_spend_chart(categories):
  chart_title = "Percentage spent by category\n"
  pc = 100
  totals = get_totals(categories)
  while pc >= 0:
    spaces = " "
    for each_total in totals:
      if each_total * 100 >= pc:
        spaces += "o  "
      else:
        spaces += "   "
    chart_title += str(pc).rjust(3) + "|" + spaces + ("\n")
    pc -= 10 
    
  dashes = "-" + "---"*len(categories)
  names = list()
  x_axis = ""
  for category in categories:
    names.append(category.name)
  maxcat = max(names, key = len) # loop through all keys and find the max length value instead of returning just the longest key (category in this case)

  for x in range(len(maxcat)):
    nameStr = "     "
    for name in names:
      if x >= len(name):
        nameStr += "   "
      else:
        nameStr += name[x] + "  " 

    if x != len(maxcat) -1:
      nameStr += '\n'

    x_axis += nameStr

  chart_title += dashes.rjust(len(dashes) + 4) + "\n" + x_axis
  return chart_title