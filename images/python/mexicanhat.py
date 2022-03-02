

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


r = 2.7
z = 10
a = 5
b = -4
c = 0.5

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.grid(False)

# R = np.linspace(0, r, 1000)
# U = np.linspace(0,  2*np.pi, 1000)
# X = np.outer(R, np.cos(U))
# Y = np.outer(R, np.sin(U))
# Z = a + b*(X**2 + Y**2) + c*(X**2 + Y**2)**2

r = np.linspace(0, 1.3, 1000)
p = np.linspace(0, 2*np.pi, 1000)
R, P = np.meshgrid(r, p)
Z = 0.7*((R**2 - 1)**2)
X, Y = R*np.cos(P), R*np.sin(P)


surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=True)

ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')

ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))


plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')

# Create the mesh in polar coordinates and compute corresponding Z.
# r = np.linspace(0, 1.25, 50)
# p = np.linspace(0, 2*np.pi, 50)
# R, P = np.meshgrid(r, p)
# Z = ((R**2 - 1)**2)

# Express the mesh in the cartesian system.
# X, Y = R*np.cos(P), R*np.sin(P)

# Plot the surface.
# ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)

# Tweak the limits and add latex math labels.
# ax.set_zlim(0, 1)
# ax.set_xlabel(r'$\phi_\mathrm{real}$')
# ax.set_ylabel(r'$\phi_\mathrm{im}$')
# ax.set_zlabel(r'$V(\phi)$')

# plt.show()
