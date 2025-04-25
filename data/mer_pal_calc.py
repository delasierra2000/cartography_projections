import numpy as np
from numpy.typing import NDArray
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from commons.coords_transformation import *

#function to save the obtained coordinates into a txt file
def save_coords(root: str, data: list[NDArray[np.float64]]):

    text2save=[str(x[0])+' '+str(x[1]) for x in data]
    file=open(root,'w')
    file.writelines('\n'.join(text2save))
    file.close()

    return






#root="./data/parallel_meridians/parallels.txt"
#save_coords(root,parallels)




#meridians

phi=np.linspace(-89.99,89.99,10000)
meridian=[]
for i in range (0,24):
    long=15*i-180
    meridian=meridian+[np.array([p,long]) for p in phi]

meridians_points=meridian


root="./parallel_meridians/meridians.txt"
save_coords(root,meridians_points)


#parallels

long=np.linspace(-180,180,10000)
parallel=[]

for i in range (-5,6):
    phi=15*i
    parallel=parallel+[np.array([phi,p]) for p in long]

parallels_points=parallel



root="./parallel_meridians/parallels.txt"
save_coords(root,parallels_points)