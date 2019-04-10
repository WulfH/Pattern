from Pattern import Pattern
import matplotlib.pyplot as plt

test=Pattern(20,20)
test.create("chess",2)
A=test.get()
B=test.autocor()

test.create("rand",10)
C=test.get()
D=test.autocor()

test.evolve("cluster")
test.evolve("cluster")
test.evolve("cluster")
E=test.get()
F=test.autocor()

test.mirror(0)
test.mirror(1)
G=test.get()
H=test.autocor()

plt.subplot(241)
plt.imshow(A, cmap='hot', interpolation='nearest')
plt.subplot(245)
plt.imshow(B, cmap='hot', interpolation='nearest')
plt.subplot(242)
plt.imshow(C, cmap='hot', interpolation='nearest')
plt.subplot(246)
plt.imshow(D, cmap='hot', interpolation='nearest')
plt.subplot(243)
plt.imshow(E, cmap='hot', interpolation='nearest')
plt.subplot(247)
plt.imshow(F, cmap='hot', interpolation='nearest')
plt.subplot(244)
plt.imshow(G, cmap='hot', interpolation='nearest')
plt.subplot(248)
plt.imshow(H, cmap='hot', interpolation='nearest')
plt.show()

