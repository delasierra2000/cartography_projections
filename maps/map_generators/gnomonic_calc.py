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

# CALCULATE POINTS?
bool=True

# SAVE POINTS?
bool2=False

save_folder="gnomonic_2"
suffix="GNOM" 
name="Gnomonic_2"

# TITLE
name="Gnomonic"

# PARAMETERS
angle=0
center=np.array([90,0])

# PROJECTION
point_calc=partial(gnomonic_map,phi_max=angle,center=center)



#----------------------------------------------------------------------
# POINT CALCULATIONS
#----------------------------------------------------------------------

calc_root1="../../data/coastline/"+save_folder+"/asia-cil-"+suffix+".txt"
calc_root2="../../data/coastline/"+save_folder+"/europe-cil-"+suffix+".txt"
calc_root3="../../data/coastline/"+save_folder+"/africa-cil-"+suffix+".txt"
calc_root4="../../data/coastline/"+save_folder+"/namer-cil-"+suffix+".txt"
calc_root5="../../data/coastline/"+save_folder+"/samer-cil-"+suffix+".txt"
calc_root6="../../data/parallel_meridians/"+save_folder+"/meridians-"+suffix+".txt"
calc_root7="../../data/parallel_meridians/"+save_folder+"/parallels-"+suffix+".txt"


if bool:

    root1="../../data/coastline/asia-cil.txt"
    root2="../../data/coastline/europe-cil.txt"
    root3="../../data/coastline/africa-cil.txt"
    root4="../../data/coastline/namer-cil.txt"
    root5="../../data/coastline/samer-cil.txt"
    root6_meridians="../../data/parallel_meridians/meridians.txt"
    root7_parallels="../../data/parallel_meridians/parallels.txt"


    coords1=point_calc(root1)
    coords2=point_calc(root2)
    coords3=point_calc(root3)
    coords4=point_calc(root4)
    coords5=point_calc(root5)
    coords6_meridians=point_calc(root6_meridians)
    coords7_parallels=point_calc(root7_parallels)

    if bool2:

        if not os.path.exists("../../data/coastline/"+save_folder):
            os.makedirs("../../data/coastline/"+save_folder)

        if not os.path.exists("../../data/parallel_meridians/"+save_folder):
            os.makedirs("../../data/parallel_meridians/"+save_folder)

        save_coords(calc_root1,coords1)
        save_coords(calc_root2,coords2)
        save_coords(calc_root3,coords3)
        save_coords(calc_root4,coords4)
        save_coords(calc_root5,coords5)
        save_coords(calc_root6,coords6_meridians)
        save_coords(calc_root7,coords7_parallels)

else:

    coords1=file_data_extraction(calc_root1)
    coords2=file_data_extraction(calc_root2)
    coords3=file_data_extraction(calc_root3)
    coords4=file_data_extraction(calc_root4)
    coords5=file_data_extraction(calc_root5)
    coords6_meridians=file_data_extraction(calc_root6)
    coords7_parallels=file_data_extraction(calc_root7)

#----------------------------------------------------------------------
# PLOTTING
#----------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(20, 11.25))

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
r=1/np.tan(angle*2*np.pi/360)
list_theta=np.linspace(0,2*np.pi,1000)
x=[r*np.cos(t) for t in list_theta]
y=[r*np.sin(t) for t in list_theta]

plt.plot(x, y, c='k')

# Title
plt.title(name)
plt.gca().set_aspect(1, adjustable='box')

#save png
if not os.path.exists("../png/"):
    os.makedirs("../png/")

if not os.path.exists("../png/all_maps/"):
    os.makedirs("../png/all_maps/")

plt.savefig("../png/"+name+".png", dpi=300, bbox_inches='tight')

root_all_maps="../png/all_maps/"
files=os.listdir(root_all_maps)
n=str(len(files)+1)

plt.savefig(root_all_maps+n+".png", dpi=300, bbox_inches='tight')

# Show Graphic
plt.show()
