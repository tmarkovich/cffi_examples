import os
import cffi

ffibuilder = cffi.FFI()
sourcefile = os.path.join('.', 'beta.h')
source = os.path.join('.', 'beta.c')

with open(sourcefile) as f:
    ffibuilder.cdef(f.read())

ffibuilder.set_source(
    '_beta',
    '#include "{0}"'.format(sourcefile),
    sources=[source],
    library_dirs=['.'],
    extra_compile_args=['-O3', '-march=native', '-ffast-math'])

ffibuilder.compile(verbose=True)
