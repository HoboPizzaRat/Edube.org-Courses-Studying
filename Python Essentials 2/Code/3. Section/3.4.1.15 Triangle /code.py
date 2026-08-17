import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        d_x = abs(self.__x - x)
        d_y = abs(self.__y - y)
        distance = (d_x**2 + d_y**2)**0.5
        return distance

    def distance_from_point(self, point):
        d_x = abs(self.__x - point.getx())
        d_y = abs(self.__y - point.gety())
        distance = (d_x**2 + d_y**2)**0.5
        return distance


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__point1 = vertice1
        self.__point2 = vertice2
        self.__point3 = vertice3

    def perimeter(self):
        distance12 = self.__point1.distance_from_point(self.__point2)
        distance23 = self.__point2.distance_from_point(self.__point3)
        distance13 = self.__point1.distance_from_point(self.__point3)
        return distance12 + distance23 + distance13


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
