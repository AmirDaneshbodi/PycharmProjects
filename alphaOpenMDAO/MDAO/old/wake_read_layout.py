from math import radians, sin, cos, sqrt


class Layout:
    def __init__(self, farm_layout):
        self.farm_layout = farm_layout

    def read_layout(self):
        farm_layout = self.farm_layout
        layout_x = []
        layout_y = []
        with open(farm_layout, 'r') as layout:
            for line in layout:
                columns = line.split()
                layout_x.append(float(columns[0]))
                layout_y.append(float(columns[1]))
        return layout_x, layout_y

    def order_layout(self, wind_angle):
        x, y = self.read_layout()
        ordered = []
        for tur in range(len(x)):
            ordered.append([self.distance_to_front(x[tur], y[tur], wind_angle), tur])
        ordered.sort()
        return ordered

    @staticmethod
    def distance_to_front(x, y, angle):
        theta = (angle - 90.0 + 270.0)
        thetar = radians(theta)
        a = sin(thetar)
        b = - cos(thetar)
        return (a * x - b * y) / sqrt(a ** 2.0 + b ** 2.0)

if __name__ == '__main__':
    horns = Layout('horns_rev.dat')
    print(horns.order_layout(340.0))
