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

    if abs(X-1)<=0.01 and Y==0:
        X_plane=0
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

#center cartesian coordinates to ecuator, then to vector (0,0,1), then rotation from (0,0,1)
def ob_mercator_map(root: str, center:NDArray[np.float64], direction : np.float64)->List[NDArray[np.float64]]:


    vector_center=EtoC(center)
    a=1/np.sqrt((vector_center[0])**2+(vector_center[1])**2)
    new_vector=a*np.array([vector_center[0],vector_center[1],0])
    angle=-Deg2Rad(direction)
    M1=matrix_rot(vector_center,new_vector)
    M2=matrix_rot(new_vector,np.array([1,0,0]))
    Mx=np.array([[1, 0, 0], [0, np.cos(angle), -np.sin(angle)],[0,np.sin(angle),np.cos(angle)]])

    M_final=Mx @ M2 @ M1
    
    data=file_data_extraction(root)

    data2=[M_final @ EtoC(x) for x in data]

    return [cylinder2plane(proj_cylinder(x)) for x in data2]

#Calculates the matrix rotation to rotate one unit vector to another
def matrix_rot(initial_vector:NDArray[np.float64], final_vector:NDArray[np.float64])->NDArray[np.float64]:


    v=np.cross(initial_vector,final_vector)
    cos=np.dot(final_vector,initial_vector)

    M=np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]],[-v[1],v[0],0]])

    np.identity(3)+M+M@M*(1/(1+cos))

    return np.identity(3)+M+M@M*(1/(1+cos))
