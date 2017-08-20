from _beta.lib import beta_logpdf, nop
import numba
from scipy.stats import beta
import time

N = 1000000
start = time.time()
for i in range(N):
    a = beta.logpdf(i, 1, 2)
end = time.time()
print(end - start)

start = time.time()
a = beta.logpdf(list(range(N)), 1, 2)
end = time.time()
print(end - start)

start = time.time()
for i in range(N):
    a = beta_logpdf(1, 2, i)
end = time.time()
print(end - start)

start = time.time()
for i in range(N):
    a = nop(1, 2, i)
end = time.time()
print(end - start)

@numba.jit(nopython=True)
def fn():
    for i in range(N):
        a = beta.logpdf(i, 1, 2)

# Numba appears to fail here. Uncomment if you'd like to try
# @numba.jit(nopython=True)
# def fn_array():
    # a = beta.logpdf(list(range(N)), 1, 2)

# start = time.time()
# fn()
# end = time.time()
# print(end - start)

# start = time.time()
# fn_array()
# end = time.time()
# print(end - start)
