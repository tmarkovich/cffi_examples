import os
import cffi

ffibuilder = cffi.FFI()
sourcefile = os.path.join('.', 'dot.h')
source = os.path.join('.', 'dot.c')

with open(sourcefile) as f:
    ffibuilder.cdef(f.read())

ffibuilder.set_source(
    '_dot',
    '#include "{0}"'.format(sourcefile),
    sources=[source],
    library_dirs=['.'],
    extra_compile_args=['-O3', '-march=native', '-ffast-math'])

ffibuilder.compile(verbose=True)
