import os
import cffi

ffibuilder = cffi.FFI()
sourcefile = 'beta.h'
source = 'beta.c'

with open(sourcefile) as f:
    ffibuilder.cdef(f.read())

ffibuilder.set_source(
    '_beta',
    '#include "{0}"'.format(sourcefile),
    sources=[source],
    include_dirs=['.'],
    extra_compile_args=['-O3', '-march=native', '-ffast-math'])

ffibuilder.compile(verbose=True)
