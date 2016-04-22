#!/usr/bin/python
################################################################################
#    Copyright 2015 Brecht Baeten
#    This file is part of plottools.
#
#    plottools is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    plottools is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with plottools.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

import matplotlib.pyplot as plt
from cycler import cycler

################################################################################
# Color definitions
################################################################################
# colors derived from http://www.stonesc.com
basecolors = {'b': ( 57./255,106./255,177./255),
			  'o': (218./255,124./255, 48./255),
			  'g': ( 62./255,150./255, 81./255),
			  'r': (204./255, 37./255, 41./255),
			  'k': ( 83./255, 81./255, 84./255),
			  'p': (107./255, 76./255,154./255),
			  'd': (146./255, 36./255, 40./255),
			  'y': (148./255,139./255, 61./255)}

lightcolors = {'b': (114./255,147./255,203./255),
			   'o': (225./255,151./255, 76./255),
			   'g': (132./255,186./255, 91./255),
			   'r': (211./255, 94./255, 96./255),
			   'k': (128./255,133./255,133./255),
			   'p': (144./255,103./255,167./255),
			   'd': (171./255,104./255, 87./255),
			   'y': (204./255,194./255, 16./255)}

basecycle = ['b','o','g','r','k','p','d','y']	


################################################################################
# Colorscheme class 
################################################################################
class Colorscheme(object):
	def __init__(self,colors=basecolors,cycle=basecycle):
		"""
		defines a colorscheme object useful for plotting
		
		Arguments:
		colors: dict, dictionary of named colors as RGB (0-1) tupples
		cycle:  list, list with the cycle order
		
		Example:
		cs = Colorscheme({'r':(1.,0.,0.),'g':(0.,1.,0.),'b':(0.,0.,1.)},['b','g','r'])
		print( cs[0] )
		
		print( cs.next() )
		print( cs.next() )
		
		cs.reset_index()
		print( cs.next() )
		"""
		
		self.colors = colors
		self.cycle = cycle
		self.currentindex = 0

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
		"""
		resets the current color index to 0
		"""
		
		self.currentindex = 0
	
	def set_as_default(self):
		"""
		sets the colorscheme as the default color cycle in matplotlib figures
		"""
		
		plt.rc('axes',prop_cycle=cycler('color', [self.colors[c] for c in self.cycle]) )
		
	def __getitem__(self,key):
		if isinstance(key,int):
			self.currentindex = key+1
			return self.colors[self.cycle[key]]
		else:
			self.currentindex = self.cycle.index(key)+1
			return self.colors[key]

				   
			   
################################################################################
# create default color schemes
################################################################################
color = Colorscheme()
lightcolor = Colorscheme(colors=lightcolors)
