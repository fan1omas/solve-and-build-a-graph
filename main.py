from matplotlib import pyplot as plt
import numpy as np
from math import *

def solve(func, target_y=0, start=0, stop=10, step=0.5):
    # y = x
    x_coords = []
    y_coords = []
    last_value = -1

    ranges = np.arange(start, stop, step)

    for x in ranges:
        x = float(x)
        y_val = func(x)
        x_coords.append(x)
        y_coords.append(y_val)

        if len(y_coords) >= 2:
            prev_y = y_coords[-2]
            curr_y = y_coords[-1]

            if (prev_y <= target_y <= curr_y) or (prev_y >= target_y >= curr_y):
                return x_coords, y_coords
def function(x):
    return x**2

a = solve(function, 4, 0, 100, 0.001)

if a is None:
    print('Нет решения или решение не найдено!')
else:
    x, y = a
    answer = [x[-2], x[-1]]

    plt.ylabel('Y')
    plt.xlabel('X')
    plt.title('Решение уравнения')

    plt.plot(x, y)
    plt.scatter(answer[0], y[x.index(answer[0])], s=50, c='red')

    c_ticks = [float(i) for i in list(plt.xticks()[0])]
    n_ticks = c_ticks + answer

    plt.xticks(n_ticks)

    print(f'Функция пересекла y между точками {answer[0]} и {answer[1]}')
    plt.show()
