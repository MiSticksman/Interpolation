import numpy as np
import bisect


class NewtonInterpolation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def newton(self, x):
        newton = self.y[0]
        for i in range(1, len(self.x), 1):
            div_x = 1
            tmp = self.calc_divided_difference(i)
            for j in range(i):
                div_x *= (x - self.x[j])
            newton += tmp * div_x
        return newton

    def calc_divided_difference(self, k):
        div_dif = 0
        for i in range(k + 1):
            div_x = 1
            f = self.y[i]
            for j in range(k + 1):
                if i == j:
                    continue
                div_x *= self.x[i] - self.x[j]
            div_dif += f / div_x
        return div_dif
