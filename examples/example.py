import matplotlib.pyplot as plt
import numpy as np
import plotcolor as pc

# sets the default color cycle
pc.color.set_default_cycle()

# line plot with thick lines
plt.figure()
x = np.linspace(0,2*np.pi,100)
n = len(pc.color.cycle)

for i in range(n):
	plt.plot(x,np.sin(x-i*2*np.pi/n),label=pc.color.cycle[i],linewidth=2)
	
plt.legend()


# some lines
plt.figure()
x = np.linspace(0,2*np.pi,100)
plt.plot(x,np.sin(x- 0*2*np.pi/12),color=pc.color['d'],label='d')
plt.plot(x,np.sin(x- 2*2*np.pi/12),color=pc.color['b'],label='b')
plt.plot(x,np.sin(x- 4*2*np.pi/12),color=pc.color['r'],label='r')
plt.plot(x,np.sin(x- 6*2*np.pi/12),color=pc.color['y'],label='y')
plt.plot(x,np.sin(x- 8*2*np.pi/12),color=pc.color['o'],label='o')
plt.plot(x,np.sin(x-10*2*np.pi/12),color=pc.color['g'],label='g')
plt.legend()



# bar plot
pc.lightcolor.reset_index()
plt.figure()
x = np.arange(6)
cat = ['cat1','cat2','cat3','cat4','cat5','cat6','cat7','cat8']

p = []
yy = np.zeros_like(x)
for c in cat:
	y = np.random.random_integers(1,high=10,size=x.shape)
	pl = plt.bar(x, y, 0.8, bottom=yy , color=pc.lightcolor.next())
	p.append(pl[0])
	yy = yy+y
	
plt.legend(p,cat)


# colormap
plt.figure()
plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto', cmap=pc.cm.hotwater)

plt.show()