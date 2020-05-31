__author__ = 'JudePark'
__email__ = 'judepark@kookmin.ac.kr'


import numpy as np


def pure_AND(x1, x2):
    """
    파이썬으로만 구현함.
    """
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2

    return 0 if tmp <= theta else 1

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    tmp = np.sum(w * x) + b

    return 0 if tmp <= 0 else 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    tmp = np.sum(w * x) + b

    return 0 if tmp <= 0 else 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2

    tmp = np.sum(w * x) + b

    return 0 if tmp <= 0 else 1

if __name__ == '__main__':
    gates = [[0, 0], [1, 0], [0, 1], [1, 1]]

    print('AND Gates')
    for gate in gates:
        print(AND(gate[0], gate[1]))

    print('NAND Gates')
    for gate in gates:
        print(NAND(gate[0], gate[1]))

    print('OR Gates')
    for gate in gates:
        print(OR(gate[0], gate[1]))