import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import copy

class Pattern:
	def __init__(self, x, y):
		self.pat=np.zeros((x,y))
#		self.x=x; self.y=y;
	def get(self):
		return copy.copy(self.pat)
	def set(self, A):
		self.pat=copy.copy(A)
	def map(self):
		plt.imshow(self.pat, cmap='hot', interpolation='nearest')
		plt.show()
	def create(self, pattern, n=2):
		if pattern=="rand":
			self.pat=np.random.randint(n, size=self.pat.shape)
		elif pattern=="chess":
			for (i,j) in np.ndindex(self.pat.shape):
				self.pat[i,j]=(i+j)%n
	def evolve(self, pattern):
		if pattern=="cluster":
			A=np.full(tuple(map(sum, zip(self.pat.shape,(2,2)))), np.nan)
			A[1:-1,1:-1]=self.pat
			for (i,j) in np.ndindex(self.pat.shape): #stats.mode works slow and strange
				self.pat[i,j]=stats.mode(A[i:i+3,j:j+3], axis=None, nan_policy="omit")[0]
		elif pattern=="mean":
			A=np.full(tuple(map(sum, zip(self.pat.shape,(2,2)))), np.nan)
			A[1:-1,1:-1]=self.pat
			for (i,j) in np.ndindex(self.pat.shape):
				self.pat[i,j]=int(np.nanmean(A[i:i+3,j:j+3]))

	def mirror(self, ax):
		x,y=self.pat.shape
		x=int(x/2); y=int(y/2)
		if ax==0:
			self.pat[-x:,:]=self.pat[x-1::-1,:]
		elif ax==1:
			self.pat[:,-y:]=self.pat[:,y-1::-1]
	def autocor(self):
		A=np.zeros(self.pat.shape)
		for (i,j) in np.ndindex(self.pat.shape):
			B=np.roll(self.pat, i, axis=0)
			B=np.roll(B, j, axis=1)
			A[i,j]=np.sum(np.absolute(self.pat-B))
		return A
