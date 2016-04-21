#!/usr/bin/python
######################################################################################
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
######################################################################################

import matplotlib.pyplot as plt

def zoom_axis(fig,ax,zoom_x,zoom_y,axis_x,axis_y,box=True,box_color='k',box_alpha=0.8,connect=True,connect_color='k',connect_alpha=0.3,spacing_zoom=2,spacing_axis=20):
    """"
    Creates a new axis which zooms in on a part of a given axis
    
    Arguments:
    fig: 		matplotlib figure
	ax: 		matplotlib axis
	zoom_x:		list, specifying the zooming horizontal area
	zoom_y:		list, specifying the zooming vertical area
	axis_x:		list, specifying the new axis horizontal location in data coordinates
	axis_y:		list, specifying the new axis vertical location in data coordinates
	
	Returns:
	ax1: 		a new axis
	
	Example:
	
    """"
	
    plt.tight_layout()
    ax1_p0 = (ax.transData + fig.transFigure.inverted()).transform_point((axis_x[0],axis_y[0]))
    ax1_p1 = (ax.transData + fig.transFigure.inverted()).transform_point((axis_x[1],axis_y[1]))

    ax1 = plt.axes([ax1_p0[0],ax1_p0[1],ax1_p1[0]-ax1_p0[0],ax1_p1[1]-ax1_p0[1]])
    
    ax1.set_xlim(zoom_x)
    ax1.set_ylim(zoom_y)
    
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)
    
	
    if box:
        ax.plot([zoom_x[0],zoom_x[1],zoom_x[1],zoom_x[0],zoom_x[0]],[zoom_y[0],zoom_y[0],zoom_y[1],zoom_y[1],zoom_y[0]],color=box_color,alpha=box_alpha)
    
    if connect:
        # estimate the width of the ticks
        spacing_zoom = (ax.transData.inverted()).transform_point((spacing_zoom,0))[0]-(ax.transData.inverted()).transform_point((0,0))[0]
        spacing_axis = (ax.transData.inverted()).transform_point((spacing_axis,0))[0]-(ax.transData.inverted()).transform_point((0,0))[0]

        if zoom_x[1] < axis_x[0]:
            # the zoom box is on the left
            x_connect = [zoom_x[1] + spacing_zoom , axis_x[0] - spacing_axis]
            y_connect_bot = np.interp(x_connect,[zoom_x[1],axis_x[0]],[zoom_y[0],axis_y[0]])
            y_connect_top = np.interp(x_connect,[zoom_x[1],axis_x[0]],[zoom_y[1],axis_y[1]])

        else:
            # the zoom box is on the right
            # the zoom box is on the left
            x_connect = [axis_x[1] + 0.5*spacing_axis , zoom_x[0] - spacing_zoom]
            y_connect_bot = np.interp(x_connect,[axis_x[1],zoom_x[0]],[axis_y[0],zoom_y[0]])
            y_connect_top = np.interp(x_connect,[axis_x[1],zoom_x[0]],[axis_y[1],zoom_y[1]])
            
        ax.plot(x_connect,y_connect_bot,color=connect_color,alpha=connect_alpha)
        ax.plot(x_connect,y_connect_top,color=connect_color,alpha=connect_alpha)
    
    return ax1

