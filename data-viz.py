import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#from sklearn import datasets
"""
#BAR CHART
bar_width = 0.25
num_bins = 5
bar1 = np.random.randint(0, 100, num_bins)
bar2 = np.random.randint(0, 100, num_bins)
indices = np.arange(num_bins)

plt.bar(indices, bar1, bar_width, color='b', label='Prof 1')
plt.bar(indices+bar_width, bar2, bar_width, color='g', label='Prof 2')

plt.xlabel('Final grade')
plt.ylabel('Frequency')
plt.xticks(indices+bar_width, ('A', 'B', 'C', 'D', 'F'))
plt.legend()
plt.show()
"""
"""
#HISTOGRAM
mu = 0
sigma = 1
vals = mu + sigma * np.random.randn(1000)

plt.hist(vals, 50)

plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.title('Normal Distribution (sampled)')
plt.grid(True)
plt.show()
"""

"""#BOXPLOT
x = np.random.rand(100) * 100

plt.boxplot(x, vert=False)
plt.show()
"""

"""#PIE CHART
labels = ['gas', 'groceries', 'books', 'rent']
values = [100, 300, 20, 500]
explode = (0, 0, 1, 0)

plt.pie(values, labels=labels, explode=explode, radius=1, shadow=True, autopct='%f%%')
plt.show()
"""

"""#LINE PLOT
x = np.linspace(0, 10)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, 'g-', label='sine')
plt.plot(x, y2, 'b-', label='cosine')
plt.legend()
plt.grid(True)
plt.show()
"""

"""#SCATTERPLOT
iris = datasets.load_iris()
X = iris.data[:,2]
Y = iris.data[:,3]
colors = iris.target

plt.scatter(X, Y, c=colors)
plt.grid(True)
plt.show()
"""

"""#QUIVER PLOT
X, Y = np.meshgrid(np.arange(-10, 10), np.arange(-10,10))
U = -Y
V = X
plt.quiver(X,Y,U,V)
#plt.streamplot(X,Y,U,V)
"""
"""
#3D LINE PLOT
phi = np.linspace(-6 * np.pi, 6 * np.pi, 100)
z = np.linspace(-4, 4, 100)
x = np.sin(phi)
y = np.cos(phi)

fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot(x,y,z)
"""

#3D SURFACE PLOT
X, Y = np.meshgrid(np.arange(-100, 100), np.arange(-100,100))
Z = X ** 2 + Y ** 2

G_x, G_y = np.gradient(Z)
G = np.sqrt(G_x**2 + G_y**2)
G = G / G.max()

fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(X,Y,Z, facecolors=cm.inferno(G))


"""
x = np.linspace(0, 10)
speed_plot = plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x), '-', label='sin')
plt.ylabel('speed (m/s)')
plt.setp(speed_plot.get_xticklabels(), visible=False)
plt.grid(True)

plt.subplot(2,1,2, sharex=speed_plot)
plt.plot(x, np.cos(x), '-', label='cos')
plt.ylabel('acceleration (m/s/s)')
plt.xlabel('time (s)')
plt.grid(True)
"""

plt.show()

