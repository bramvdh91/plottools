import matplotlib.pyplot as plt
import plottools as pt


pt.set_publication_rc()


# small figure, box on the left
plt.figure(figsize=(8/2.54,6/2.54))
plt.plot([0,2],[1,2])
plt.plot([0,2],[2,1])
plt.xlabel('xlabel')
plt.ylabel('ylabel')
fig = plt.gcf()
ax = plt.gca()

ax1 = pt.zoom_axes(fig,ax,[0.1,0.3],[1.0,1.2],[1.0,1.9],[1.5,2.0])
ax1.plot([0,2],[1,2])
ax1.plot([0,2],[2,1])



# small figure, box on the right
plt.figure(figsize=(8/2.54,6/2.54))
plt.plot([0,2],[1,2])
plt.plot([0,2],[2,1])
plt.xlabel('xlabel')
plt.ylabel('ylabel')
fig = plt.gcf()
ax = plt.gca()

ax1 = pt.zoom_axes(fig,ax,[1.5,1.6],[1.7,1.8],[0.15,0.9],[1.4,1.9])
plt.plot([0,2],[1,2])
plt.plot([0,2],[2,1])


# show plots
plt.show()