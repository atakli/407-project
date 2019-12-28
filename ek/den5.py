import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 6*np.pi, 100)
# y = np.sin(x)

# plt.ion()		# You probably won't need this if you're embedding things in a tkinter plot...

# fig, ax = plt.subplots()
# line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

# for phase in np.linspace(0, 10*np.pi, 500):
    # line1.set_ydata(np.sin(x + phase))
    # line1.set_xdata(x + 1)
    # fig.canvas.draw()
    # fig.canvas.flush_events()
a = np.zeros(10)
d = np.zeros(10)
fig, ax = plt.subplots()
ax.set_xlim(0,5)
ax.plot([],[],'ro')

plt.show()