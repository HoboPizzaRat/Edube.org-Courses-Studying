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


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
