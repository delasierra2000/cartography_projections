import numpy as np
from typing import List, Dict, Union
from numpy.typing import NDArray

#function to extract the data from .txt and obtain a list of point vectors.
def file_data_extraction(root: str)->List[NDArray[np.float64]]:

    file=open(root,"r")
    data=file.readlines()

    #data treatment
    data=[np.array((x.replace("\t","").replace("\n","")).split(" "),dtype=np.float64) for x in data if not (x[2]).isalpha()]

    return data 

def save_coords(root: str, data: list[NDArray[np.float64]]):

    text2save=[str(x[0])+' '+str(x[1]) for x in data]
    file=open(root,'w')
    file.writelines('\n'.join(text2save))
    file.close()

    return

