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

save_folder="mercator_2"
suffix="MERC" 
name="Mercator_2"

# TITLE
name="Mercator"

# PARAMETERS
angle_direction=0
center_pos=np.array([0,0])

# PROJECTION

point_calc=partial(mercator_ob_map,center=center_pos,angle=angle_direction)


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

data=circle(np.array([[0,0]]),0.7)
elipse_points=mercator_ob_map2(data,center_pos,angle_direction)

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
df8 = pd.DataFrame(elipse_points, columns=["x", "y"])
df8["source"] = "circle"


df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], ignore_index=True)

canvas = ds.Canvas(plot_width=2000, plot_height=1000, x_range=(-np.pi, np.pi), y_range=(-2, 2))
a1 = canvas.points(df, 'x', 'y')  


img = tf.shade(a1,cmap=["black"])
img = tf.set_background(img, "white") 

#Show img
img.to_pil().show()


#Save
save_maps_enumerated(img)

#Show time
stop = timeit.default_timer()

print('Time: ', stop - start)  







