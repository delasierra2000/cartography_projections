import numpy as np
from functools import partial
import timeit
import datashader as ds
import datashader.transfer_functions as tf
import pandas as pd

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
angle=30
center=np.array([-90,0])

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

    start = timeit.default_timer()



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





df1 = pd.DataFrame(coords1, columns=["x", "y"])
df1["source"] = "points1"
df2 = pd.DataFrame(coords2, columns=["x", "y"])
df2["source"] = "points2"
df3 = pd.DataFrame(coords3, columns=["x", "y"])
df3["source"] = "points3"
df4 = pd.DataFrame(coords4, columns=["x", "y"])
df4["source"] = "points4"
df5 = pd.DataFrame(coords5, columns=["x", "y"])
df5["source"] = "points5"
df6 = pd.DataFrame(coords6_meridians, columns=["x", "y"])
df6["source"] = "points6"
df7 = pd.DataFrame(coords7_parallels, columns=["x", "y"])
df7["source"] = "points7"

r=1/np.tan(angle*2*np.pi/360)
list_theta=np.linspace(0,2*np.pi,10000)
x=[r*np.cos(t) for t in list_theta]
y=[r*np.sin(t) for t in list_theta]

df_circle=pd.DataFrame({'x':x,'y':y})

df = pd.concat([df1, df2, df3, df4, df5, df6, df7], ignore_index=True)



canvas = ds.Canvas(plot_width=1000, plot_height=1000, x_range=(-r, r), y_range=(-r, r))

a1 = canvas.points(df, 'x', 'y') 
img1 = tf.shade(a1,cmap=["black"])
img1 = tf.set_background(img1, "white") 

a2 = canvas.points(df_circle, 'x', 'y')
img2 = tf.shade(a2, cmap=["black"])


img= tf.stack(img1, img2)

#Show img
img.to_pil().show()

#Save
save_maps_enumerated(img)

#Show time
stop = timeit.default_timer()

print('Time: ', stop - start)  




