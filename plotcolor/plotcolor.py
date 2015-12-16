#!/usr/bin/python
######################################################################################
#    Copyright 2015 Brecht Baeten
#    This file is part of plotcolor.
#
#    plotcolor is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    plotcolor is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with plotcolor.  If not, see <http://www.gnu.org/licenses/>.
######################################################################################

import matplotlib.pyplot as plt


basecolors = {	't1':'#3bc7b0','t2':'#39b19e',
				'g1':'#0dc872','g2':'#48bb7f',
				'b1':'#1f81b9','b2':'#2b9adb',
				'p1':'#a66fdb','p2':'#c097cf',
				'd1':'#253b4d','d2':'#39566f',
				'y1':'#f3cd3f','y2':'#f6af3f',
				'o1':'#e87f1d','o2':'#dd772f',
				'r1':'#c23b24','r2':'#ed7262',
				'l1':'#7e8c8d','l2':'#9cacad' }
basecycle = ['d1','b1','r1','g1','y1','t1','o1','p1','l1','d2','b2','r2','g2','y2','t2','o2','p2','l2']

class Color(object):
	def __init__(self,colors=basecolors,cycle=basecycle):
		self.colors = colors
		self.cycle = cycle
		self.currentindex = 0
		
		self.set_default_cycle()
	
	def set_default_cycle(self):
		"""
		set the default axes color cycle
		"""
		plt.rc('axes',color_cycle=[self.colors[c] for c in self.cycle])
	
	def next(self):
		"""
		get the next color in the cycle
		"""
		c = self.colors[self.cycle[self.currentindex]]
		self.currentindex += 1
		if self.currentindex >= len(self.cycle):
			self.currentindex = 0
			
		return c
		
	def reset_index(self):
		self.currentindex = 0
		
	def __getitem__(self,key):
		if isinstance(key,int):
			self.currentindex = key+1
			return self.colors[self.cycle[key]]
		else:
			self.currentindex = self.cycle.index(key)+1
			return self.colors[key]


# definition of the colors
#basic = {'g':'#2ecc71',
#	     'b':'#3498db',
#		 'p':'#9b59b6',
#		 'd':'#6c7a89',
#		 'y':'#f2ca27',
#		 'o':'#e67e22',
#		 'r':'#e74c3c'}


		  



