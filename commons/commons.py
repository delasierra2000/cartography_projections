import numpy as np
from numpy.typing import NDArray

#Degrees to radians
def Deg2Rad(angle: np.float64)->np.float64:

    return angle*2*np.pi/360

#Spheric coortinates to Cartesian
def EtoC(vector: NDArray[np.float64])->NDArray[np.float64]:


    phi=vector[:,0]
    lamb=vector[:,1]

    X=np.cos(phi)*np.cos(lamb)
    Y=np.cos(phi)*np.sin(lamb)
    Z=np.sin(phi)

    return np.stack((X,Y,Z),axis=1)

def CtoE(vector: NDArray[np.float64])->NDArray[np.float64]:


    x=vector[:,0]
    y=vector[:,1]
    z=vector[:,2]

    phi=np.arcsin(z)
    lamb=np.atan2(y,x)

    return np.stack((phi,lamb),axis=1)


def rot(rotation_vector: NDArray[np.float64],angle:np.float64)->NDArray[np.float64]:

    r1=rotation_vector[0][0]
    r2=rotation_vector[0][1]
    r3=rotation_vector[0][2]

    U=np.array([[0,-r3,r2],[r3,0,-r1],[-r2,r1,0]])
    #lat_0=-lat_0
    R=np.cos(angle)*np.identity(3)+(1-np.cos(angle))*(rotation_vector.T @ rotation_vector)+np.sin(angle)*U
    return R.T


def rot2ecuator(center:NDArray[np.float64])->NDArray[np.float64]:

    lat_0=center[0]
    long_0=center[1]

    temp_vector=EtoC(np.array([[0,long_0]]))
    rotation_vector=np.cross(np.array([0,0,1]),temp_vector)
    
    return rot(rotation_vector,lat_0)

def rot_vector2vector(original_vector: NDArray[np.float64],final_vector: NDArray[np.float64])->NDArray[np.float64]:

    alpha=np.arccos(original_vector @ (final_vector.T))

    rotation_vector=-np.cross(original_vector,final_vector)
    rotation_vector=rotation_vector/np.linalg.norm(rotation_vector)

    return rot(rotation_vector,-alpha)














