class Rectangle :
    def __init__(self, width ,height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
        return self.width

    def set_height(self,height):
        self.height = height
        return self.height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.width + self.height) * 2
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if self.width < 50 and self.height < 50:
            shape = ''
            line = self.width * '*'
            for i in range(self.height):
                shape += line+'\n'
            return shape
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape):
        x = self.get_area()
        y = shape.get_area()
        n = x / y
        return int(n)
    
    def __str__(self):
        dip = f"Rectangle(width={self.width}, height={self.height})"
        return  dip


class Square(Rectangle):
    def __init__(self, side_length):
        self.height = self.width = side_length

    def set_side(self, side_length):
        self.height = self.width = side_length
        return side_length
    
    def set_width(self, side_length):
        self.height = self.width = side_length
        return self.width

    def set_height(self,side_length):
        self.height = self.width = side_length
        return self.height

    def __str__(self):
        dip = f"Square(side={self.width})"
        return  dip




rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

# ---->>>>>>
            #50
            #26
            #Rectangle(width=10, height=3)
            #**********
            #**********
            #**********

            #81
            #5.656854249492381
            #Square(side=4)
            #****
            #****
            #****
            #****

            #8