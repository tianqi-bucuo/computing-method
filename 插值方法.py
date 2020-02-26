from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import random


def NewTon(x, point_x, point_y):
    d = []
    n = len(point_x)
    for i in range(n):
        d.append(point_y[i])
    for k in range(1, n):
        for j in range(n-1, k-1, -1):
            d[j] = (d[j] - d[j-1])/(point_x[j]-point_x[j-k])

    p = d[n - 1]
    for i in range(n-2, -1, -1):
        p = p*(x-point_x[i])+d[i]
    return p


def lagrange(x, point_x, point_y):
    s = 0
    count = len(point_x)
    for i in range(count):
        p = 1
        for j in range(count):
            if i != j:
                p = p*(x-point_x[j])/(point_x[i]-point_x[j])
        s = s + point_y[i]*p
    return s


def main():
    # point = int(input('输入点的个数:'))
    point_x = [-5, -3, 0, 2, 5]
    point_y = [-4, -1, 10, -9, 8]
    # for i in range(point):
    #     point_x.append(random.uniform(-5,5))
    #     point_y.append(random.uniform(-10,10))
    point_x = np.array(point_x)
    point_y = np.array(point_y)

    x_list1 = []
    y_list1 = []
    for x in point_x:
        x_list1.append(x)
    for i in range(500):
        x_list1.append(random.uniform(-5, 5))
    x_list1.sort()   # 给存放x坐标的列表排序
    for x in x_list1:
        y_list1.append(NewTon(x, point_x, point_y))

    x_list2 = []
    y_list2 = []
    for x in point_x:
        x_list2.append(x)
    for i in range(500):
        x_list2.append(random.uniform(-5, 5))
    x_list2.sort()  # 给存放x坐标的列表排序
    for x in x_list2:
        y_list2.append(NewTon(x, point_x, point_y))

    x_list3 = []
    for x in point_x:
        x_list3.append(x)
    for i in range(500):
        x_list3.append(random.uniform(point_x.min(), point_x.max()))
    x_list3.sort()  # 给存放x坐标的列表排序
    # plt.scatter(point_x, point_y)
    f = interp1d(point_x, point_y, kind='cubic')  # 编辑插值函数格式
    y_list3 = f(x_list3)

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
    plt.plot(x_list1, y_list1, 'g', x_list2, y_list2, 'b', x_list3, y_list3, 'y', point_x, point_y, 'or')
    plt.legend(['NewTon', 'lagrange', 'Spline', 'point'], loc='best')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == '__main__':
    main()