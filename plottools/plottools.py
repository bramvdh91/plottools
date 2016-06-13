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
import numpy as np

def set_publication_rc():
    # figure
    plt.rc('figure', autolayout=True)
    plt.rc('savefig', format='pdf', dpi=150, bbox='tight', pad_inches=0.01)
    # font
    plt.rc('font', family='serif', serif=['computer modern roman'], size=6)
    # axes
    plt.rc('axes', linewidth=0.4, labelsize=8)
    plt.rc('axes.formatter', useoffset=False)
    # legend
    plt.rc('legend', fontsize=8, frameon=True)
    # lines
    plt.rc('lines', linewidth=0.8,markersize=4)
    # text
    plt.rc('text', usetex=True)
    # ticks
    plt.rc('xtick.major', size=3, width=0.3, pad=3)
    plt.rc('ytick.major', size=3, width=0.3, pad=3)
    plt.rc('xtick.minor', size=2, width=0.3, pad=3)
    plt.rc('ytick.minor', size=2, width=0.3, pad=3)
    
    
def zoom_axes(fig,ax,zoom_x,zoom_y,axes_x,axes_y,box=True,box_color='k',box_alpha=0.8,connect=True,connect_color='k',connect_alpha=0.3,spacing_zoom=2,spacing_axes=20):
    """
    Creates a new axes which zooms in on a part of a given axes

    Arguments:
    fig:         matplotlib figure
    ax:         matplotlib axes
    zoom_x:        list, specifying the zooming horizontal area
    zoom_y:        list, specifying the zooming vertical area
    axes_x:        list, specifying the new axes horizontal location in data coordinates
    axes_y:        list, specifying the new axes vertical location in data coordinates

    Returns:
    ax1:         a new axes

    Example:

    """

    plt.tight_layout()
    ax1_p0 = (ax.transData + fig.transFigure.inverted()).transform_point((axes_x[0],axes_y[0]))
    ax1_p1 = (ax.transData + fig.transFigure.inverted()).transform_point((axes_x[1],axes_y[1]))

    ax1 = plt.axes([ax1_p0[0],ax1_p0[1],ax1_p1[0]-ax1_p0[0],ax1_p1[1]-ax1_p0[1]])

    ax1.set_xlim(zoom_x)
    ax1.set_ylim(zoom_y)

    plt.xticks(fontsize=4)
    plt.yticks(fontsize=4)
    ax1.tick_params(axis='x', pad=3)
    ax1.tick_params(axis='y', pad=2)

    if box:
        ax.plot([zoom_x[0],zoom_x[1],zoom_x[1],zoom_x[0],zoom_x[0]],[zoom_y[0],zoom_y[0],zoom_y[1],zoom_y[1],zoom_y[0]],color=box_color,alpha=box_alpha,linewidth=0.4)

    if connect:
        # estimate the width of the ticks
        spacing_zoom = (ax.transData.inverted()).transform_point((spacing_zoom,0))[0]-(ax.transData.inverted()).transform_point((0,0))[0]
        spacing_axes = (ax.transData.inverted()).transform_point((spacing_axes,0))[0]-(ax.transData.inverted()).transform_point((0,0))[0]
        
        if zoom_x[1] < axes_x[0]:
            # the zoom box is on the left
            x_connect_bot = [zoom_x[1] + spacing_zoom , axes_x[0] - 0.3*spacing_axes]
            x_connect_top = [zoom_x[1] + spacing_zoom , axes_x[0] - 0.3*spacing_axes]
            y_connect_bot = np.interp(x_connect_bot,[zoom_x[1],axes_x[0]],[zoom_y[0],axes_y[0]])
            y_connect_top = np.interp(x_connect_top,[zoom_x[1],axes_x[0]],[zoom_y[1],axes_y[1]])
            
            if y_connect_bot[1] > axes_y[0]:
                x_connect_bot = [zoom_x[1] + spacing_zoom , axes_x[0] - spacing_axes]
                y_connect_bot = np.interp(x_connect_bot,[zoom_x[1],axes_x[0]],[zoom_y[0],axes_y[0]])
            
            if y_connect_top[1] < axes_y[1]:
                x_connect_top = [zoom_x[1] + spacing_zoom , axes_x[0] - spacing_axes]
                y_connect_top = np.interp(x_connect_top,[zoom_x[1],axes_x[0]],[zoom_y[1],axes_y[1]])
                
        else:
            # the zoom box is on the right
            # the zoom box is on the left
            x_connect_bot = [axes_x[1] + 0.3*spacing_axes , zoom_x[0] - spacing_zoom]
            x_connect_top = [axes_x[1] + 0.3*spacing_axes , zoom_x[0] - spacing_zoom]
            y_connect_bot = np.interp(x_connect_bot,[axes_x[1],zoom_x[0]],[axes_y[0],zoom_y[0]])
            y_connect_top = np.interp(x_connect_top,[axes_x[1],zoom_x[0]],[axes_y[1],zoom_y[1]])
            
        ax.plot(x_connect_bot,y_connect_bot,color=connect_color,alpha=connect_alpha,linewidth=0.4)
        ax.plot(x_connect_top,y_connect_top,color=connect_color,alpha=connect_alpha,linewidth=0.4)

    return ax1

