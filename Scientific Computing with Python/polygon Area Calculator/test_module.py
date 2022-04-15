import shape_calculator

rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
# 50
rect.set_height(3)
print(rect.get_perimeter())
# 26
print(rect)
# Rectangle(width=10, height=3)
print(rect.get_picture())
# **********
# **********
# **********

sq = shape_calculator.Square(9)
print(sq.get_area())
# 81
sq.set_side(4)
print(sq.get_diagonal())
# 5.656854249492381
print(sq)
# Square(side=4)
print(sq.get_picture())
# ****
# ****
# ****
# ****

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
# 8