import numpy as np
from functools import partial
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

# TITLE
name="Transverse Mercator Animation"

# PARAMETERS
phi_max=30
lat=np.linspace(90,-90,600)



root1="../../data/coastline/asia-cil.txt"
root2="../../data/coastline/europe-cil.txt"
root3="../../data/coastline/africa-cil.txt"
root4="../../data/coastline/namer-cil.txt"
root5="../../data/coastline/samer-cil.txt"
root6_meridians="../../data/parallel_meridians/meridians.txt"
root7_parallels="../../data/parallel_meridians/parallels.txt"

i=0


if not os.path.exists("../png/"):
    os.makedirs("../png/")

if not os.path.exists("../png/all_maps/"):
    os.makedirs("../png/all_maps/")

for l in lat:
    

    center=np.array([l,0])


    # PROJECTION
    point_calc=partial(ster_map,phi_max=phi_max,center=center)


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

    r=np.cos(phi_max*2*np.pi/360)/(1+np.sin(phi_max*2*np.pi/360))
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

    #Save
    save_maps_enumerated(img)

    i=i+1
    print(str(i)+"/600")
