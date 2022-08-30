# -*- coding: utf-8 -*-

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


def point_in_circle(circle, point):
    difference_x = point.x-circle.point_center.x
    difference_y = point.y-circle.point_center.y
    return (difference_x**2 + difference_y**2) <= circle.radius**2


point_center = Point(6, 4)
circle = Circle(point_center, 3)

point_1 = Point(8, 3)
point_2 = Point(8, 1)

print(point_in_circle(circle, point_1))
print(point_in_circle(circle, point_2))
