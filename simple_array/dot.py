from _dot.lib import dot
from cffi import FFI
import numba
import numpy as np
import random
import time

ffi = FFI()

N = 10000
len_x = 100000

diff = 0.
for _ in range(N):
    x = np.random.rand(len_x)
    y = np.random.rand(len_x)
    start = time.time()
    a = np.dot(x, y)
    end = time.time()
    diff += (end - start)
print("Using np.dot")
print(diff)

@numba.jit(nopython=True)
def fn(x, y):
    a = np.dot(x, y)

diff = 0.
for _ in range(N):
    x = np.random.rand(len_x)
    y = np.random.rand(len_x)
    start = time.time()
    a = fn(x, y)
    end = time.time()
    diff += (end - start)
print("Using numba with np.dot")
print(diff)

diff = 0.
for _ in range(N):
    x = np.random.rand(len_x)
    y = np.random.rand(len_x)
    start = time.time()
    a = dot(ffi.cast('double *', x.ctypes.data), len_x,
            ffi.cast('double *', y.ctypes.data), len_x)
    end = time.time()
    diff += (end - start)
print("Using CFFI with ffi.cast included in fn call")
print(diff)

diff = 0.
for _ in range(N):
    x = ffi.cast('double *', np.random.rand(len_x).ctypes.data)
    y = ffi.cast('double *', np.random.rand(len_x).ctypes.data)
    start = time.time()
    a = dot(x, len_x, y, len_x)
    end = time.time()
    diff += (end - start)
print("Using CFFI with ffi.cast excluded in fn call")
print(diff)

def rand_init_array(arr):
    for i in range(len(arr)):
        arr[i] = random.random()
    return arr

def allocate(typ, N, init_array=None):
    if init_array is None:
        return ffi.new("{d}[{N}]".format(d=typ, N=N))
    else:
        return ffi.new("{d}[{N}]".format(d=typ, N=N), init_array)

diff = 0.
for _ in range(N):
    x = rand_init_array([0]  * len_x)
    y = rand_init_array([0]  * len_x)
    start = time.time()
    a = dot(x, len_x, y, len_x)
    end = time.time()
    diff += (end - start)
print("Using CFFI with a python array passed in")
print(diff)

diff = 0.
for _ in range(N):
    x = rand_init_array(allocate('double', len_x))
    y = rand_init_array(allocate('double', len_x))
    start = time.time()
    a = dot(x, len_x, y, len_x)
    end = time.time()
    diff += (end - start)
print("Using CFFI with explicit cffi memory allocation")
print(diff)

# diff = 0.
# for _ in range(N):
    # x = rand_init_array(allocate('double', len_x))
    # y = rand_init_array(allocate('double', len_x))
    # start = time.time()
    # a = dot(x, len_x, y, len_x)
    # end = time.time()
    # diff += (end - start)
# print(diff)
