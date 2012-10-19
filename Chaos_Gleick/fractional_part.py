"""
Source: "Smale could be happy with an example like this: take a number,
a fraction between zero and one, and double it. Then drop the integer part, the
part to the left of the decimal point. Then repeat the process"
-Page 66

Gleick, James. "Life's Ups and Downs." Chaos: Making a New Science.
New York, N.Y., U.S.A.: Viking, 1987. 1-340. Print.

"""
import numpy as np
import matplotlib.pyplot as mp
N=1000;
rand = np.random.rand(1)
X,Y = np.arange(N),np.concatenate((np.random.rand(1),np.arange(1,N)));
for i in xrange(1,np.size(Y)):
    Y[i] = (2*Y[i-1])%1
mp.plot(X,Y,'bo')
mp.show()

