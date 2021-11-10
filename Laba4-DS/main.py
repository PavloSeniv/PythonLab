import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Task1 Create

# x = np.linspace(-3,3, 101)
# y = np.sin(x)
# z = np.cos(x)

# xnumbers = np.linspace(-3, 3, 7)
# ynumbers = np.linspace(-1, 1, 11)

# plt.plot(x, y, 'r:', x, z, 'g--') # r, g - red, green colour
# plt.xlabel("Проміжок від -3 до 3",color='blue',fontsize=14)
# plt.ylabel("Значення функції",color='blue',fontsize=14)
# plt.title("sin,cos")
# plt.xticks(xnumbers)
# plt.yticks(ynumbers)
# plt.show()

#########################################

# Task2 Create

# ex = (0.1, 0, 0,0,0)
# plt.title("Президентський рейтинг")
# labels = 'Зеленський', 'Порошенко', 'Бойко', 'Тимошенко', 'Не голосуватиму'
# plt.pie([27.4, 11.7, 9.6, 8.1, 43.2], explode=ex, autopct='%1.1f%%', labels=labels)
# plt.show()

#########################################

# Task1 coronovarus.csv

# data = pd.read_csv('coronovarus.csv', sep = ';')
# print(data)

# fig, ax = plt.subplots()
# data.plot(kind='bar', x="Date", y="New cases", ax = ax)

# ax.set(title='Коронавірус в Україні')
# plt.xticks(rotation=45)
# ax.legend().set_visible(False)
# plt.grid()
# plt.show()

#########################################

# Task2 coronovarus.csv

# data = pd.read_csv('coronovarus.csv', sep = ';')
# print(data)

# fig, ax = plt.subplots()

# column_graph = data.plot(kind='bar', x="Date",fontsize=6, y="New cases", ax = ax)

# # # set individual bar lables using above list
# # for i in ax1.patches:
# #     # get_x pulls left or right; get_height pushes up or down
# #     ax1.text(i.get_x(), i.get_height(), \
# #             str(round((i.get_height()), 2)), fontsize=8,
# #                 color='black')

# def autolabel(rects):
#   for rect in column_graph.patches:
#     height = rect.get_height()
#     ax.text(rect.get_x() + rect.get_width()/2., 0.65*height, '%d' % int(height), ha='center', va='bottom')

# plt.title("Coronavirus/Ukraine",color='blue',fontsize=14)
# plt.xlabel("Date",color='blue',fontsize=8)
# plt.ylabel("New cases",color='blue',fontsize=8)

# plt.xticks(rotation=0)
# ax.legend().set_visible(False)
# plt.grid()

# autolabel(column_graph)
# plt.show()

#########################################

# Task Create a blank shape

# fig = plt.figure()

# ax_1 = fig.add_subplot(3,1,1)
# ax_2 = fig.add_subplot(3,3,4)
# ax_3 = fig.add_subplot(3,3,6)
# ax_4 = fig.add_subplot(3,1,3)

# plt.show()

#########################################

# Task Create a surface
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = np.linspace(-6, 6, 1000)
y = np.linspace(-6, 6, 1000)

X, Y = np.meshgrid(x,y)
Z = X**3 + X*(Y**2)

fig = plt.figure()

ax = plt.axes(projection='3d')
ax.contour3D(X,Y,Z,500)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_ylabel('z')

plt.show()

#########################################