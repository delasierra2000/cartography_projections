import numpy as np
import matplotlib.pyplot as plt
import math as m
from typing import List, Dict, Union
from numpy.typing import NDArray
import os
from commons.coords_transformation import *

#function to save the obtained coordinates into a txt file
def save_coords(root: str, data: list[NDArray[np.float64]]):

    text2save=[str(x[0])+' '+str(x[1]) for x in data]
    file=open(root,'w')
    file.writelines('\n'.join(text2save))
    file.close()

    return

root1="./data/coastline/asia-cil.txt"
root2="./data/coastline/europe-cil.txt"
root3="./data/coastline/africa-cil.txt"
root4="./data/coastline/namer-cil.txt"
root5="./data/coastline/samer-cil.txt"
root6_meridians="./data/parallel_meridians/meridians.txt"
root7_parallels="./data/parallel_meridians/parallels.txt"



coords1=ob_mercator_map(root1,np.array([40.4,-3.7]),0)
coords2=ob_mercator_map(root2,np.array([40.4,-3.7]),0)
coords3=ob_mercator_map(root3,np.array([40.4,-3.7]),0)
coords4=ob_mercator_map(root4,np.array([40.4,-3.7]),0)
coords5=ob_mercator_map(root5,np.array([40.4,-3.7]),0)
coords6_meridians=ob_mercator_map(root6_meridians,np.array([40.4,-3.7]),0)
coords7_parallels=ob_mercator_map(root7_parallels,np.array([40.4,-3.7]),0)

calc_root1="./data/coastline/ob_mercator_points/asia-cil-MERC.txt"
calc_root2="./data/coastline/ob_mercator_points/europe-cil-MERC.txt"
calc_root3="./data/coastline/ob_mercator_points/africa-cil-MERC.txt"
calc_root4="./data/coastline/ob_mercator_points/namer-cil-MERC.txt"
calc_root5="./data/coastline/ob_mercator_points/samer-cil-MERC.txt"
calc_root6="./data/parallel_meridians/ob_mercator/meridians_MERC.txt"
calc_root7="./data/parallel_meridians/ob_mercator/parallels_MERC.txt"

save_coords(calc_root1,coords1)
save_coords(calc_root2,coords2)
save_coords(calc_root3,coords3)
save_coords(calc_root4,coords4)
save_coords(calc_root5,coords5)
save_coords(calc_root6,coords6_meridians)
save_coords(calc_root7,coords7_parallels)