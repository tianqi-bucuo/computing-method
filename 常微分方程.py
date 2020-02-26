import numpy as np
import matplotlib.pyplot as plt
import math
import mpl_toolkits.axisartist as axisartist


def f(x, y):
    return -y-x*y*y


def Euler():
    x_list = list()
    y_list = list()
    x_list.append(0)
    y_list.append(1)
    h = float(input('步长:'))
    while x_list[-1] < 2:
        x_list.append(x_list[-1]+h)
        y_list.append(y_list[-1]+h*f(x_list[-2], y_list[-1]))
    for x in x_list:
        print(x)
    for y in y_list:
        print(y)
    show1(x_list, y_list)


def Improved_Euler():
    x_list = list()
    y_list = list()
    x_list.append(0)
    y_list.append(1)
    h = float(input('步长:'))
    while x_list[-1] < 2:
        x_list.append(x_list[-1] + h)
        y_p = y_list[-1] + h * f(x_list[-1], y_list[-1])
        y_c = y_list[-1] + h * f(x_list[-2], y_p)
        y_list.append((y_p+y_c)/2)
    for x in x_list:
        print(x)
    for y in y_list:
        print(y)
    show2(x_list, y_list)


def Runge_Kutta():
    x_list = list()
    y_list = list()
    x_list.append(0)
    y_list.append(1)
    h = float(input('步长:'))
    while x_list[-1] < 2:
        x_list.append(x_list[-1] + h)
        k1 = f(x_list[-2], y_list[-1])
        k2 = f(x_list[-2]+h/2, y_list[-1]+h*k1/2)
        k3 = f(x_list[-2]+h/2, y_list[-1]+h*k2/2)
        k4 = f(x_list[-1], y_list[-1]+h*k3)
        y_list.append(y_list[-1]+h*(k1+2*k2+2*k3+k4)/6)
    for x in x_list:
        print(x)
    for y in y_list:
        print(y)
    show3(x_list, y_list)


def show1(x_list1, y_list1):
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
    x_list2 = np.arange(0, 2.1, 0.1)
    y_list2 = 1/(2*math.e**x_list2-x_list2-1)
    plt.plot(x_list1, y_list1, 'r', x_list2, y_list2, 'b')
    plt.legend(['Euler', 'Exact'], loc='best')
    for x in np.arange(0.125, 2.125, 0.125):
        plt.vlines(x, 0, 1/(2*math.e**x-x-1), colors='r', linestyles='dashed')
    plt.show()


def show2(x_list1, y_list1):
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
    x_list2 = np.arange(0, 2.1, 0.1)
    y_list2 = 1/(2*math.e**x_list2-x_list2-1)
    plt.plot(x_list1, y_list1, 'r', x_list2, y_list2, 'b')
    plt.legend(['Improved_Euler', 'Exact'], loc='best')
    for x in np.arange(0.125, 2.125, 0.125):
        plt.vlines(x, 0, 1/(2*math.e**x-x-1), colors='r', linestyles='dashed')
    plt.show()


def show3(x_list1, y_list1):
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
    x_list2 = np.arange(0, 2.1, 0.1)
    y_list2 = 1/(2*math.e**x_list2-x_list2-1)
    plt.plot(x_list1, y_list1, 'r', x_list2, y_list2, 'b')
    plt.legend(['Runge_Kutta', 'Exact'], loc='best')
    for x in np.arange(0.125, 2.125, 0.125):
        plt.vlines(x, 0, 1/(2*math.e**x-x-1), colors='r', linestyles='dashed')
    plt.show()


if __name__ == '__main__':
    Euler()
    Improved_Euler()
    Runge_Kutta()