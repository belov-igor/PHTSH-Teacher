# -*- coding: utf-8 -*-

# Две окружности: https://acmp.ru/index.asp?main=task&id_task=26

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point[x={self.x}, y={self.y}]"


class Circle:
    def __init__(self, point_center, radius):
        self.point_center = point_center
        self.radius = radius

    def __str__(self):
        return f"Circle[center = {self.point_center}, radius = {self.radius}]"


def intersection_of_circles(circle_1, circle_2):
    x_distance = circle_1.point_center.x - circle_2.point_center.x
    y_distance = circle_1.point_center.y - circle_2.point_center.y
    r1 = circle_1.radius
    r2 = circle_2.radius
    return (r2-r1)**2 <= (x_distance**2 + y_distance**2) <= (r2+r1)**2


a = Point(1, 1)
r1 = 1
circle_1 = Circle(a, r1)

b = Point(4, 4)
r2 = 1
circle_2 = Circle(b, r2)

print(intersection_of_circles(circle_1, circle_2))