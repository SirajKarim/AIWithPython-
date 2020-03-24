import numpy as np
import matplotlib.pyplot as pt
from sklearn.neighbors import KNeighborsClassifier

xblue=[0.3,0.5,1]
yblue=[1,4.5,2.3]

xred=[3.3,3.5,4]
yred=[7,1.5,6.3]

x=np.array([[0.3,1],[0.5,4.5],[1,2.3]])
y=([0,0,0,1,1,1])

pt.plot(xblue,yblue,'ro',color='blue')
pt.plot(xred,yred,'ro',color='red')
pt.plot(3,5,'ro',color='green',markersize=15)
pt.axis([-0.5,10,-0.5,10])
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(x,y)

pred=classifier.predict(np.array([[5,5]]))
print(pred)

pt.show()