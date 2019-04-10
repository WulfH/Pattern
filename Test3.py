from Pattern import Pattern
import numpy as np
import matplotlib.pyplot as plt

test=Pattern(5,5)
test.set(np.array([[0,0,0,5,0],[5,0,0,0,0],[5,5,0,5,5],[0,5,0,0,5],[0,5,0,5,0]]))
A=test.get()
B=test.autocor()

test.mirror(1)
C=test.get()
D=test.autocor()

test.evolve("mean")
E=test.get()
F=test.autocor()

plt.subplot(231)
plt.imshow(A, cmap='hot', interpolation='nearest')
plt.subplot(234)
plt.imshow(B, cmap='hot', interpolation='nearest')
plt.subplot(232)
plt.imshow(C, cmap='hot', interpolation='nearest')
plt.subplot(235)
plt.imshow(D, cmap='hot', interpolation='nearest')
plt.subplot(233)
plt.imshow(E, cmap='hot', interpolation='nearest')
plt.subplot(236)
plt.imshow(F, cmap='hot', interpolation='nearest')
plt.show()

