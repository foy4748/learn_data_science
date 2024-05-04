import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Worked!
matplotlib.use(backend="TkAgg")


xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
