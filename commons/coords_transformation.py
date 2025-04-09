import numpy as np
import math as m
from typing import List, Dict, Union
from numpy.typing import NDArray

#Degrees to radians
def Deg2Rad(angle: np.float64)->np.float64:

    return angle*2*np.pi/360

#Spheric coortinates to Cartesian
def EtoC(vector: NDArray[np.float64])->NDArray[np.float64]:

    vector_rad=Deg2Rad(vector)

    phi=vector_rad[0]
    lamb=vector_rad[1]

    X=np.cos(phi)*np.cos(lamb)
    Y=np.cos(phi)*np.sin(lamb)
    Z=np.sin(phi)

    return np.array([X,Y,Z])

#function to extract the data from .txt and obtain a list of point vectors.
def file_data_extraction(root: str)->List[NDArray[np.float64]]:

    file=open(root,"r")
    data=file.readlines()

    #data treatment
    data=[np.array((x.replace("\t","").replace("\n","")).split(" "),dtype=np.float64) for x in data if not (x[2]).isalpha()]

    return data 

#function that pojects the points on the spheric surface onto the the cylinder 
def proj_cylinder(vector: NDArray[np.float64])->NDArray[np.float64]:

    constant=1/np.sqrt(vector[0]**2+vector[1]**2)
    
    return vector*constant

#cylinder to plane
def cylinder2plane(vector: NDArray[np.float64])->NDArray[np.float64]:
    
    X=vector[0]
    Y=vector[1]
    Z=vector[2]

    pos_from_green=np.array([1,0])
    vector_XY=np.array([X,Y])

    angle=np.arccos(np.dot(vector_XY,pos_from_green))

    if X==1 and Y==0:
        X_plane=X
    elif Y>0:
        angle=np.arccos(np.dot(vector_XY,pos_from_green))
        X_plane=angle
    else:
        angle=np.arccos(np.dot(vector_XY,pos_from_green))
        X_plane=-angle
    
    return np.array([X_plane,Z])

#funtion to obtain the points in the 2D representation (Mercator)
def mercator_map(root: str)->List[NDArray[np.float64]]:

    data=file_data_extraction(root)

    return [cylinder2plane(proj_cylinder(EtoC(x))) for x in data]