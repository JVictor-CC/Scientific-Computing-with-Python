class Category:

  def __init__(self, name):
    self.name = name
    self.total = 0  
    self.total_spent = 0
    self.ledger = list()

  def __str__(self):
    _print = f"{self.name:*^30}\n"
    for i in self.ledger:
      _print += f"{i['description'][:23]:23}{i['amount']:>7.2f}\n"
    _print += f"Total: {self.total:.2f}"
    return _print
  
  def deposit(self,amount, description = ''):
    aux = {"amount": amount, "description": description}
    self.ledger.append(aux)
    self.total+=amount
    
  def withdraw(self,amount,description = ''):
    if self.check_funds(amount):
      aux = {"amount": -amount, "description": description}
      self.ledger.append(aux)
      self.total -= amount
      self.total_spent += amount
    
    return self.check_funds(amount)
    
  def get_balance(self):
    return self.total

  def get_total_spent(self):
    return self.total_spent
  
  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount,f'Transfer to {category.name}')
      category.deposit(amount, f'Transfer from {self.name}')
        
    return self.check_funds(amount)
      
  def check_funds(self, amount): 
    if self.total >= amount:
      return True
    else:
      return False




  
def create_spend_chart(categories):
  
  total_spent = list()
  bar_chart = ''
  names = list()
  percentage = list()
  
  for i in range(len(categories)):
    total_spent.append(categories[i].get_total_spent())
    names.append(categories[i].name)

  for i in range(len(total_spent)):
    percentage.append((total_spent[i] / sum(total_spent)) * 100)
  
  #print(sum(total_spent),'\n',percentage,'\n\n')
  
  bar_chart += 'Percentage spent by category\n'
  for i in range(100,-1,-10):
    bar_chart += f"{str(i)+'|':>4}"
    for val in percentage:
      if val >= i:
        bar_chart += ' o '
      else:
        bar_chart += '   '
    bar_chart+= ' \n'

  bar_chart += f"{'--'*(len(percentage)+2):>{4*len(percentage)+2}}"  

  larg_name = max(names,key = len)
  for i in range(len(larg_name)):
    bar_chart += '\n'
    bar_chart += f"{' ':>4} "
    for j in names:
      if i >= len(j):
        bar_chart += f"   "
      else:
        bar_chart += f"{j[i]}  "
        
  return bar_chart