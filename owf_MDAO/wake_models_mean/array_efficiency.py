from wake_models import jensen_1angle, ainslie_1angle, larsen_1angle
from layout import read_layout
from windrose import read_windrose
from power_models import power_v90 as power


def jensen_windrose(layout_file, windrose_file):

    layout_x, layout_y = read_layout(layout_file)
    wind_direction, wind_speed, wind_frequency = read_windrose(windrose_file)
    efficiency = []
    profit = []
    summation = 0.0
    nt = len(layout_y)
    P = []
    U = []

    efficiency_proportion = []

    for wind in range(len(wind_direction)):
        U0 = wind_speed[wind]  # Free stream wind speed
        angle = wind_direction[wind]
        # angle2 = - 270.0 - angle  # To read windroses where N is 0 and E is 90

        U.append(jensen_1angle(layout_x, layout_y, U0, angle, rotor_radius=40.0, k=0.04))
        P.append([power(u) for u in U[-1]])

        # Farm efficiency
        profit.append(sum(P[-1]))
        efficiency.append(profit[-1] * 100.0 / (float(nt) * max(P[-1])))  # same as using U0
        efficiency_proportion.append(efficiency[-1] * wind_frequency[wind] / 100.0)
        summation += efficiency_proportion[wind]

    # print profit
    # print efficiency
    # print efficiency_proportion
    # print U
    # print P

    return summation


def ainslie_windrose(layout_file, windrose_file):

    layout_x, layout_y = read_layout(layout_file)
    wind_direction, wind_speed, wind_frequency = read_windrose(windrose_file)
    efficiency = []
    profit = []
    summation = 0.0
    nt = len(layout_y)
    P = []
    U = []

    efficiency_proportion = []

    for wind in range(len(wind_direction)):
        U0 = wind_speed[wind]  # Free stream wind speed
        angle = wind_direction[wind]
        # angle2 = - 270.0 - angle  # To read windroses where N is 0 and E is 90

        U.append(ainslie_1angle(layout_x, layout_y, U0, angle, rotor_radius=40.0, TI=0.08))
        P.append([power(u) for u in U[-1]])

        # Farm efficiency
        profit.append(sum(P[-1]))
        efficiency.append(profit[-1] * 100.0 / (float(nt) * max(P[-1])))  # same as using U0
        efficiency_proportion.append(efficiency[-1] * wind_frequency[wind] / 100.0)
        summation += efficiency_proportion[wind]

    # print profit
    # print efficiency
    # print efficiency_proportion
    # print U
    # print P

    return summation


def larsen_windrose(layout_file, windrose_file):
    layout_x, layout_y = read_layout(layout_file)
    wind_direction, wind_speed, wind_frequency = read_windrose(windrose_file)
    efficiency = []
    profit = []
    summation = 0.0
    nt = len(layout_y)
    P = []
    U = []

    efficiency_proportion = []

    for wind in range(len(wind_direction)):
        U0 = wind_speed[wind]  # Free stream wind speed
        angle = wind_direction[wind]
        # angle2 = - 270.0 - angle  # To read windroses where N is 0 and E is 90

        U.append(larsen_1angle(layout_x, layout_y, U0, angle, rotor_radius=40.0, hub_height=100.0, TI=0.08))
        P.append([power(u) for u in U[-1]])

        # Farm efficiency
        profit.append(sum(P[-1]))
        efficiency.append(profit[-1] * 100.0 / (float(nt) * max(P[-1])))  # same as using U0
        efficiency_proportion.append(efficiency[-1] * wind_frequency[wind] / 100.0)
        summation += efficiency_proportion[wind]

    # print profit
    # print efficiency
    # print efficiency_proportion
    # print U
    # print P

    return summation


if __name__ == '__main__':
    print jensen_windrose('coordinates.dat', 'windrose.dat')
    print ainslie_windrose('coordinates.dat', 'windrose.dat')
    print larsen_windrose('coordinates.dat', 'windrose.dat')