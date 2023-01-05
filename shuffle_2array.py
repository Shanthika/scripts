import numpy as np 
import argparse 



def shuffle(a,b):
	randomize = np.arange(len(a))
	np.random.shuffle(randomize)
	a = a[randomize]
	b = b[randomize]

	return a,b


if __name__ == '__main__':


	a = np.array([[1,2,3],[3,4,5],[1,2,5]])
	b = np.array([[1,2,3],[3,4,5],[1,2,5]])
	a,b = shuffle(a,b)
	print(a,b)