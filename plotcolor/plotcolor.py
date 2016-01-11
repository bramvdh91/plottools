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

from cycler import cycler
import matplotlib.pyplot as plt


# colors derived from http://www.stonesc.com
basecolors = {'b': ( 57./255,106./255,177./255),
			  'o': (218./255,124./255, 48./255),
			  'g': ( 62./255,150./255, 81./255),
			  'r': (204./255, 37./255, 41./255),
			  'k': ( 83./255, 81./255, 84./255),
			  'p': (107./255, 76./255,154./255),
			  'd': (146./255, 36./255, 40./255),
			  'y': (148./255,139./255, 61./255)}
basecycle = ['b','o','g','r','k','p','d','y']

lightcolors = {'b': (114./255,147./255,203./255),
			   'o': (225./255,151./255, 76./255),
			   'g': (132./255,186./255, 91./255),
			   'r': (211./255, 94./255, 96./255),
			   'k': (128./255,133./255,133./255),
			   'p': (144./255,103./255,167./255),
			   'd': (171./255,104./255, 87./255),
			   'y': (204./255,194./255, 16./255)}

class Color(object):
	def __init__(self,colors=basecolors,cycle=basecycle):
		self.colors = colors
		self.cycle = cycle
		self.currentindex = 0
	
	def set_default_cycle(self):
		"""
		set the default axes color cycle
		"""
		plt.rc('axes',prop_cycle=cycler('color', [self.colors[c] for c in self.cycle]) )

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


		  



