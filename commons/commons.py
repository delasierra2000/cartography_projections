import numpy as np
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

#Calculates the matrix rotation to rotate one unit vector to another
def matrix_rot(initial_vector:NDArray[np.float64], final_vector:NDArray[np.float64])->NDArray[np.float64]:


    v=np.cross(initial_vector,final_vector)
    cos=np.dot(final_vector,initial_vector)

    M=np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]],[-v[1],v[0],0]])

    np.identity(3)+M+M@M*(1/(1+cos))

    return np.identity(3)+M+M@M*(1/(1+cos))

