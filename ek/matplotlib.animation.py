# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = plt.plot([], [], 'ro')

# def init():
	# ax.set_xlim(0, 2*np.pi)
	# ax.set_ylim(-5, 5)
	# return ln,

# def update(frame):
	# xdata.append(frame)
	# ydata.append(np.sin(frame))
	# ln.set_data(xdata, ydata)
	# return ln,

# ani = FuncAnimation(fig, update, frames=np.random.randint(-5, 5, 20)[10:],
					# init_func=init, blit=True)
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = plt.plot([], [], 'ro')

# def init():
	# ax.set_xlim(0, 2*np.pi)
	# ax.set_ylim(-1, 1)
	# return ln,

# def update(frame):
	# xdata.append(frame)
	# ydata.append(np.sin(frame))
	# ln.set_data(xdata, ydata)
	# return ln,

# ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
					# init_func=init, blit=True)
# plt.show()
"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
# x = np.arange(10)
line, = ax.plot(x, np.sin(x))
# line, = ax.plot(x, np.random.randint(-5, 5, 20)[10:])


def animate(i):
	line.set_ydata(np.sin(x + i/10.0))	# update the data
	# line.set_ydata(np.random.randint(-5, 5, 20)[10:])	 # update the data
	return line,

def init():	# Init only required for blitting to give a clean slate.
	# line.set_ydata(x)#np.ma.array(x))#, mask=True))
	return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
							  interval=25, blit=True)
plt.show()
