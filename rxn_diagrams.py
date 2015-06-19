"""Rxn_diagrams.py
A script to automate drawing reaction coordinate diagrams
Doug Crandell - Indiana University 2013
"""

import sys
import math
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from matplotlib.lines import Line2D

def main(argv):
    t= 0.4
    pts = []
    count = 1
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    max_val = float("-inf")
    min_val = float("inf")
    
    #Parse list of arguments and determine the maximum and minimum values for energy scale
    for val in argv:
        if float(val) > max_val:
            max_val = float(val)
        if float(val) < min_val:
            min_val = float(val)
        pt = (count,float(val))
        count += 2
        if count == 3:
            start_pt = (-11,float(val))
            pts.insert(0,start_pt)
        pts.append(pt)
    pts.append((count+2,pts[-2][1]))
    codes = [Path.MOVETO,Path.CURVE4,Path.CURVE4,Path.CURVE4]

    #Find control points for all points that aren't end points
    for point in range(len(pts)-2):
        ctl_pts = getControlPoints(pts[point][0],pts[point][1],pts[point+1][0],pts[point+1][1],pts[point+2][0],pts[point+2][1],t)
        if point == 0:
            next_ctrl_pt = ctl_pts[1]
        if point > 0:
            verts = [pts[point],next_ctrl_pt,ctl_pts[0],pts[point+1]]
            next_ctrl_pt = ctl_pts[1]
            path = Path(verts,codes)
            patch = patches.PathPatch(path, facecolor='none', lw=2)
            ax.add_patch(patch)

    #Specify axis parameters
    ax1 = plt.axes()
    ax1.set_frame_on(False)
    ax1.get_xaxis().set_visible(False)
    xmin, xmax = ax1.get_xaxis().get_view_interval()
    ymin, ymax = ax1.get_yaxis().get_view_interval()
    ax1.arrow(0, min_val, 0, max_val+1-(min_val), head_width=0.3, head_length=0.3, fc='k', ec='k')
    plt.ylabel(r'$\Delta$E kcal mol' + r'$^-$' + r'$^1$')
    plt.tick_params(right='off',length=5,width=1)
    ax.set_xlim(-0.1, 20)
    ax.set_ylim(min_val-1, max_val+1)
    plt.show()

def getControlPoints(x0,y0,x1,y1,x2,y2,t):
    #Find control points for drawing a bezier curve
    d01 = math.sqrt(math.pow(x1-x0,2) + math.pow(y1-y0,2))
    d12 = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
    fa = t*d01/(d01+d12)
    fb = t*d12/(d01+d12)
    p1x = x1-fa*(x2-x0)
    p1y = y1-fa*(y2-y0)
    p2x = x1+fb*(x2-x0)
    p2y = y1+fb*(y2-y0)
    return (p1x,p1y),(p2x,p2y)


if __name__ == "__main__":
    #Take energy values as arguments when calling from the command line
    main(sys.argv[1:])
