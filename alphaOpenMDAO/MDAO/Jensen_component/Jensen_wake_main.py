from Jensen_component.wake_CT import ct_poly as ct
from Jensen_component.wake_layout_order import order_layout
from Jensen_component.wake_total_deficit import total_wind_speed
from Jensen_component.wake_turbines_behind_jensen import turbines_in_wakes_jensen
from Jensen_component.wake_deficit_Jensen import deficit_jensen


def jensen(farm, angle, k, r0, u_inf):

    indices, layout_ordered_x, layout_ordered_y = order_layout(farm, angle)
    print(indices)
    print(layout_ordered_x)
    print(layout_ordered_y)
    u_ij = [[] for _ in range(len(layout_ordered_x))]
    wind_speed = []
    CT = []

    for num in range(len(layout_ordered_x)):

        wind_speed.append(total_wind_speed(u_ij[num], u_inf))
        CT.append(ct(wind_speed[num]))
        downstream = turbines_in_wakes_jensen(indices, layout_ordered_x, layout_ordered_y, layout_ordered_x[num], layout_ordered_y[num], angle, r0, k)
        deficits = deficit_jensen(downstream, CT[num], k, r0)

        for i in range(0, len(deficits)):
            u_ij[deficits[i][1]].append(deficits[i][0])

    return wind_speed, layout_ordered_x, layout_ordered_y

if __name__ == '__main__':
    a, x, y = (jensen('coordinates.dat', 90.0, 0.04, 40.0, 8.5))
    for i in range(len(a)):
        print(x[i], y[i], a[i])
