import numpy as np
import scipy.io as scio

from matplotlib import pyplot as plt
from matplotlib import rcParams


def plt_time_domain(arr, fs=1600, ylabel='Amp(mg)', title='原始数据时域图', img_save_path=None, x_vline=None, y_hline=None):
    """
    :fun: 绘制时域图模板
    :param arr: 输入一维数组数据
    :param fs: 采样频率
    :param ylabel: y轴标签
    :param title: 图标题
    :return: None
    """
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 显示负号
    font = {'family': 'Times New Roman', 'size': '20', 'color': '0.5', 'weight': 'bold'}

    plt.figure(figsize=(12, 4))
    length = len(arr)
    t = np.linspace(0, length / fs, length)
    plt.plot(t, arr, c='g')
    plt.xlabel('t(s)')
    plt.ylabel(ylabel)
    plt.title(title)
    if x_vline:
        plt.vlines(x=x_vline, ymin=np.min(arr), ymax=np.max(arr), linestyle='--', colors='r')
    if y_hline:
        plt.hlines(y=0.2, xmin=np.min(t), xmax=np.max(t), linestyle=':', colors='y')
    # ===保存图片====#
    if img_save_path:
        plt.savefig(img_save_path, dpi=500, bbox_inches='tight')
    plt.show()

fs = 100  # 采样频率
f = 200    # 模拟正弦信号频率
time = 5  # 采样时长
t = np.linspace(0, time, time*fs)
data = 1*np.sin(2*np.pi*f*t) + np.random.normal(0, 0.1, time*fs)
plt_time_domain(data, fs=fs)

print("hello world")