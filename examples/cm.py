import matplotlib.pyplot as plt
import numpy as np
import plottools as pt


# hot water
plt.figure()
plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto', cmap=pt.cm.hotwater)

# show plots
plt.show()