import matplotlib.pyplot as plt
import numpy as np
import plotcolor as pc


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
plt.plot(x,np.sin(x- 0*2*np.pi/12),color=pc.color['d1'],label='d1')
plt.plot(x,np.sin(x- 2*2*np.pi/12),color=pc.color['b1'],label='b1')
plt.plot(x,np.sin(x- 4*2*np.pi/12),color=pc.color['r1'],label='r1')
plt.plot(x,np.sin(x- 6*2*np.pi/12),color=pc.color['y1'],label='y1')
plt.plot(x,np.sin(x- 8*2*np.pi/12),color=pc.color['o1'],label='o1')
plt.plot(x,np.sin(x-10*2*np.pi/12),color=pc.color['g1'],label='g1')
plt.legend()



# bar plot
pc.color.reset_index()
plt.figure()
x = np.arange(6)
cat = ['cat1','cat2','cat3','cat4','cat5']

p = []
yy = np.zeros_like(x)
for c in cat:
	y = np.random.random_integers(1,high=10,size=x.shape)
	pl = plt.bar(x, y, 0.8, bottom=yy , color=pc.color.next())
	p.append(pl[0])
	yy = yy+y
	
plt.legend(p,cat)



plt.show()