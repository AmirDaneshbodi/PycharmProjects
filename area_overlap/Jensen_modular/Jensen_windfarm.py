__author__ = 'Sebastian Sanchez Perez Moreno' \
             's.sanchezperezmoreno@tudelft.nl'
# Jensen wake model with partial shadowing factor applied to horns rev. Must change Ct according to wind speed.
import wake
from math import sqrt, log, tan, cos, floor, ceil, pi, sin
from numpy import radians
import time
from eddy_viscosity_integrate import ainslie


def power(U0):
    return power_bladed(U0)


def Ct(U0):
    return ct_bladed(U0)


def power_bladed(U0):
    return 0.5 * 61.0 ** 2.0 * pi * 1.225 * 0.485 * U0 ** 3.0


def ct_bladed(U0):
    return 0.781


def ct_table(U0):
    v = U0
    if v == 7: return 0.977
    if v == 8: return 0.943
    if v == 9: return 0.899
    if v == 10: return 0.852
    if v == 11: return 0.804


def ct_TTL(U0):
    if ceil(U0) == floor(U0):
        return ct_table(U0)
    else:
        return interpolate(floor(U0), ct_table(floor(U0)), ceil(U0), ct_table(ceil(U0)), U0)


def power_table(U0):
    v = U0
    if v == 7: return 970.0
    if v == 8: return 1780.0
    if v == 9: return 2770.0
    if v == 10: return 3910.0
    if v == 11: return 5190.0


def power_TTL(U0):
    if ceil(U0) == floor(U0):
        return power_table(U0)
    else:
        return interpolate(floor(U0), ct_table(floor(U0)), ceil(U0), ct_table(ceil(U0)), U0)


def interpolate(minx, miny, maxx, maxy, valx):
    print maxx, minx
    return miny + (maxy - miny) * ((valx - minx) / (maxx - minx))


def distance_to_front(x, y, theta):
    theta = radians(theta)
    return abs(x + tan(theta) * y - 10000000000.0 / cos(theta)) / sqrt(1.0 + tan(theta) ** 2.0)


def determine_front(wind_angle, x_t1, y_t1, x_t2, y_t2):
    wind_angle = radians(wind_angle)
    a = (x_t2 - x_t1) * cos(wind_angle) + (y_t2 - y_t1) * sin(wind_angle)
    if a > 0.0:
        return a
    else:
        return 0.0


