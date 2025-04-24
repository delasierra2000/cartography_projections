import numpy as np
from typing import List, Dict, Union
from numpy.typing import NDArray
import datashader as ds
import os

#function to extract the data from .txt and obtain a list of point vectors.
def file_data_extraction(root: str)->NDArray[np.float64]:

    file=open(root,"r")
    data=file.readlines()

    #data treatment
    data=np.array([(x.replace("\t","").replace("\n","")).split(" ") for x in data if not (x[2]).isalpha()],dtype=np.float64)

    return data 

def save_coords(root: str, data: list[NDArray[np.float64]]):

    text2save=[str(x[0])+' '+str(x[1]) for x in data]
    file=open(root,'w')
    file.writelines('\n'.join(text2save))
    file.close()

    return

def save_maps_enumerated(img):

    root="../png/all_maps/"
    if not os.path.exists("../png/"):
        os.makedirs("../png/")

    if not os.path.exists(root):
        os.makedirs(root)

    files=os.listdir(root)
    n=str(len(files)+1)
    ds.utils.export_image(img=img,filename=n, fmt=".png", background=None,export_path=root)

    return

