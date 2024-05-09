class Figure:
    sides_count = 0

    def __init__(self, color, *args):
        self.__color = color
        self.filled = False
        self.set_sides(*args)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *args):
        if self.__is_valid_sides(*args):
            self.__sides = list(args)

    def __is_valid_sides(self, *args):
        return all(side > 0 for side in args) and len(args) == self.sides_count

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius)

    def get_square(self):
        return 3.14 * (self.get_sides()[0] ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *args):
        super().__init__(color, *args)

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__(color, *[side] * self.sides_count)

    def get_volume(self):
        return self.get_sides()[0] ** 3


# Создаем объекты и проверяем их
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)
cube1.set_color(300, 70, 15)
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)
circle1.set_sides(15)
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина
print(len(circle1))

# Проверка объема (куба)
print(cube1.get_volume())
