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

    lat=vector[:,0]
    long=vector[:,1]
    
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

    factor=2*np.pi/360
    long_ini=long_ini*factor
    data=file_data_extraction(root)*factor

    return proj_cylinder(data,long_ini)

def mercator_ob_map(root: str, center: NDArray[np.float64], angle: np.float64)->List[NDArray[np.float64]]:

    data=file_data_extraction(root)
    data=data*2*np.pi/360
    center=center*2*np.pi/360
    angle=-angle*2*np.pi/360
    
    R=rot2ecuator(center)

    long_0=center[1]
    temp_vector=EtoC(np.array([[0,long_0]]))
    R2=rot(temp_vector,angle)

    M=R@R2


    rotated_data = CtoE(EtoC(data) @ M)

    return proj_cylinder(rotated_data,center[1])



#----------------------------------------
# GNOMONIC
#----------------------------------------

#function that pojects the points on the spheric surface onto the the cylinder 



#Mg=np.array([[np.cos(-np.pi/2),-np.sin(-np.pi/2)],[np.sin(-np.pi/2),np.cos(-np.pi/2)]])



def proj_standard_gnomonic(vector: NDArray[np.float64],phi_max: np.float64)->NDArray[np.float64]:

    
    vector=vector[(vector[:,0]>0) & (vector[:,0]>phi_max)]
    phi=vector[:,0]
    lamb=vector[:,1]

    x = np.sin(lamb)/np.tan(phi)

    y = -np.cos(lamb)/np.tan(phi)

    return np.stack((x,y),axis=1)


def gnomonic_standard_map(root: str, phi_max: np.float64=45)->List[NDArray[np.float64]]:

    data=file_data_extraction(root)*2*np.pi/360
    phi_max=phi_max*2*np.pi/360

    return proj_standard_gnomonic(data, phi_max)

def gnomonic_map(root: str, phi_max: np.float64=45, center: NDArray[np.float64]=np.array([90,0]))->List[NDArray[np.float64]]:

    phi_max=phi_max*2*np.pi/360
    center=center*2*np.pi/360
    data=file_data_extraction(root)*2*np.pi/360

    center_as_matrix=center[np.newaxis, :]
    vector_center=EtoC(center_as_matrix)

    M=rot_vector2vector(vector_center,np.array([0,0,1]))

    print(vector_center @ M)


    rotated_data = CtoE(EtoC(data) @ M)

    return proj_standard_gnomonic(rotated_data, phi_max)


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

