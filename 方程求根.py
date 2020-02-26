import math
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist


def f(x):
    return x-2*math.sin(x)


def f1(x):
    return 1-2*math.cos(x)


def dichotomy(e):
    a = 1
    b = 3
    while abs(a-b) > e:
        if f(a) * f(b) > 0:
            print('根不在输入区间内')
            break
        c = (a + b) / 2
        if f(a)*f(c) > 0:
            a = c
        else:
            b = c

    print((a+b)/2)
    show1((a+b)/2)


def Newton(i, e):
    x_list = list()
    x_list.append(i)
    x_list.append(x_list[-1] - f(x_list[-1]) / f1(x_list[-1]))
    while (x_list[-1]-x_list[-2]) > e:
        x_list.append(x_list[-1]-f(x_list[-1])/f1(x_list[-1]))
    print(x_list[-1])
    show2(x_list[-1])


def Chord_cut(x0, x1, e):
    x_list = list()
    x_list.append(x0)
    x_list.append(x1)
    while (x_list[-1] - x_list[-2]) > e:
        x_list.append(x_list[-1] - f(x_list[-1]) * (x_list[-1] - x_list[0]) / (f(x_list[-1]) - f(x_list[0])))
    print(x_list[-1])
    show3(x_list[-1])


def show1(res):
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
    x_list = np.arange(0, 4, 0.1)
    x_list = list(x_list)
    y_list = list()
    for x in x_list:
        y_list.append(f(x))
    plt.plot(x_list, y_list, 'b')
    plt.vlines(1, 0, 1-2*math.sin(1), colors='r', linestyles='dashed')
    plt.vlines(3, 0, 3-2*math.sin(3), colors='r', linestyles='dashed')
    plt.text(0.2, 4, 'The solution of dichotomy', fontsize=15)
    plt.text(0.2, 3.5, res, fontsize=15)
    plt.show()


def show2(res):
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
    x_list = np.arange(0, 4, 0.1)
    x_list = list(x_list)
    y_list = list()
    for x in x_list:
        y_list.append(f(x))
    plt.plot(x_list, y_list, 'b')
    plt.vlines(1, 0, 1-2*math.sin(1), colors='r', linestyles='dashed')
    plt.vlines(3, 0, 3-2*math.sin(3), colors='r', linestyles='dashed')
    plt.text(0.2, 4, 'The solution of Newton', fontsize=15)
    plt.text(0.2, 3.5, res, fontsize=15)
    plt.show()


def show3(res):
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
    x_list = np.arange(0, 4, 0.1)
    x_list = list(x_list)
    y_list = list()
    for x in x_list:
        y_list.append(f(x))
    plt.plot(x_list, y_list, 'b')
    plt.vlines(1, 0, 1-2*math.sin(1), colors='r', linestyles='dashed')
    plt.vlines(3, 0, 3-2*math.sin(3), colors='r', linestyles='dashed')
    plt.text(0.2, 4, 'The solution of Chord_cut', fontsize=15)
    plt.text(0.2, 3.5, res, fontsize=15)
    plt.show()


if __name__ == '__main__':
    dichotomy(0.001)
    Newton(1.9, 0.0001)
    Chord_cut(1.8, 1.9, 0.0001)