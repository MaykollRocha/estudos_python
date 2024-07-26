class Rectangle:
    def __init__(self,width,height):
        self.__width = width
        self.__height = height

    def set_width(self,width):
        self.__width = width
    
    def set_height(self,height):
        self.__height = height

    def get_area(self):
        return self.__width * self.__height
    
    def get_perimeter(self):
        return  (2 *self.__width + 2 * self.__height)
    def get_picture(self):
        if self.__height > 50 or self.__width > 50: 
            return 'Too big for picture.'
        string = ''
        for _ in range(self.__height):
            string += '*'*self.__width + '\n'
        return string
    def get_diagonal(self):
        return (self.__width**2 + self.__height**2)**(1/2)
    def __str__(self):
        return f'Rectangle(width={self.__width}, height={self.__height})'
    def get_amount_inside(self,form):
        return self.get_area()//form.get_area()

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)
        self.side = side
    
    def set_width(self, width):
        self.set_side(width)
    
    def set_height(self, height):
        self.set_side(height)
    
    def __str__(self):
        return f'Square(side={self.side})'
   
rect = Rectangle(51, 2)
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
rect.set_width(10)
print(rect.get_amount_inside(sq))