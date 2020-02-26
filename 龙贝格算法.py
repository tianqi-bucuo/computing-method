from sympy import *
import math
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist


def f(x):
    if x == 0:
        x = Symbol('x')
        return limit(sin(x)/x, x, 0)
    else:
        return float(math.sin(x)/x)


def lon(a, b, e):
    T_list = []
    S_list = []
    C_list = []
    R_list = []
    h = b-a
    T_list.append((h * f(a) + f(b)) / 2)
    count = 0
    while count < 4:
        s = 0
        x = a + h / 2
        s = s + f(x)
        x = x + h
        while x < b:
            s = s + f(x)
            x = x + h
        T_list.append(T_list[-1] / 2 + h * s / 2)
        h = h/2
        count = count+1

    for i in range(4):
        S_list.append((4*T_list[i+1]-T_list[i])/(4-1))
    for i in range(3):
        C_list.append((4*4*S_list[i+1]-S_list[i])/(4*4-1))
    for i in range(2):
        R_list.append((4*4*4*C_list[i+1]-C_list[i])/(4*4*4-1))

    while (abs(R_list[-1]-R_list[-2])) >= e:
        s = 0
        x = a + h / 2
        s = s + f(x)
        x = x + h
        while x < b:
            s = s + f(x)
            x = x + h
        T_list.append(T_list[-1] / 2 + h * s / 2)
        h = h / 2
        S_list.append((4*T_list[-1]-T_list[-2])/(4-1))
        C_list.append((4 * 4 * S_list[-1] - S_list[-2]) / (4 * 4 - 1))
        R_list.append((4 * 4 * 4 * C_list[-1] - C_list[-2]) / (4 * 4 * 4 - 1))
    print('T:')
    for t in T_list:
        print(t)
    print('S:')
    for s in S_list:
        print(s)
    print('C:')
    for c in C_list:
        print(c)
    print('R:'+'\n')
    for r in R_list:
        print(r)
    print('h:', h)
    return R_list[-1]


def show(res):
    # 创建画布
    fig = plt.figure()
    # 使用axisartist.Subplot方法创建一个绘图区对象ax
    ax = axisartist.Subplot(fig, 111)
    # 将绘图区对象添加到画布中
    fig.add_axes(ax)
    ax.axis[:].set_visible(False)
    ax.axis["x"] = ax.new_floating_axis(0, 0)
    ax.axis["x"].set_axisline_style("->", size=1.0)
    ax.axis["y"] = ax.new_floating_axis(1, 0)
    ax.axis["y"].set_axisline_style("-|>", size=1.0)
    ax.axis["x"].set_axis_direction("top")
    ax.axis["y"].set_axis_direction("right")
    x_list = np.arange(10**-10, 6, 10**-4)
    y_list = np.sin(x_list)/x_list
    plt.plot(x_list, y_list)
    # plt.legend()
    plt.text(1.8, 1, 'The solution of longberg algorithm:', fontsize=15)
    plt.text(2.6, 0.8, res, fontsize=15)

    for x in np.arange(0.1875, 6, 0.1875):
        plt.vlines(x, 0, sin(x)/x, colors='r', linestyles='dashed')
    plt.show()


if __name__ == '__main__':
    res = lon(0, 6, 0.000001)
    show(res)