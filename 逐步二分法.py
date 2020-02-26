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


def func(a, b, e):
    h = b - a
    T = list()
    T.append((f(a)+f(b))*h/2)
    s = 0
    x = a + h/2
    while x < b:
        s = s + f(x)
        x = x + h
    T.append((T[-1]+h*s)/2)

    while abs(T[-1]-T[-2]) >= e:
        h = h/2
        s = 0
        x = a + h/2
        s = s + f(x)
        x = x + h
        while x < b:
            s = s + f(x)
            x = x + h
        T.append((T[-1] + h * s) / 2)
    print(h)
    return T[-1]


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
    plt.text(1.8, 1, 'The solution of Step 2 Distribution:', fontsize=12)
    plt.text(2.6, 0.8, res, fontsize=12)

    for x in np.arange(0.05, 6, 0.05):
        plt.vlines(x, 0, sin(x) / x, colors='r', linestyles='dashed')
    # for x in np.arange(0.02, 0.25, 0.03):
    #     plt.vlines(x, 0, sin(x)/x, colors='r', linestyles='dashed')
    # for x in np.arange(0.25, 1.9, 0.05):
    #     plt.vlines(x, 0, sin(x) / x, colors='r', linestyles='dashed')
    # for x in np.arange(2.3, 6, 0.05):
    #     plt.vlines(x, 0, sin(x) / x, colors='r', linestyles='dashed')
    plt.vlines(2.05, 0, sin(2.05) / 2.05, colors='r', linestyles='dashed')
    plt.show()


if __name__ == '__main__':
    res = func(0, 6, 0.0001)
    show(res)