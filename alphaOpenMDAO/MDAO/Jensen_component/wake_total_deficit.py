from math import sqrt

def total_wind_speed(u_ij, U_inf):

    sum_squares = 0.0

    for tur in range(len(u_ij)):
        sum_squares += u_ij[tur] ** 2.0

    total_deficit = sqrt(sum_squares)

    return U_inf * (1.0 - total_deficit)

if __name__ == '__main__':
    pass