__author__ = 'Sebastian Sanchez Perez Moreno' \
             's.sanchezperezmoreno@tudelft.nl'
# Jensen wake model with partial shadowing factor applied to horns rev. Must change Ct according to wind speed.
import wake
from math import sqrt, log, tan, cos
from numpy import deg2rad
import time

# output = open('matrix_jensen.dat', 'w')
# output.write('# This file has the wake deficit matrix per turbine per wind direction\n')
# output2 = open('final_speed_jensen.dat', 'w')
# output2.write('# This file has the deficit, wind speed and power at each turbine per wind direction.\n# Turbine number\tX-coordinate\tY-coordinate\tTotal speed deficit\tTotal wind speed\tWind direction angle\tPower produced\n')
layout = open('horns_rev.dat', 'r')
# layout = open('layout.dat', 'r')
windrose = open('horns_rev_windrose2.dat', 'r')
# draw = open('draw_horns_rev_jensen.dat', 'w')
# draw.write('# This file has the turbines affected by the wake of one turbine at one direction.\n')
# draw2 = open('drawline.dat', 'w')
turb_data = open('turb17_jensen.dat', 'w')
direction = open('direction_farmpower_jensen_horns.dat', 'w')
# direction.write('# This file includes the efficiency of the whole farm by wind direction.\n# Wind direction angle\tFarm efficiency\n')
# row = open('row_data_jensen.dat', 'w')
# data = open('rows_jensen.dat', 'w')

def analysis():

    layout_x = []
    layout_y = []
    for line in layout:
        columns = line.split()
        layout_x.append(float(columns[0]))
        layout_y.append(float(columns[1]))

    windrose_angle = []
    windrose_speed = []
    windrose_frequency = []
    for line in windrose:
        columns = line.split()
        windrose_angle.append(float(columns[0]))
        windrose_speed.append(float(columns[1]))
        windrose_frequency.append(float(columns[2]))

    layout.close()
    windrose.close()

    def Ct(U0):
        return 0.0001923077 * U0 ** 4.0 + -0.0075407925 * U0 ** 3.0 + 0.096462704 * U0 ** 2.0 - 0.5012354312 * U0 + 1.7184749184

    def power(U0):
        if U0 < 4.0:
            return 0.0
        elif U0 <= 25.0:
            return 0.0003234808 * U0 ** 7.0 - 0.0331940121 * U0 ** 6.0 + 1.3883148012 * U0 ** 5.0 - 30.3162345004 * U0 ** 4.0 + 367.6835557011 * U0 ** 3.0 - 2441.6860655008 * U0 ** 2.0 + 8345.6777042343 * U0 - 11352.9366182805
        else:
            return 0.0

    # for U0 in range(4, 20):
    nt = 80  # Number of turbines ## Length of layout list
    summation = 0.0
    aver = [0.0 for x in range(nt)]

    def distance_to_front(x, y, theta, r): ## TODO: Calculate distance to any front and use negative distances to order.
        theta = deg2rad(theta)
        return abs(x + tan(theta) * y - r / cos(theta)) / sqrt(1.0 + tan(theta) ** 2.0)

    for wind in range(0, len(windrose_angle)):
    # for wind in range(90, 91):
        # if wind in [100, 133, 271, 280, 313]:
        #     continue
        # U1 = windrose_speed[wind]  # Free stream wind speed
        # U0 = U1 * (70.0 / 10.0) ** 0.11 # Power or log law for wind shear profile
        # U0 = U1 * log(70.0 / 0.005) / log(10.0 / 0.005)
        U0 = 8.5
        k = 0.04  # Decay constant
        r0 = 40.0  # Turbine rotor radius
        angle = windrose_angle[wind]
        angle3 = angle + 180.0
        deficit_matrix = [[0.0 for x in range(nt)] for x in range(nt)]
        proportion = [[0.0 for x in range(nt)] for x in range(nt)]
        distance = [[0.0 for x in range(2)] for x in range(nt)]

        U = [U0 for x in range(nt)]
        total_deficit = [0.0 for x in range(nt)]

        for tur in range(nt):
            distance[tur] = [distance_to_front(layout_x[tur], layout_y[tur], angle, 100000000.0), tur]
        distance.sort()

        for turbine in range(nt):
            for num in range(turbine):
                total_deficit[distance[turbine][1]] += deficit_matrix[distance[turbine][1]][distance[num][1]] ** 2.0
            total_deficit[distance[turbine][1]] = sqrt(total_deficit[distance[turbine][1]])
            U[distance[turbine][1]] = U0 * (1.0 - total_deficit[distance[turbine][1]])
            for i in range(turbine + 1, nt):
                proportion[distance[turbine][1]][distance[i][1]] = wake.determine_if_in_wake(layout_x[distance[turbine][1]], layout_y[distance[turbine][1]], layout_x[distance[i][1]], layout_y[distance[i][1]], k, r0, angle3)
                # If statement for proportion = 0
                deficit_matrix[distance[i][1]][distance[turbine][1]] = proportion[distance[turbine][1]][distance[i][1]] * wake.wake_deficit(Ct(U[distance[turbine][1]]), k, wake.distance(layout_x[distance[turbine][1]], layout_y[distance[turbine][1]], layout_x[distance[i][1]], layout_y[distance[i][1]]), r0)

        # for turb in range(nt):
        #     for i in range(nt):
        #         output.write('{0:f}\t'.format(deficit_matrix[turb][i]))
        #     output.write('\n')
        #     output2.write('{0:d}\t{1:.1f}\t{2:.1f}\t{3:f}\t{4:f}\t{5:d}\t{6:f}\n'.format(turb, layout_x[turb], layout_y[turb], total_deficit[turb], U[turb], int(angle), power(U[turb])))
        # output2.write('\n')

        # for n in range(nt):
        #     aver[n] += power(U[n]) / 360.0

        turb_data.write('{0:f}\n'.format(power(U[14])))

        # Farm efficiency
        profit = 0.0
        efficiency_proportion = [0.0 for x in range(0, len(windrose_frequency))]
        for l in range(nt):
            profit += power(U[l])
        efficiency = profit * 100.0 / (float(nt) * power(U[distance[0][1]])) # same as using U0
        efficiency_proportion[wind] = efficiency * windrose_frequency[wind] / 100.0
        # print 'Farm efficiency with wind direction = {0:d} deg: {1:2.2f}%'.format(int(angle), efficiency)
        direction.write('{0:f}\t{1:f}\n'.format(angle, profit))
        summation += efficiency_proportion[wind]
    print 'total farm efficiency is {0:f} %'.format(summation)
    # for n in range(nt):
    #     turb_data.write('{0:f}\n'.format(aver[n]))
    turb_data.close()
    # output.close()
    # output2.close()
    # draw.close()
    direction.close()
    # row.close()
    # data.close()

if __name__ == '__main__':
    start_time = time.time()
    analysis()
    print("--- %s seconds ---" % (time.time() - start_time))