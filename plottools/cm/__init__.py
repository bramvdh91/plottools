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

import sys
import os

from hotwater import hotwater
from coldhot import coldhot


def cm2svg(colormap,filename):
	"""
	creates a svg file with the colormap defined as a gradient
	"""
	
	
	# get the colors of the colormap at the stops
	stops = [0.00,0.25,0.50,0.75,1.00]
	svg_stops = ['#{:06.0f}'.format(s*100) for s in stops]
	colors = ['#{:02x}{:02x}{:02x}'.format(int(colormap(s)[0]*255),int(colormap(s)[1]*255),int(colormap(s)[2]*255)) for s in stops]

	
	# current path
	modulepath = os.path.dirname(sys.modules[__name__].__file__)

	# open the cm_blank svg file
	blank_file = open(os.path.join(modulepath,'cm_blank.svg'), 'r') 
	contents = blank_file.read()
	blank_file.close()

	
	for s,c in zip(svg_stops,colors):
		contents = contents.replace(s,c)
	
	new_file = open(filename, 'w')
	new_file.write(contents)
	new_file.close()