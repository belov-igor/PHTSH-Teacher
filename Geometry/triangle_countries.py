# -*- coding: utf-8 -*-


# Треугольные страны: https://acmp.ru/index.asp?main=task&id_task=90
# Треугольники и точка: https://acmp.ru/index.asp?main=task&id_task=102


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point[x={self.x}, y={self.y}]'


class Triangle:
    def __init__(self, vertex_1, vertex_2, vertex_3):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.vertex_3 = vertex_3

    def __str__(self):
        return f'Triangle[vertex 1 = {self.vertex_1}, vertex 2 = {self.vertex_2}, vertex 3 = {self.vertex_3}]'


class Vector:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        self.x_component = end_point.x - start_point.x
        self.y_component = end_point.y - start_point.y

    def __str__(self):
        return f'Vector [start = {self.start_point}, end = {self.end_point}]'


def vector_cross_product(vector_1, vector_2):
    return vector_1.x_component * vector_2.y_component - vector_2.x_component * vector_1.y_component


def hitting_the_triangle(point, triangle):
    vertex_1 = triangle.vertex_1
    vertex_2 = triangle.vertex_2
    vertex_3 = triangle.vertex_3
    vector_1 = Vector(vertex_1, point)
    vector_2 = Vector(vertex_2, point)
    vector_3 = Vector(vertex_3, point)
    product_1 = vector_cross_product(vector_1, Vector(vertex_1, vertex_2))
    product_2 = vector_cross_product(vector_2, Vector(vertex_2, vertex_3))
    product_3 = vector_cross_product(vector_3, Vector(vertex_3, vertex_1))
    # для треугольников и точки
    # return (product_1 >= 0 and product_2 >= 0 and product_3 >= 0) or (product_1 <= 0 and product_2 <= 0 and
    # product_3 <= 0)

    # для треугольных стран
    return (product_1 > 0 and product_2 > 0 and product_3 > 0) or (product_1 < 0 and product_2 < 0 and product_3 < 0)


# Для треугольных стран
triangles = [
    [[-2, 0], [2, 0], [0, 2]],
    [[-3, 0], [3, 0], [0, 3]]
]
o = Point(0, 1)
# o = Point(0, 2)

# Для треугольников и точки
# triangles = [
#     [[0, 0], [100, 0], [0, 100]],
# ]
# o = Point(100, 100)
# o = Point(10, 10)
# o = Point(50, 50)
# o = Point(0, 0)

for vertexes in triangles:
    a = Point(x=vertexes[0][0], y=vertexes[0][1])
    b = Point(x=vertexes[1][0], y=vertexes[1][1])
    c = Point(x=vertexes[2][0], y=vertexes[2][1])
    triangle = Triangle(a, b, c)
    print(hitting_the_triangle(o, triangle))