class Layout:
    def __init__(self, layout_file):

        self.layout = open(layout_file, 'r')
        self.layout_x = []
        self.layout_y = []
        self.efficiency = 0.0
        self.profit = []
        self.U = []
        self.powers = []
        self.summation = 0.0

        for line in self.layout:
            columns = line.split()
            self.layout_x.append(float(columns[0]))
            self.layout_y.append(float(columns[1]))

    def jensen_angle(self, U0, angle):

        nt = len(self.layout_y)  # Number of turbines ## Length of layout list

        k = 0.04  # Decay constant
        r0 = 62.0  # Turbine rotor radius
        angle2 = - 270.0 - angle  # To read windroses where N is 0 and E is 90.
        angle3 = angle + 180.0
        deficit_matrix = [[0.0 for _ in range(nt)] for _ in range(nt)]
        proportion = [[0.0 for _ in range(nt)] for _ in range(nt)]
        distance = [[0.0 for _ in range(2)] for _ in range(nt)]
        self.U = [U0 for _ in range(nt)]
        total_deficit = [0.0 for _ in range(nt)]

        for tur in range(nt):
            distance[tur] = [distance_to_front(self.layout_x[tur], self.layout_y[tur], angle), tur]
        distance.sort()

        for turbine in range(nt):
            for num in range(turbine):
                total_deficit[distance[turbine][1]] += deficit_matrix[distance[turbine][1]][distance[num][1]] ** 2.0

            total_deficit[distance[turbine][1]] = sqrt(total_deficit[distance[turbine][1]])
            self.U[distance[turbine][1]] = U0 * (1.0 - total_deficit[distance[turbine][1]])

            for i in range(turbine + 1, nt):

                determ = wake.determine_if_in_wake(self.layout_x[distance[turbine][1]],
                                                           self.layout_y[distance[turbine][1]],
                                                           self.layout_x[distance[i][1]], self.layout_y[distance[i][1]], k,
                                                           r0, angle3)
                proportion[distance[turbine][1]][distance[i][1]] = determ[0]

                if proportion[distance[turbine][1]][distance[i][1]] != 0.0:
                    deficit_matrix[distance[i][1]][distance[turbine][1]] = proportion[distance[turbine][1]][
                                                                               distance[i][1]] * wake.wake_deficit(
                        Ct(self.U[distance[turbine][1]]), k, determ[1], r0)

        # Farm efficiency
        self.profit = 0.0

        for l in range(nt):
            self.profit += power(self.U[l])
        self.efficiency = self.profit * 100.0 / (float(nt) * power(self.U[distance[0][1]]))  # same as using U0
        self.powers = [power(self.U[i]) for i in range(nt)]

        with open('speed_jensen.dat', 'w') as out:
            for i in range(len(self.U)):
                out.write('{0:f}\n'.format(self.U[i]))

    def jensen_windrose(self, windrose_file):

        windrose = open(windrose_file, 'r')
        windrose_angle = []
        windrose_speed = []
        windrose_frequency = []

        for line in windrose:
            columns = line.split()
            windrose_angle.append(float(columns[0]))
            windrose_speed.append(float(columns[1]))
            windrose_frequency.append(float(columns[2]))

        nt = len(self.layout_y)  # Number of turbines ## Length of layout list

        turb_data = open('turb1_power_jensen.dat', 'w', 1)
        direction = open('direction_power_jensen.dat', 'w', 1)

        for wind in range(len(windrose_angle)):
            U0 = windrose_speed[wind]  # Free stream wind speed
            k = 0.04  # Decay constant
            r0 = 62.0  # Turbine rotor radius
            angle = windrose_angle[wind]
            # angle2 = - 270.0 - angle  # To read windroses where N is 0 and E is 90
            angle3 = angle + 180.0
            deficit_matrix = [[0.0 for _ in range(nt)] for _ in range(nt)]
            proportion = [[0.0 for _ in range(nt)] for _ in range(nt)]
            distance = [[0.0 for _ in range(2)] for _ in range(nt)]
            U = [U0 for _ in range(nt)]
            total_deficit = [0.0 for _ in range(nt)]

            for tur in range(nt):
                distance[tur] = [distance_to_front(self.layout_x[tur], self.layout_y[tur], angle), tur]

            distance.sort()

            for turbine in range(nt):
                for num in range(turbine):
                    total_deficit[distance[turbine][1]] += deficit_matrix[distance[turbine][1]][distance[num][1]] ** 2.0

                total_deficit[distance[turbine][1]] = sqrt(total_deficit[distance[turbine][1]])
                U[distance[turbine][1]] = U0 * (1.0 - total_deficit[distance[turbine][1]])

                for i in range(turbine + 1, nt):

                    determ = wake.determine_if_in_wake(self.layout_x[distance[turbine][1]],
                                                               self.layout_y[distance[turbine][1]],
                                                               self.layout_x[distance[i][1]], self.layout_y[distance[i][1]], k,
                                                               r0, angle3)
                    proportion[distance[turbine][1]][distance[i][1]] = determ[0]

                    if proportion[distance[turbine][1]][distance[i][1]] != 0.0:
                        deficit_matrix[distance[i][1]][distance[turbine][1]] = proportion[distance[turbine][1]][
                                                                                   distance[i][1]] * wake.wake_deficit(
                            Ct(U[distance[turbine][1]]), k, determ[1], r0)

            # Farm efficiency
            efficiency_proportion = [0.0 for _ in range(len(windrose_frequency))]
            profit_sum = 0.0
            for l in range(nt):
                profit_sum += power(U[l])
            profit = profit_sum
            efficiency = profit * 100.0 / (float(nt) * power(U[distance[0][1]]))  # same as using U0
            efficiency_proportion[wind] = efficiency * windrose_frequency[wind] / 100.0
            self.summation += efficiency_proportion[wind]

            # turb_data.write('{0:f} {1:f}\n'.format(angle, power(U[2])))  # Number of turbine you want output of. Now 14.
            direction.write('{0:f} {1:f}\n'.format(angle, profit))
        turb_data.close()
        direction.close()

    def ainslie_windrose(self, windrose_file):

        D = 80.0  # Diameter

        for x in range(len(self.layout_x)):
            self.layout_x[x] = (self.layout_x[x] / D)

        for x in range(len(self.layout_y)):
            self.layout_y[x] = (self.layout_y[x] / D)

        layout_x = self.layout_x
        layout_y = self.layout_y

        windrose = open(windrose_file, 'r')
        windrose_angle = []
        windrose_speed = []
        windrose_frequency = []

        for line in windrose:
            columns = line.split()
            windrose_angle.append(float(columns[0]))
            windrose_speed.append(float(columns[1]))
            windrose_frequency.append(float(columns[2]))

        nt = len(self.layout_y)
        # turb_data = open('turb1_power_jensen.dat', 'w', 1)
        direction = open('direction_power_ainslie.dat', 'w', 1)

        for wind in range(0, len(windrose_angle)):

            U0 = windrose_speed[wind]  # Free stream wind speed
            angle = windrose_angle[wind]
            angle3 = angle + 180.0
            wake_deficit_matrix = [[0.0 for _ in range(nt)] for _ in range(nt)]
            distance = [[0.0 for _ in range(2)] for _ in range(nt)]
            total_deficit = [0.0 for _ in range(nt)]
            U = [U0 for _ in range(nt)]

            for tur in range(nt):
                distance[tur] = [distance_to_front(layout_x[tur], layout_y[tur], angle), tur]

            distance.sort()

            for turbine in range(nt):
                for num in range(turbine):
                    total_deficit[distance[turbine][1]] += wake_deficit_matrix[distance[turbine][1]][
                                                               distance[num][1]] ** 2.0
                total_deficit[distance[turbine][1]] = sqrt(total_deficit[distance[turbine][1]])
                U[distance[turbine][1]] = U0 * (1.0 - total_deficit[distance[turbine][1]])
                parallel_distance = [0.0 for x in range(nt)]
                perpendicular_distance = [0.0 for x in range(nt)]

                for i in range(turbine + 1, nt):
                    parallel_distance[distance[i][1]] = determine_front(angle3, layout_x[distance[turbine][1]],
                                                                        layout_y[distance[turbine][1]],
                                                                        layout_x[distance[i][1]],
                                                                        layout_y[distance[i][1]])
                    perpendicular_distance[distance[i][1]] = wake.crosswind_distance(radians(angle3),
                                                                                layout_x[distance[turbine][1]],
                                                                                layout_y[distance[turbine][1]],
                                                                                layout_x[distance[i][1]],
                                                                                layout_y[distance[i][1]])

                    if perpendicular_distance[distance[i][1]] <= 1.7 and parallel_distance[
                        distance[i][1]] > 0.0:  ## 1.7 gives same results as a bigger distance, many times faster.

                        wake_deficit_matrix[distance[i][1]][distance[turbine][1]] = ainslie(
                            Ct(U[distance[turbine][1]]), U[distance[turbine][1]],
                            parallel_distance[distance[i][1]], perpendicular_distance[distance[i][1]])
                    else:
                        wake_deficit_matrix[distance[i][1]][distance[turbine][1]] = 0.0
            # turb_data.write('{0:f} {1:f}\n'.format(angle, power(U[14])))
            # Farm efficiency
            profit = 0.0
            efficiency_proportion = [0.0 for _ in range(0, len(windrose_frequency))]
            for l in range(nt):
                profit += power(U[l])
            efficiency = profit * 100.0 / (float(nt) * power(U[distance[0][1]]))
            efficiency_proportion[wind] = efficiency * windrose_frequency[wind] / 100.0
            direction.write('{0:f} {1:f}\n'.format(angle, profit))
            self.summation += efficiency_proportion[wind]

    def ainslie_angle(self, wind_speed, angle):

        D = 126.0  # Diameter

        for x in range(len(self.layout_x)):
            self.layout_x[x] = (self.layout_x[x] / D)

        for x in range(len(self.layout_y)):
            self.layout_y[x] = (self.layout_y[x] / D)

        layout_x = self.layout_x
        layout_y = self.layout_y

        nt = len(self.layout_y)
        # turb_data = open('turb1_power_jensen.dat', 'w', 1)
        direction = open('direction_power_ainslie.dat', 'w', 1)
        U0 = wind_speed  # Free stream wind speed
        angle3 = angle + 180.0
        wake_deficit_matrix = [[0.0 for _ in range(nt)] for _ in range(nt)]
        distance = [[0.0 for _ in range(2)] for _ in range(nt)]
        total_deficit = [0.0 for _ in range(nt)]
        self.U = [U0 for _ in range(nt)]
        U = self.U

        for tur in range(nt):
            distance[tur] = [distance_to_front(layout_x[tur], layout_y[tur], angle), tur]

        distance.sort()

        for turbine in range(nt):
            for num in range(turbine):
                total_deficit[distance[turbine][1]] += wake_deficit_matrix[distance[turbine][1]][
                                                           distance[num][1]] ** 2.0
            total_deficit[distance[turbine][1]] = sqrt(total_deficit[distance[turbine][1]])
            U[distance[turbine][1]] = U0 * (1.0 - total_deficit[distance[turbine][1]])
            parallel_distance = [0.0 for x in range(nt)]
            perpendicular_distance = [0.0 for x in range(nt)]

            for i in range(turbine + 1, nt):
                parallel_distance[distance[i][1]] = determine_front(angle3, layout_x[distance[turbine][1]],
                                                                    layout_y[distance[turbine][1]],
                                                                    layout_x[distance[i][1]],
                                                                    layout_y[distance[i][1]])
                perpendicular_distance[distance[i][1]] = wake.crosswind_distance(radians(angle3),
                                                                                 layout_x[distance[turbine][1]],
                                                                                 layout_y[distance[turbine][1]],
                                                                                 layout_x[distance[i][1]],
                                                                                 layout_y[distance[i][1]])

                if perpendicular_distance[distance[i][1]] <= 1.7 and parallel_distance[
                    distance[i][1]] > 0.0:  ## 1.7 gives same results as a bigger distance, many times faster.

                    wake_deficit_matrix[distance[i][1]][distance[turbine][1]] = ainslie(
                        Ct(U[distance[turbine][1]]), U[distance[turbine][1]],
                        parallel_distance[distance[i][1]], perpendicular_distance[distance[i][1]])
                else:
                    wake_deficit_matrix[distance[i][1]][distance[turbine][1]] = 0.0
        # turb_data.write('{0:f} {1:f}\n'.format(angle, power(U[14])))
        # Farm efficiency
        profit = 0.0
        for l in range(nt):
            profit += power(U[l])
        self.efficiency = profit * 100.0 / (float(nt) * power(U[distance[0][1]]))
        self.powers = [power(self.U[i]) for i in range(nt)]

        with open('speed_ainslie.dat', 'w') as out:
            for i in range(len(self.U)):
                print U[i]
                out.write('{0:f}\n'.format(self.U[i]))

if __name__ == '__main__':
    a = Layout('coordinates.dat')
    a.jensen_angle(11.0, 180.0)
    # print(a.efficiency)
    # print(a.powers)
    # b = Layout('coordinates.dat')
    # b.jensen_windrose('windrose.dat')
    # print(b.summation)
    c = Layout('coordinates.dat')
    c.ainslie_angle(11.0, 180.0)
