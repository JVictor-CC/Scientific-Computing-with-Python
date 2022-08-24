import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self,**kwargs):
    if not kwargs:
      print('It needs at least one ball')
      return None
    else:
      self.contents = list()
      for keys, values in kwargs.items():
        self.contents += values * [keys]
      
  def draw(self, balls):
    elements = list()
    #selecting random elements
    if balls >= len(self.contents):
      return self.contents

    for i in range(balls):
      rem = self.contents.pop(int(len(self.contents) * random.random()))
      elements.append(rem)
    
    return elements
  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  print('\nHat: ',hat.contents,'\n')
  print('expected_balls: ',expected_balls,'\n')
  sum=0
  probability = 0
  for i in range(num_experiments):
    #make copies for each interaction
    exp_cpy = copy.deepcopy(expected_balls)
    hat_cpy = copy.deepcopy(hat)
    
    balls_drawn = hat_cpy.draw(num_balls_drawn)  
    
    # checks if values are in both lists and decreases by 1 if it's true
    for value in balls_drawn:
      if value in exp_cpy:
        exp_cpy[value] = exp_cpy[value] - 1
        
    # if all values within the expected values are less than zero, the counter adds 1.
    if all(values <= 0 for values in exp_cpy.values()):
      sum +=1
    
    probability = sum / num_experiments
  
  return probability