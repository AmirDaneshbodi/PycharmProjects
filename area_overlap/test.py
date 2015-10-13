from math import sqrt, log, tan, cos
from numpy import deg2rad, array

def distance_to_front(x, y, theta, r):
    theta = deg2rad(theta)
    return abs(x + tan(theta) * y - r / cos(theta)) / sqrt(1.0 + tan(theta) ** 2.0)

if __name__ == '__main__':
    print distance_to_front(2, 5, 0, 100)
    a = array([[1,6],[3,5],[5,4]])
    print a[:,1]