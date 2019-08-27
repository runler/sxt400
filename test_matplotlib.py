import matplotlib.pyplot as plt

# 准备绘制的两个点 (1,2)  (4,8)
# 调用绘制方法 plot([x轴坐标列表],[y轴坐标列表],linewidth = 线条宽度 )
# plt.plot([1,4],[2,8])
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], linewidth=5)
# 添加X/Y轴名称、图标名称、字体大小
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.xlabel('月份', fontsize=14)
plt.ylabel('产品', fontsize=14)
plt.title('练习图标一', fontsize=24)
# 显示绘制的图
plt.show()

# 不能弹出“figure”窗口：File--->Settings--->Tools--->Python Scientific"去除右边候选框中的勾号

