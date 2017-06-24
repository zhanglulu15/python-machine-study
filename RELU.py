import math
import matplotlib as plt


def sigmoid(x, derivate=False):
    if derivate:
        return sigmoid(x) * (1 - sigmoid(x))
    return 1.0 / (1 + math.exp(-x))
print(sigmoid(8))


def relu(x):
    if x > 0:
        return x
    else:
        return 0
print(relu(8))
