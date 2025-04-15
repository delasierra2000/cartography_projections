import numpy as np
from typing import List, Dict, Union
from numpy.typing import NDArray
import os
import sys
import timeit

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from commons.commons import *
from commons.file_management import *


#----------------------------------------
# CILINDER
#----------------------------------------

#function that pojects the points on the spheric surface onto the the cylinder 


def proj_cylinder(vector: NDArray[np.float64],long_ini:float)->NDArray[np.float64]:

    factor=2*np.pi/360
    long_ini=long_ini*factor
    long=vector[:,1]*factor
    lat=vector[:,0]*factor


    x = np.where(
        np.abs(long - long_ini) <= np.pi,
        long - long_ini,
        np.where(
            long - long_ini<-np.pi,
            long - long_ini + 2 * np.pi,
            long - long_ini - 2 * np.pi
        )
    )
    
    y=np.log(np.tan(np.pi/4+lat/2))
    
    return np.stack((x,y),axis=1)







#funtion to obtain the points in the 2D representation (Mercator)
def mercator_map(root: str,long_ini: np.float64)->List[NDArray[np.float64]]:

    data=file_data_extraction(root)

    return proj_cylinder(data,long_ini)

def mercator_map2(root: str, center: NDArray[np.float64], angle: np.float64)->List[NDArray[np.float64]]:

    data=file_data_extraction(root)
    data=data*2*np.pi/360
    center=center*2*np.pi/360
    angle=-angle*2*np.pi/360
    
    R=rot2ecuator(center)

    long_0=center[1]
    temp_vector=EtoC(np.array([[0,long_0]]))
    R2=rot(temp_vector,angle)

    M=R@R2


    rotated_data = CtoE(EtoC(data) @ M)/(2*np.pi/360)

    return proj_cylinder(rotated_data,center[1]/(2*np.pi/360))

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

#----------------------------------------
# GNOMONIC
#----------------------------------------

#function that pojects the points on the spheric surface onto the the cylinder 
def proj_standard_gnomonic(vector: NDArray[np.float64])->NDArray[np.float64]:

    Mg=np.array([[np.cos(-np.pi/2),-np.sin(-np.pi/2)],[np.sin(-np.pi/2),np.cos(-np.pi/2)]])

    if vector[2]<=0:
        sol=None
    else:
        constant=1/vector[2]
        sol=Mg @ (constant*vector[0:2])
        
    return sol


def gnomonic_standard_map(root: str, phi_max: np.float64=45)->List[NDArray[np.float64]]:

    data=file_data_extraction(root)
    data=[x for x in data if x[0]>phi_max]

    return [proj_standard_gnomonic(EtoC(x)) for x in data]

def gnomonic_map(root: str, phi_max: np.float64=45, center: NDArray[np.float64]=np.array([90,0]))->List[NDArray[np.float64]]:



    data=file_data_extraction(root)
    data=[EtoC(x) for x in data]
    direction=EtoC(center)
    M=matrix_rot(direction,np.array([0,0,1]))
    data=[M @ x for x in data]
    data2=[x for x in data if x[2]>np.sin(phi_max*2*np.pi/360)]

    return [proj_standard_gnomonic(x) for x in data2]


#----------------------------------------
# STEREOGRAPHIC
#----------------------------------------

#function that pojects the points on the spheric surface onto the the cylinder 
def proj_standard_stereographic(vector: NDArray[np.float64])->NDArray[np.float64]:

    vector=np.array([0,0,1])+vector

    Mg=np.array([[np.cos(-np.pi/2),-np.sin(-np.pi/2)],[np.sin(-np.pi/2),np.cos(-np.pi/2)]])

    constant=2/(vector[2])

    sol=Mg @ (constant*vector[0:2])
        
    return sol


def stereographic_standard_map(root: str, phi_max: np.float64=30)->List[NDArray[np.float64]]:

    data=file_data_extraction(root)
    data=[x for x in data if x[0]>phi_max]

    return [proj_standard_stereographic(EtoC(x)) for x in data]

def stereographic_map(root: str, phi_max: np.float64=45, center: NDArray[np.float64]=np.array([90,0]))->List[NDArray[np.float64]]:



    data=file_data_extraction(root)
    data=[EtoC(x) for x in data]
    direction=EtoC(center)
    M=matrix_rot(direction,np.array([0,0,1]))
    data=[M @ x for x in data]
    data2=[x for x in data if x[2]>np.sin(phi_max*2*np.pi/360)]

    return [proj_standard_stereographic(x) for x in data2]

