import os
import cffi

ffibuilder = cffi.FFI()
header = 'beta.h'
source = 'beta.c'

with open(header) as f:
    cdef = f.read()

ffibuilder.cdef(cdef)

ffibuilder.set_source(
    '_beta',
    cdef,
    sources=[source],
    extra_compile_args=['-O3', '-march=native', '-ffast-math'])

ffibuilder.compile(verbose=True)
