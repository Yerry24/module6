import math


class Figure:
    sides_count = 0

    def __init__(self, __sides,  __color,  filled):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r > 255 or g > 255 or b > 255:
            return False
        else:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def  __is_valid_sides(self, *args):
        if isinstance (self.__sides, list):
            if len(args) == len(self.__sides):
                return True
            else:
                return False
        elif (len(args) == 1) and (isinstance(self.__sides, int) or isinstance(self.__sides, float)):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimetr = 0
        for i in self.__sides:
            perimetr += i
        return perimetr

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            if len(self.__sides) > 1:
                self.__sides = new_sides
            else:
                self.__sides = []
                self.__sides.append(new_sides[0])

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *args):
        circle_sides = []
        self.side = 1
        if len(args) == self.sides_count:
            self.side = args[0]
        else:
            self.side = 1
        self.__radius = self.side / 3.14
        circle_sides.append(self.side)
        super().__init__(circle_sides, color, False)

    def get_square(self):
        return self.__radius * self.__radius * 3.14

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *args):
        triangle_sides = [1, 1, 1]
        if len(args) == self.sides_count:
            triangle_sides = [*args[0], *args[1], *args[2]]
        super().__init__(triangle_sides, color, False)

    def get_square(self):
        sides_triangle = self.get_sides()
        p = (sides_triangle[0] + sides_triangle[1] + sides_triangle[2])/2
        s = math.sqrt(p * (p - sides_triangle[0]) * (p - sides_triangle[1]) * (p - sides_triangle[2]))
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *args):
        cube_sides = []
        if len(args) == 1:
            for i in range(self.sides_count):
                cube_sides.append(args[0])
        else:
            for i in range(self.sides_count):
                cube_sides.append(1)
        super().__init__(cube_sides, color, False)

    def get_volume(self):
        sides_cube = self.get_sides()
        return sides_cube[0] * sides_cube[0] * sides_cube[0]

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверки функционала
c1 =  Circle((200, 200, 100), 10, 15, 6)
print(c1.get_sides())
print(c1.get_square())
t1 = Triangle((200, 200, 100), 10, 6)
print(t1.get_sides())
print(t1.get_square())
cu1 = Cube((200, 200, 100), 9)
print(cu1.get_sides())
cu2 = Cube((200, 200, 100), 9, 12)
print(cu2.get_sides())