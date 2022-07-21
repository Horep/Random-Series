import numpy as np


n = 10**3
num = 10**3
s = 2
integer_list = np.arange(1, n+1)
recip = 1/(integer_list**s)

weights = np.exp(2*np.pi*1j*np.random.rand(num, n))
terms = np.multiply(weights, recip)
pointset = terms.sum(axis=1)
