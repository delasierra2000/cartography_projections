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



coords1=mercator_map(root1)
coords2=mercator_map(root2)
coords3=mercator_map(root3)
coords4=mercator_map(root4)
coords5=mercator_map(root5)
coords6_meridians=mercator_map(root6_meridians)
coords7_parallels=mercator_map(root7_parallels)

calc_root1="./data/coastline/mercator_points/asia-cil-MERC.txt"
calc_root2="./data/coastline/mercator_points/europe-cil-MERC.txt"
calc_root3="./data/coastline/mercator_points/africa-cil-MERC.txt"
calc_root4="./data/coastline/mercator_points/namer-cil-MERC.txt"
calc_root5="./data/coastline/mercator_points/samer-cil-MERC.txt"
calc_root6="./data/parallel_meridians/mercator/meridians_MERC.txt"
calc_root7="./data/parallel_meridians/mercator/parallels_MERC.txt"

save_coords(calc_root1,coords1)
save_coords(calc_root2,coords2)
save_coords(calc_root3,coords3)
save_coords(calc_root4,coords4)
save_coords(calc_root5,coords5)
save_coords(calc_root6,coords6_meridians)
save_coords(calc_root7,coords7_parallels)