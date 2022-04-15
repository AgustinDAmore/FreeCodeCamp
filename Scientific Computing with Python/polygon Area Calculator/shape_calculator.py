
class Rectangle:

    __slots__ = ["width","height"]

    def __init__(self,Width,Height) -> None:
        self.width = int
        self.height = int

        self.width = Width    
        self.height = Height    

    def set_width(self,Width):
        self.width = Width

    def set_height(self,Height):
        self.height = Height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        assert self.height <= 50 or self.width <= 50, 'Too big for picture.'
        for i in range(self.height):
            print("*"*self.width)
        return ""

    def get_amount_inside(self,square):
        return self.get_area()//square.get_area()

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

class Square:

    __slots__ = ["side"]

    def __init__(self,Side) -> None:
        self.side = Side    

    def set_side(self,Side):
        self.side = Side

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return (2 * self.side + 2 * self.side)

    def get_diagonal(self):
        return ((self.side ** 2 + self.side ** 2) ** .5)

    def get_picture(self):
        assert self.side <= 50, 'Too big for picture.'
        for i in range(self.side):
            print("*"*self.side)
        return ""

    def get_amount_inside(self,rectangle):
        return self.get_area()//rectangle.get_area()

    def __repr__(self) -> str:
        return f"Square(side={self.side})"