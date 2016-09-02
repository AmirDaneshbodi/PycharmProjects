from math import sqrt


def deficit_jensen(downstream_list_distance, ct, k, r0):

        deficits = []

        for tur in range(len(downstream_list_distance)):

            deficits.append([
                (1.0 - sqrt(1.0 - ct)) / (1.0 + (k * downstream_list_distance[tur][0]) / r0) ** 2.0, downstream_list_distance[tur][1]])

        return deficits


if __name__ == '__main__':
    print(deficit_jensen([[560.0, 3], [1120.0, 4], [1680.0, 5], [2240.0, 6]], 0.8, 0.04, 40.0))