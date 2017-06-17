# numpy

import numpy as np

# python list
array_like = [[1, 10, 100], [1, 20, 200]]

print(np.zeros([2,3]))
print(np.zeros_like(array_like))  # copy the shape
print(np.ones([2,3]))
print(np.ones_like(array_like))  # copy the shape
print(np.empty([2,3]))
print(np.empty_like(array_like))  # copy the shape

print(np.arange(10, 20, 2, np.float16))
print(np.array(array_like, np.float16))
print(type(np.array(array_like, np.float16)))  # ndarray

a = np.array(array_like, np.float16)
print(a.dtype)
print(a.size)
print(a.itemsize)  # bit / item
print(a.nbytes)  # sum bit
print(a.strides)  # bit / dim, bit / item
print(a.shape)
print(a.ndim)
print([i for i in a.flat])

# comparison
print('---comparison----')
a = np.array(array_like[0])
b = np.array(array_like[1])
c = np.array([1,1,1,1])
print(a < b)  # compare each dim and return ndarray
print(a == c)  # different dimension return 1 False

# operation
print('---operation----')
print(a >> 1)
print(a / 2)
print(a // 2)
print(-a)
print((~a).astype(np.uint8))  # bit opposite

# copy
print('---copy----')
ca = a.copy()  # create a new ndarray
print(all(ca == a))
print(ca is a)

# reshape
print('---reshape---')
ca = np.array(array_like)
print(ca)
print(np.reshape(ca, [3,2]))  # first make 1-dim vector, and then make a ndarray
print(np.resize(ca, [2,2]))  # lose data from end, first make 1-dim vector, then make a ndarray

# save and load, npy, npz, text file
#numpy.save	            numpy.load	    バイナリ	npy	非圧縮
#numpy.savetxt	        numpy.loadtxt	テキスト	 	非圧縮
#numpy.savez	        numpy.load	    バイナリ	npz	非圧縮・複数
#numpy.savez_compressed	numpy.load	    バイナリ	npz	圧縮・複数
#numpy.ndarray.tofile	numpy.fromfile	バイナリ	 	非圧縮
#numpy.ndarray.dump	    pickle.load	    バイナリ	 	非圧縮
#numpy.ndarray.dumps	pickle.loads	バイナリ	 	非ファイル保存
print('---save&load---')
np.savetxt('sample_text.txt', ca)  # loadtxt
np.savez_compressed('sample_nocompression.npz', ca)  # load
np.savez('sample_compression.npz', ca)  # load
na = np.load('sample_nocompression.npy')
print(na)



