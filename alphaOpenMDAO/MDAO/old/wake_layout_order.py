from math import radians, cos, sqrt, sin

from old.wake_read_layout import ReadLayout


class LayoutOrder:
    def __init__(self, farm, wind_angle):
        self.farm = farm
        self.wind_angle = wind_angle

    def order_layout(self):
        farm = self.farm
        wind_angle = self.wind_angle
        x, y = ReadLayout(farm).read_layout()
        distance = []
        for tur in range(len(x)):
            distance.append([DistanceToFront(x[tur], y[tur], wind_angle).distance_to_front(), tur])
        distance.sort()
        return distance


class DistanceToFront:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def distance_to_front(self):
        angle = self.angle
        x = self.x
        y = self.y

        theta = 90.0 - angle
        thetar = radians(theta)
        a = sin(thetar)
        b = - cos(thetar)

        return (a * x - b * y) / sqrt(a ** 2.0 + b ** 2.0)




if __name__ == '__main__':
    print(LayoutOrder('horns_rev.dat', 45.0).order_layout())
