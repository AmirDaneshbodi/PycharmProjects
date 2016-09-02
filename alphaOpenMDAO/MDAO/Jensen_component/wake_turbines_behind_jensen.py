from math import radians, tan, sin, sqrt, cos


def turbines_in_wakes_jensen(indices, layout_ordered_x, layout_ordered_y, upstream_x, upstream_y, wind_angle, r0, k):
    in_wake = []

    xt = upstream_x
    yt = upstream_y

    for tur in range(len(layout_ordered_x)):

        xw = layout_ordered_x[tur]
        yw = layout_ordered_y[tur]
        alpha = radians(- wind_angle - 270.0)

        if (xw - xt) * cos(alpha) + (yw - yt) * sin(alpha) < 0.0:

            X_int = (xw + tan(alpha) * yw + tan(alpha) * (tan(alpha) * xt - yt)) / (tan(alpha) ** 2.0 + 1.0)
            Y_int = (- tan(alpha) * (- xw - tan(alpha) * yw) - tan(alpha) * xt + yt) / (tan(alpha) ** 2.0 + 1.0)
            distance_to_centre = abs(- tan(alpha) * xw + yw + tan(alpha) * xt - yt) / sqrt(1.0 + tan(alpha) ** 2.0)
            distance_to_turbine = sqrt((X_int - xt) ** 2.0 + (Y_int - yt) ** 2.0)
            radius = r0 + k * distance_to_turbine

            if abs(radius) >= abs(distance_to_centre):
                in_wake.append([distance_to_turbine, indices[tur]])

    return in_wake

if __name__ == '__main__':
    from .wake_layout_order import order_layout
    indices, layout_ordered_x, layout_ordered_y = order_layout('coordinates.dat', 270.0)
    print(turbines_in_wakes_jensen(indices, layout_ordered_x, layout_ordered_y, 425094.0, 6151447.0, 270.0, 40.0, 0.04))