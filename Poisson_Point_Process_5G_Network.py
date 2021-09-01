import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from random import randint
import scipy 


#Simulation window parameters
xMin=0;xMax=1000
yMin=0;yMax=1000
xDelta=xMax-xMin
yDelta=yMax-yMin #rectangle dimensions

areaTotal=xDelta*yDelta




 
#Point process parameters
lambda0=200e-6; #intensity (ie mean density) of the Poisson process
lambda1= 5e-6
lambda2 = 50e-6





#Simulate Poisson point process
ms_num = scipy.stats.poisson( lambda0*areaTotal ).rvs()     #Poisson number of points
num_macro = scipy.stats.poisson( lambda1*areaTotal ).rvs()  #Poisson number of points
num_small = scipy.stats.poisson( lambda2*areaTotal ).rvs()  #Poisson number of points

print("ms_num : ", ms_num)
print("num_macro : ", num_macro)
print("num_small : ", num_small)




#coordinates of Poisson points
macro_X = xDelta*scipy.stats.uniform.rvs(0,1,(num_macro,1))+xMin
macro_Y = yDelta*scipy.stats.uniform.rvs(0,1,(num_macro,1))+yMin

small_X = xDelta*scipy.stats.uniform.rvs(0,1,(num_small,1))+xMin
small_Y = yDelta*scipy.stats.uniform.rvs(0,1,(num_small,1))+yMin

ms_X = xDelta*scipy.stats.uniform.rvs(0,1,(ms_num,1))+xMin  
ms_Y = yDelta*scipy.stats.uniform.rvs(0,1,(ms_num,1))+yMin  




#figure
plt.scatter(ms_X, ms_Y, s=1, c="black", marker="s", label='UE' )
plt.xlabel("x"); plt.ylabel("y")

plt.scatter(macro_X,macro_Y, c="red", marker="^", label='Macro Cell' )    
plt.xlabel("x"); plt.ylabel("y")

plt.scatter(small_X,small_Y, c="green", marker="^", label='Small Cell' )
plt.xlabel("x"); plt.ylabel("y")

plt.legend(bbox_to_anchor=(1, 1))
plt.show()
