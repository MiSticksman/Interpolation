import numpy as np
import bisect


class LagrangeInterpolation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def lagrange(self, x):
        lagrange = 0
        for i in range(len(self.y)):
            basics_pol = 1
            for j in range(len(self.x)):
                if j != i:
                    basics_pol *= (x - self.x[j]) / (self.x[i] - self.x[j])
            lagrange += basics_pol * self.y[i]
        return lagrange



