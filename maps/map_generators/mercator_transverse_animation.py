import numpy as np
import matplotlib.pyplot as plt
import math as m
from typing import List, Dict, Union
from numpy.typing import NDArray
from functools import partial

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from commons.coords_transformation import *
from commons.file_management import *


#----------------------------------------------------------------------
# CONFIG
#----------------------------------------------------------------------

# TITLE
name="Transverse Mercator Animation"

# PARAMETERS
angle_direction=90
long=np.linspace(0,360,300)


root1="../../data/coastline/asia-cil.txt"
root2="../../data/coastline/europe-cil.txt"
root3="../../data/coastline/africa-cil.txt"
root4="../../data/coastline/namer-cil.txt"
root5="../../data/coastline/samer-cil.txt"
root6_meridians="../../data/parallel_meridians/meridians.txt"
root7_parallels="../../data/parallel_meridians/parallels.txt"

i=0

long=long[73:]

if not os.path.exists("../png/"):
    os.makedirs("../png/")

if not os.path.exists("../png/all_maps/"):
    os.makedirs("../png/all_maps/")

for l in long:
    

    center=np.array([0,l])


    # PROJECTION
    point_calc=partial(ob_mercator_map,center=center,direction=angle_direction)


    #----------------------------------------------------------------------
    # POINT CALCULATIONS
    #----------------------------------------------------------------------



    coords1=point_calc(root1)
    coords2=point_calc(root2)
    coords3=point_calc(root3)
    coords4=point_calc(root4)
    coords5=point_calc(root5)
    coords6_meridians=point_calc(root6_meridians)
    coords7_parallels=point_calc(root7_parallels)

        

    #----------------------------------------------------------------------
    # PLOTTING
    #----------------------------------------------------------------------

    fig, ax = plt.subplots(figsize=(20, 11.25))
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    x1 = [punto[0] for punto in coords1]
    y1 = [punto[1] for punto in coords1]

    x2 = [punto[0] for punto in coords2]
    y2 = [punto[1] for punto in coords2]

    x3 = [punto[0] for punto in coords3]
    y3 = [punto[1] for punto in coords3]

    x4 = [punto[0] for punto in coords4]
    y4 = [punto[1] for punto in coords4]

    x5 = [punto[0] for punto in coords5]
    y5 = [punto[1] for punto in coords5]

    x_mer = [punto[0] for punto in coords6_meridians]
    y_mer = [punto[1] for punto in coords6_meridians]

    x_pal = [punto[0] for punto in coords7_parallels]
    y_pal = [punto[1] for punto in coords7_parallels]

    # Plotting of coastlines
    plt.scatter(x1, y1, s=0.01)
    plt.scatter(x2, y2, s=0.01)
    plt.scatter(x3, y3, s=0.01)
    plt.scatter(x4, y4, s=0.01)
    plt.scatter(x5, y5, s=0.01)
    plt.scatter(x_mer, y_mer, s=0.01, alpha=0.2, c='k')
    plt.scatter(x_pal, y_pal, s=0.01, alpha=0.2, c='k')

    # Plot limit
    h=np.linspace(-2,2,1000)
    l=np.linspace(-np.pi, np.pi,1000)

    cons1=[-2]*1000
    cons2=[2]*1000
    cons3=[-np.pi]*1000
    cons4=[np.pi]*1000

    plt.plot(l,cons1,c='k')
    plt.plot(l,cons2,c='k')
    plt.plot(cons3,h,c='k')
    plt.plot(cons4,h,c='k')

    # Title
    plt.title(name)
    plt.xlim(-np.pi, np.pi)
    plt.ylim(-2, 2)
    plt.gca().set_aspect(np.pi/4, adjustable='box')


    root_all_maps="../png/all_maps/"
    files=os.listdir(root_all_maps)
    n=str(len(files)+1)

    plt.savefig(root_all_maps+n+".png", dpi=300, bbox_inches='tight')


    i=i+1
    print(str(i)+"/227")
