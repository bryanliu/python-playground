import matplotlib.pyplot as plt

# example 1: 最简单的例子，横坐标的点，纵坐标的点
# plt.plot([1, 3, 5], [4, 8, 10])
# plt.show()

# example 2: -pi 到 pi 的一条曲线
# x = np.linspace(-np.pi, np.pi, 100)
# plt.plot(x, np.sin(x))
# plt.show()

# example 3: 创建多条曲线
# x = np.linspace(-np.pi, np.pi, 100)
# # plt.figure(1, dpi=50)
# for i in range(1, 5):
#     plt.plot(x, np.sin(x / i))
# plt.show()

# example 4: 直方图，统计个数
# plt.hist([1, 1, 3, 4, 5, 5, 5, 6, 7, 7, 7, 7, 8, 3])
# plt.show()

# example 5: 从文件读取数据绘图
import pandas as pd

# iris = pd.read_csv("./iris.training.csv")
# #print(iris.head()) # head() 读取 5行
# iris.plot(kind="scatter", x="120", y="4")
# plt.show()

# example 6: 使用 seaborn 绘图
import seaborn as sns

# iris = pd.read_csv("./iris.training.csv")
# #设置样式
# sns.set(style="white", color_codes=True)
# # 设置图片为散点图
# sns.jointplot(x="120", y="4", data=iris, size=5)
# # 绘制一个小曲线图
# sns.distplot(iris['120'])
# plt.show()

iris = pd.read_csv("./iris.training.csv")
# 设置样式
sns.set(style="white", color_codes=True)
# 按照字段virginica分类
sns.FacetGrid(iris, hue="virginica", size=5).map(plt.scatter, "120", "4")
plt.show()
