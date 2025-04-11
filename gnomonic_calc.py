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



coords1=gnomonic_map(root1,30)
coords2=gnomonic_map(root2,30)
coords3=gnomonic_map(root3,30)
coords4=gnomonic_map(root4,30)
coords5=gnomonic_map(root5,30)
coords6_meridians=gnomonic_map(root6_meridians,30)
coords7_parallels=gnomonic_map(root7_parallels,30)

calc_root1="./data/coastline/gnomonic_standard_points/asia-cil-GNOM.txt"
calc_root2="./data/coastline/gnomonic_standard_points/europe-cil-GNOM.txt"
calc_root3="./data/coastline/gnomonic_standard_points/africa-cil-GNOM.txt"
calc_root4="./data/coastline/gnomonic_standard_points/namer-cil-GNOM.txt"
calc_root5="./data/coastline/gnomonic_standard_points/samer-cil-GNOM.txt"
calc_root6="./data/parallel_meridians/gnomonic_standard/meridians_GNOM.txt"
calc_root7="./data/parallel_meridians/gnomonic_standard/parallels_GNOM.txt"

save_coords(calc_root1,coords1)
save_coords(calc_root2,coords2)
save_coords(calc_root3,coords3)
save_coords(calc_root4,coords4)
save_coords(calc_root5,coords5)
save_coords(calc_root6,coords6_meridians)
save_coords(calc_root7,coords7_parallels)