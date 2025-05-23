import numpy as np
from numpy.typing import NDArray
import os
import sys

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
def mercator_map(root: str,long_ini: np.float64)->NDArray[np.float64]:

    factor=2*np.pi/360
    long_ini=long_ini*factor
    data=file_data_extraction(root)*factor

    return proj_cylinder(data,long_ini)

def mercator_ob_map(root: str, center: NDArray[np.float64], angle: np.float64)->NDArray[np.float64]:

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

def mercator_ob_map2(data: NDArray[np.float64], center: NDArray[np.float64], angle: np.float64)->NDArray[np.float64]:

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


def gnomonic_standard_map(root: str, phi_max: np.float64=45)->NDArray[np.float64]:

    data=file_data_extraction(root)*2*np.pi/360
    phi_max=phi_max*2*np.pi/360

    return proj_standard_gnomonic(data, phi_max)

def gnomonic_map(root: str, phi_max: np.float64=45, center: NDArray[np.float64]=np.array([90,0]))->NDArray[np.float64]:

    phi_max=phi_max*2*np.pi/360
    center=center*2*np.pi/360
    data=file_data_extraction(root)*2*np.pi/360

    center_as_matrix=center[np.newaxis, :]
    vector_center=EtoC(center_as_matrix)

    M=rot_vector2vector(vector_center,np.array([0,0,1]))


    rotated_data = CtoE(EtoC(data) @ M)

    return proj_standard_gnomonic(rotated_data, phi_max)


#----------------------------------------
# STEREOGRAPHIC
#----------------------------------------

#function that pojects the points on the spheric surface onto the the cylinder 
def proj_standard_ster(vector: NDArray[np.float64],phi_max: np.float64)->NDArray[np.float64]:

    
    vector=vector[(vector[:,0]>-np.pi/2) & (vector[:,0]>phi_max)]
    phi=vector[:,0]
    lamb=vector[:,1]

    x = np.cos(phi)*np.sin(lamb)/(1+np.sin(phi))

    y = -np.cos(phi)*np.cos(lamb)/(1+np.sin(phi))

    return np.stack((x,y),axis=1)

def ster_standard_map(root: str, phi_max: np.float64=45)->NDArray[np.float64]:

    data=file_data_extraction(root)*2*np.pi/360
    phi_max=phi_max*2*np.pi/360

    return proj_standard_ster(data, phi_max)

def ster_map(root: str, phi_max: np.float64=45, center: NDArray[np.float64]=np.array([90,0]))->NDArray[np.float64]:

    phi_max=phi_max*2*np.pi/360
    center=center*2*np.pi/360
    data=file_data_extraction(root)*2*np.pi/360

    center_as_matrix=center[np.newaxis, :]
    vector_center=EtoC(center_as_matrix)

    M=rot_vector2vector(vector_center,np.array([0,0,1]))


    rotated_data = CtoE(EtoC(data) @ M)

    return proj_standard_ster(rotated_data, phi_max)

#----------------------------------------
# CONIC
#----------------------------------------

def proj_standard_conic(vector: NDArray[np.float64], center: NDArray[np.float64], phi1: np.float64, phi2: np.float64)->NDArray[np.float64]:
 
    
    vector=vector[vector[:,0]>=0]
    phi=vector[:,0]
    lamb=vector[:,1]
    phi0=center[0]
    lamb0=center[1]

    n=(np.sin(phi1)+np.sin(phi2))/2
    C=np.cos(phi1)**2+2*n*np.sin(phi1)
    ro0=np.sqrt(C-2*n*np.sin(phi0))/n
    theta=n*lamb
    ro=np.sqrt(C-2*n*np.sin(phi))/n

    x = ro*np.sin(theta)
    y = ro0-ro*np.cos(theta)


    return np.stack((x,y),axis=1)

def standard_conic_map(root: str, center: NDArray[np.float64], phi1: np.float64, phi2: np.float64)->NDArray[np.float64]:

    data=file_data_extraction(root)*2*np.pi/360
    center=center*2*np.pi/360
    phi1=phi1*2*np.pi/360
    phi2=phi2*2*np.pi/360


    return proj_standard_conic(data, center, phi1, phi2)

#----------------------------------------
# ELIPSE INDICATRIZ DE TISSOT
#----------------------------------------

def circle_Z(r:np.float64)->NDArray[np.float64]:

    z=np.sqrt(1-r**2)

    alpha_list=np.linspace(0,2*np.pi,1000)
    points=np.zeros((1000,3))
    i=0
    for alpha in alpha_list:
        x=r*np.cos(alpha)
        y=r*np.sin(alpha)
        points[i,:]=np.array([x,y,z])
        i=i+1

    return points

def circle(center: NDArray[np.float64],r:np.float64):

    vector_center=EtoC(center)
    Z=np.array([[0,0,1]])
    M=rot_vector2vector(Z,vector_center)

    points=circle_Z(r)
    rotated_points=CtoE(points @ M)*360/(2*np.pi)


    return rotated_points
