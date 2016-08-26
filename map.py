'''
    File name: create map.py
    Author: Ahmed Charef
    Date created: 10/03/2016
    Date last modified: 14/03/2016
    Python Version: 2.7
'''
import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = []
y = []
z = []

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
readfile = open('axeX.txt', 'r')
sepfile = readfile.read().split('\n')
for plot1 in sepfile:
	X = plot1.split('\n')
	X2 = float(X[0])
	x.append(X2)
#print(x)

print('YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
readfile2 = open('axeY.txt', 'r')
sepfile2 = readfile2.read().split('\n')
for plot2 in sepfile2:
        Y = plot2.split('\n')
	Y2 = float(Y[0])
        y.append(Y2)
#print(y)

print('ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ')
readfile3 = open('axeZ.txt', 'r')
sepfile3 = readfile3.read().split('\n')
for plot3 in sepfile3:
        Z = plot3.split('\n')
        Z2 = float(Z[0])        
	z.append(Z2)
#print(z)

#plt.plot(x,y)
#plt.xlabel('X axis')
#plt.ylabel('Y axis')

ax.scatter(x, y, z, c ='r', marker ='o')
ax.plot(x, y, z, '^', c='gray')
#ax.plot(y, y, z, 'o', c='white')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')


#plt.plot(x,y)
plt.show()
readfile3.close()
readfile2.close()
readfile.close()



