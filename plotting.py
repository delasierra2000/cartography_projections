import numpy as np
import matplotlib.pyplot as plt
import math as m
from typing import List, Dict, Union
from numpy.typing import NDArray
import os
from commons.coords_transformation import *


root1="./data/coastline/mercator_points/asia-cil-MERC.txt"
root2="./data/coastline/mercator_points/europe-cil-MERC.txt"
root3="./data/coastline/mercator_points/africa-cil-MERC.txt"
root4="./data/coastline/mercator_points/namer-cil-MERC.txt"
root5="./data/coastline/mercator_points/samer-cil-MERC.txt"

coords1=file_data_extraction(root1)
coords2=file_data_extraction(root2)
coords3=file_data_extraction(root3)
coords4=file_data_extraction(root4)
coords5=file_data_extraction(root5)

print(len(coords1)+len(coords2)+len(coords3)+len(coords4)+len(coords5))


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

# Plotting of coastlines
plt.scatter(x1, y1, s=0.01)
plt.scatter(x2, y2, s=0.01)
plt.scatter(x3, y3, s=0.01)
plt.scatter(x4, y4, s=0.01)
plt.scatter(x5, y5, s=0.01)

# Labels
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Title
plt.title('Mercator')
plt.xlim(-np.pi, np.pi)
plt.ylim(-2, 2)
plt.gca().set_aspect(np.pi/4, adjustable='box')

# Show Graphic
plt.show()