##with open("Egg.txt", 'r') as fp:
##    fp0 = open("eggpoints.txt", 'w')
##    while True:
##        line = fp.readline()
##        if line == "":
##            break
##        elif ((line[0] == "G") & (line[1] == "1") & (line.__contains__(" E"))) | (line.__contains__(" Z")):
##            line = line.split("X", 1)[1]
##            line = "X" + line
##            if line.__contains__(" Z"):
##                height = "Z" + line.split(" Z", 1)[1]
##            elif line.__contains__(" E"):
##                line = line.split("E", 1)[0] + height
##            fp0.write(line)
##    fp0.close()
##    fp.close()

with open("eggpoints.txt", 'r') as fp:
    x = [0]
    y = [0]
    z = [0]
    xc = 0
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
            if X >= xc:
                x.append(X)
                y.append(Y)
                z.append(Z)
            xc = X

    fp.close()

#index_of_the_first_element_to_be_deleted = len(x)
#end = index_of_the_first_element_to_be_deleted
a = [0, 100]
start = int(len(x)*(a[0]/100))+1
end = int(len(x)*(a[1]/100))
##dilution
step = 25
x = x[start:end:step]
y = y[start:end:step]
z = z[start:end:step]
from matplotlib import pyplot as plt
#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
ax = plt.axes(projection="3d")
#ax.scatter(x, y, z, c='red', s=1)
#ax.plot(x, y, z, color='black')
ax.plot_trisurf(x, y, z, linewidth = 0.2, antialiased = True)
####################################################################
##################### Generating Bounding-Box ######################
bsize = 100                                                        #
import numpy as np                                                 #
xvector = np.array([bsize, 0, 0])                                  #
yvector = np.array([0, bsize, 0])                                  #
zvector = np.array([0, 0, bsize])                                  #
offset = np.array([sum(x)/len(x), sum(y)/len(y), sum(z)/len(z)])   #
xpositive = xvector + offset                                       #
xnegative = offset - xvector                                       #
ypositive = yvector + offset                                       #
ynegative = offset - yvector                                       #
zpositive = zvector + offset                                       #
znegative = offset - zvector                                       #
ax.scatter(xpositive[0], xpositive[1], xpositive[2], c='grey', s=1)#
ax.scatter(xnegative[0], xnegative[1], xnegative[2], c='grey', s=1)#
ax.scatter(ypositive[0], ypositive[1], ypositive[2], c='grey', s=1)#
ax.scatter(ynegative[0], ynegative[1], ynegative[2], c='grey', s=1)#
ax.scatter(zpositive[0], zpositive[1], zpositive[2], c='grey', s=1)#
ax.scatter(znegative[0], znegative[1], znegative[2], c='grey', s=1)#
####################################################################
plt.show()

###index_of_the_first_element_to_be_deleted = len(x)
###end = index_of_the_first_element_to_be_deleted
##a = 0
##start = int(len(x)*(a/100))+1
##end = int(len(x)*((a+1)/100))
####dilution
##step = 1
###from mpl_toolkits import mplot3d
##import matplotlib.pyplot as plt
###plt.rcParams["figure.autolayout"] = True
##fig = plt.figure()
##ax = plt.axes(projection="3d")
##ax.scatter(x[start:end:step], y[start:end:step], z[start:end:step], c='red', s=1)
###ax.plot(x[start:end:step], y[start:end:step], z[start:end:step], color='black')
##ax.plot_trisurf(x[start:end:step], y[start:end:step], z[start:end:step], linewidth = 0.2, antialiased = True)
##plt.show()
