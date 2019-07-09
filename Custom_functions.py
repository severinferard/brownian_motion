
import statistics
import math
from matplotlib import pyplot as plt


def My_func(positionsdata, dicdistrelativedata, dicdistorigindata):
    pass
    # return(x,y)


def quadratique(positionsdata, dicdistrelativedata, dicdistorigindata):
    y = []
    l = []
    for value in dicdistorigindata:
        l.append(value)
        squared = [i * i for i in l]
        print("squared", squared)
        average = statistics.mean(squared)
        print("average", average)
        quadratique = math.sqrt(average)
        print("quadratique", quadratique)
        y.append(quadratique)

    D = 0.0000456
    x = range(len(y))

    plt.figure()
    plt.plot(x, y, 'o')
    plt.show()
    return(x, y)


def quadratique2(positionsdata, dicdistrelativedata, dicdistorigindata):
    y = []
    for value in range(len(dicdistorigindata)):
        membre1 = ((8.314 * 293)) / (8 * (10**23))
        membre2 = 1 / (3 * math.pi * 0.001 * 0.000005)
        y.append(membre1 * membre2 * value)

    x = range(len(y))
    plt.figure()
    plt.plot(x, y, 'o')
    plt.show()
    return(x, y)


# test(1, 1, 1)


# print(quadratique2(1, 1, [0.0, 4.031128874149275, 5.656854249492381, 8.54400374531753, 7.615773105863909, 9.848857801796104, 11.313708498984761, 12.806248474865697, 12.529964086141668, 7.810249675906654, 11.40175425099138, 11.661903789690601, 16.401219466856727, 18.439088914585774, 16.278820596099706, 18.601075237738275, 13.45362404707371, 14.142135623730951, 16.97056274847714, 17.029386365926403, 19.209372712298546, 16.55294535724685, 16.278820596099706, 15.0, 14.142135623730951, 19.1049731745428, 18.601075237738275, 20.0, 19.849433241279208, 23.430749027719962, 19.849433241279208, 22.02271554554524, 22.360679774997898]))
