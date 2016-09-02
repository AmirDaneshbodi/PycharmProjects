from math import radians, cos, sqrt, sin, tan

from Jensen_component.wake_read_layout import read_layout


def order_layout(farm, wind_angle):

    x, y = read_layout(farm)
    ordered = []

    for tur in range(len(x)):
        ordered.append([distance_to_front2(x[tur], y[tur], wind_angle), tur])

    ordered.sort()
    print(ordered)
    return [ordered[i][1] for i in range(len(ordered))], [x[ordered[i][1]] for i in range(len(ordered))], [y[ordered[i][1]] for i in range(len(ordered))]


def distance_to_front(x, y, angle):

    thetar = radians(angle)
    a = sin(thetar)
    b = - cos(thetar)

    return (a * x - b * y) / sqrt(a ** 2.0 + b ** 2.0)


def distance_to_front2(x, y, theta):
    theta = radians(theta + 90.0)

    return abs(x + radians(theta) * y - 1000000000000000.0 / cos(theta)) / sqrt(1.0 + tan(theta) ** 2.0)



if __name__ == '__main__':
    print(order_layout('coordinates.dat', 270.0))
