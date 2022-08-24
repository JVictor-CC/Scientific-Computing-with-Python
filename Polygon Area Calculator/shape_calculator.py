class Rectangle:

  def __init__(self, w_val, h_val):
    self.width = int(w_val)
    self.height = int(h_val)

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  
  def set_width(self, w_val):
    self.width = int(w_val)
    
  def set_height(self, h_val):
    self.height = int(h_val)
    
  def get_area(self):
    return (self.width * self.height)
  
  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)
    
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      _print = ''
      for i in range(self.height):
        _print += f"{'*' * self.width}\n"
      return _print  
    
  def get_amount_inside(self, a_shape):
    if a_shape.width > self.width or a_shape.height > self.height:
      return 0
    else:
      return (self.width // a_shape.width) * (self.height // a_shape.height)

class Square(Rectangle):

  def __init__(self, len):
    self.set_side(len)

  def __str__(self):
    return f"Square(side={self.width})"

  def set_side(self, len):
    self.width = len
    self.height = len

  def set_width(self, len): 
    self.set_side(len)

  def set_height(self, len):
    self.set_side(len)