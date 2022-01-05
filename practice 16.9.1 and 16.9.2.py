# Задание 16.9.1
# Создайте класс любых геометрических фигур, где на выход мы получаем характеристики фигуры. Каждый экземпляр должен иметь
# атрибуты, которые зависят от выбранной фигуры. Например, для прямоугольника это будут аргументы x, y, width и height.
# Кроме того вы должны иметь возможность передавать эти атрибуты при создании объекта класса.
# Создайте метод, который возвращает атрибуты вашей фигуры в виде строки.
# Circle(1, 2, 3)
# Square(4, 5, 6)
class Shape:
       def __str__(self):
        if isinstance(self, Circle):
         return f'Circle({self.x},{self.y},{self.r})'
        if isinstance(self, Square):
         return f'Square({self.x},{self.y},{self.a})'
        if isinstance(self, Rectangle):
            return f'Rectangle({self.width},{self.height})'


class Circle (Shape):
 def __init__(self, x, y, r):
     self.x = x
     self.y = y
     self.r = r
class Square(Shape):
 def __init__(self, x, y, a):
  self.x = x
  self.y = y
  self.a = a

circle_1 = Circle (1, 2, 3)
square_1 = Square (1, 2, 3)
print(circle_1)
print(square_1)

# Задание 16.9.2
# Напишите код для описания геометрической фигуры.
# Создайте класс «прямоугольник» с помощью метода  __init__(). На выходе в консоли вам
# необходимо получить длину и ширину с итоговыми значениями.

class Rectangle(Shape):
 def __init__(self, width, height):
  self.width = width
  self.height = height
 def rectangle_area(self):
     return self.height * self.width
print(Rectangle(2,3))


