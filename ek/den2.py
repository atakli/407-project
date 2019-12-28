import matplotlib.pyplot as plt
x = np.arange(0, 2*np.pi, 0.01)
fig, ax = plt.subplots()
for i in np.arange(100):
	ax.plot(x, np.sin(x+ i/10.0))
	ax.draw()