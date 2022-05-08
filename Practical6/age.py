import numpy as np
import matplotlib.pyplot as plt
N=10
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]#create the two list
x=np.array(paternal_age)
y=np.array(chd)
#Create two array of x,y and the numbers from paternal_age and chd
plt.xlabel('paternal_age')
plt.ylabel('chd')
plt.scatter(x,y,marker='o')
plt.show()# create a scatter plot that show the relationship between paternal age and chd

paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
chd={'30':1.03,'35':1.07,'40':1.11,'45':1.17,'50':1.23,'55':1.32,'60':1.42,'65':1.55,'70':1.72,'75':1.94}# creat the dict that paternal_age one to one correspondence to chd
x='35'#choose x as the variable for age that can be modified and will return the correct risk of cardiovascular health in the offsprint
print (chd[x])
