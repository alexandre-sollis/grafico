import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
fig.patch.set_facecolor('black')
ax = plt.axes(xlim = (-1,4), ylim = (-1,3))
ax.patch.set_facecolor('black')
line, = ax.plot([], [], lw = 1)


def init():
    line.set_data([],[])
    return line,

def animate(i):
    x = np.linspace(-3,6,500)
    y = 0.01*i*(x-1)*(x-2)
    line.set_data(x,y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func = init, 
                                frames = 200, interval = 20, blit = True)
plt.show()
