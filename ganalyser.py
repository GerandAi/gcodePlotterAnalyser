with open("eggpoints.txt", 'r') as fp:
    x = [0]
    y = [0]
    z = [0]
    mx = 0
    while True:
        line = fp.readline()
        if not line:
            break
        else:
            X = line.split("X", 1)[1]
            X = X.split(" Y", 1)[0]
            Y = line.split("Y", 1)[1]
            Y = Y.split(" Z", 1)[0]
            Z = line.split("Z", 1)[1]
            Z = Z[:-1]
            X = float(X)
            Y = float(Y)
            Z = float(Z)

            #if 1:
            if X >= mx:
                x.append(X)
                y.append(Y)
                z.append(Z)
            mx = X

    fp.close()

i=1
fz = 0
c = 0
fc = []
h = []
xthresh = 6.2
ythresh = 5.2
dc = 0
cc = 233.6
while z[i] < z[-1]:
    dx = x[i+1]-x[i]
    dy = y[i+1]-y[i]
    dz = z[i+1]-z[i]
    if dz == 0 and dx >= 0 and dy <= ythresh and dx <= xthresh:
        c = c + (dx**2 + dy**2)**(1/2)
        #print(dx, dy, c)
    elif dz > 0:
        dc = abs(c - cc)
        if dc <= 0.3:
            fc.append(c)
            fz = fz + dz
            h.append(fz)
        else:
            #print("Large jump skipped!")
            pass
        cc = c
        c = 0
        #print(h)
    else:
        #print("Large jump skipped!")
        pass
    i+=1

#index_of_the_first_element_to_be_deleted = len(x)
#end = index_of_the_first_element_to_be_deleted
a = [0, 100]
start3d = int(len(x)*(a[0]/100))+1
end3d = int(len(x)*(a[1]/100))
step3d = 100
b = [0, 100]
start2d = int(len(h)*(b[0]/100))+1
end2d = int(len(h)*(b[1]/100))
step2d = 100
##dilution
x = x[start3d:end3d:step3d]
y = y[start3d:end3d:step3d]
z = z[start3d:end3d:step3d]
##import library
import numpy as np
fc = np.array(fc[start2d:end2d:step2d])
h = np.array(h[start2d:end2d:step2d])
zeros = np.zeros(len(h))
#from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
#plt.rcParams["figure.autolayout"] = True
#######################fig = plt.figure()
ax = plt.axes(projection="3d")
##ax.scatter(x, y, z, c='red', s=1)
ax.plot_trisurf(x, y, z, linewidth = 0.2, antialiased = True)
##ax.plot(x, y, z, color='black')
hfc = np.divide(fc, 2.0)
kfc = np.multiply(hfc[::-1], -1.0)
fc = np.append(hfc, kfc)
zeros = np.append(zeros, zeros)
h = np.append(h, h[::-1])
bsize = 200
#######################################
####### Generating Bounding-Box #######
ax.scatter(bsize, 0, 0, c='grey', s=1)
ax.scatter(-bsize, 0, 0, c='grey', s=1)
ax.scatter(0, bsize, 0, c='grey', s=1)
ax.scatter(0, -bsize, 0, c='grey', s=1)
ax.scatter(0, 0, bsize, c='grey', s=1)
ax.scatter(0, 0, -bsize, c='grey', s=1)
#######################################
#ax.scatter(fc, zeros, h, c='red', s=1)
ax.plot(fc, zeros, h, color='black')
ax.plot([fc[-1], fc[0]], [0, 0], [h[-1], h[0]], color='black')
plt.show()

fp = open("flategg.txt", 'w')
for index in range(len(fc)):
    fp.write(str(fc[index])+"\t")
    fp.write(str(h[index])+"\t")
    fp.write("\n")
fp.close()
bsize = 180
######################################
###### Generating Bounding-Box #######
plt.scatter(bsize, 0, c='grey', s=1) #
plt.scatter(-bsize, 0, c='grey', s=1)#
plt.scatter(0, bsize, c='grey', s=1) #
plt.scatter(0, -bsize, c='grey', s=1)#
######################################
plt.plot(fc, h, color='black')
plt.plot([fc[-1], fc[0]], [h[-1], h[0]], color='black')
plt.show()
