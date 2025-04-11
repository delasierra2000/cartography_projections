import numpy as np
import matplotlib.pyplot as plt
import math as m
from typing import List, Dict, Union
from numpy.typing import NDArray
import os
from commons.coords_transformation import *


root1="./data/coastline/gnomonic_center_points/asia-cil-GNOM.txt"
root2="./data/coastline/gnomonic_center_points/europe-cil-GNOM.txt"
root3="./data/coastline/gnomonic_center_points/africa-cil-GNOM.txt"
root4="./data/coastline/gnomonic_center_points/namer-cil-GNOM.txt"
root5="./data/coastline/gnomonic_center_points/samer-cil-GNOM.txt"
root6_meridians="./data/parallel_meridians/gnomonic_center/meridians_GNOM.txt"
root7_parallels="./data/parallel_meridians/gnomonic_center/parallels_GNOM.txt"

coords1=file_data_extraction(root1)
coords2=file_data_extraction(root2)
coords3=file_data_extraction(root3)
coords4=file_data_extraction(root4)
coords5=file_data_extraction(root5)
coords6_meridians=file_data_extraction(root6_meridians)
coords7_parallels=file_data_extraction(root7_parallels)



x1 = [punto[0] for punto in coords1]
y1 = [punto[1] for punto in coords1]

x2 = [punto[0] for punto in coords2]
y2 = [punto[1] for punto in coords2]

x3 = [punto[0] for punto in coords3]
y3 = [punto[1] for punto in coords3]

x4 = [punto[0] for punto in coords4]
y4 = [punto[1] for punto in coords4]

x5 = [punto[0] for punto in coords5]
y5 = [punto[1] for punto in coords5]

x_mer = [punto[0] for punto in coords6_meridians]
y_mer = [punto[1] for punto in coords6_meridians]

x_pal = [punto[0] for punto in coords7_parallels]
y_pal = [punto[1] for punto in coords7_parallels]

# Plotting of coastlines
plt.scatter(x1, y1, s=0.01)
plt.scatter(x2, y2, s=0.01)
plt.scatter(x3, y3, s=0.01)
plt.scatter(x4, y4, s=0.01)
plt.scatter(x5, y5, s=0.01)
plt.scatter(x_mer, y_mer, s=0.01, alpha=0.2, c='k')
plt.scatter(x_pal, y_pal, s=0.01, alpha=0.2, c='k')

# Plot limit
r=1/np.tan(30*2*np.pi/360)
list_theta=np.linspace(0,2*np.pi,1000)
x=[r*np.cos(t) for t in list_theta]
y=[r*np.sin(t) for t in list_theta]

plt.plot(x, y, c='k')

# Labels
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Title
plt.title('Gnomonic Spain centered')
plt.gca().set_aspect(1, adjustable='box')

# Show Graphic
plt.show()

