# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main


rect = shape_calculator.Rectangle(10, 15)
rect2 = shape_calculator.Rectangle(5,8)
print(rect.get_area())
print(rect.get_perimeter())
print(rect.get_picture())
print(rect2.get_picture())
print(rect.get_amount_inside(rect2))
print(rect)
print('________________________________\n')
sq = shape_calculator.Square(4)
print(sq.get_picture())
print(sq.get_area())
print(sq.get_diagonal())
print(sq)


# Run unit tests automatically
main(module='test_module', exit=False)