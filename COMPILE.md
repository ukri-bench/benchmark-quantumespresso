# Quantum Espresso Benchmarks

Quantum Espresso is an integrated suite of Open-Source computer codes for electronic-structure calculations and materials modeling at the nanoscale. It is based on density-functional theory, plane waves, and pseudopotentials. it features heavy use of dense linear algebra and parallelised fast Fourier transforms. 

## Compiling with Spack
This section will cover compilation with the spack build system which is commonly used to build optimised toolchains on HPC systems. It is available at <https://spack.io/>. 

You may wish to customise the spack system packages to use your own optimised versions, or alternatively, these may be specified in the spack invocation (see AMD example below).

### CPU
To build quantum espresso:

    spack install quantum-espresso+mpi+openmpi+scalapack+elpa

This will build QE with MPI and OpenMP parallelism and use ScaLAPACK/ELPA for parallelised linear algebra operations. 

There are many options that may be enabled here, and these are listed on <https://packages.spack.io/package.html?name=quantum-espresso>. 

[AMD suggest](https://www.amd.com/en/developer/zen-software-studio/applications/spack/hpc-applications-quantum-espresso.html) that you should use the following spack invocation when using the AMD compilers:
```
# Example for building Quantum-Espresso with AOCC and AOCL.
$ spack install quantum-espresso+elpa+scalapack hdf5=parallel %aocc ^amdfftw ^amdscalapack ^amdblis threads=openmp ^amdlibflame ^elpa ^openmpi fabrics=cma,ucx
```

### GPU Support
Quantum espresso supports OpenACC offloading with the possibility of OpenMP offloading in the future.

#### OpenACC
To build with OpenACC support, you must have the [Nvidia HPC SDK](https://developer.nvidia.com/hpc-sdk) installed which contains the required compilers, along with GPU-enabled math libraries. These can be installed via spack. Alternatively, the spack package configurations must be set appropriately if these have been installed manually. 

To compile the OpenACC enabled QE:
`spack install quantum-espresso %nvhpc +mpi +cuda`

If your MPI implementation has support for CUDA-aware MPI(some versions of MPICH), you may add the `+mpigpu` flag.

#### OpenMP
The OpenMP build is very much a work-in-progress and is not supported by spack, nor widely available. These instructions will be updated when this changes in the future. 

## Manual Compile 
It is also possible to build QE manually and here we give some guidance towards doing so. The steps listed here are a terse version of the main instructions from the [quantum espresso installation instructions](https://www.quantum-espresso.org/Doc/user_guide/node7.html).  

### Prerequisites
The following are a list of requirements to build Quantum Espresso from scratch. 
1. Minimal unix environment (sh, make, awk, sed)
2. CMake
3. [BLAS](http://www.netlib.org/blas/) and [LAPACK ](http://www.netlib.org/lapack/) or similar
4. Fortran 2008 standards compliant compiler.
5. [FFTW](https://www.fftw.org/)
6. An MPI-library
7. [ScaLAPACK](https://www.netlib.org/scalapack/)

It is suggested that you also have the following libraries for performance reasons, although QE can be compiled without them:
- [ELPA](https://gitlab.mpcdf.mpg.de/elpa/elpa)

Additionally, for the Nvidia/OpenACC version, you also need the [Nvidia HPC SDK](https://developer.nvidia.com/hpc-sdk). 

### Compilation with CMake
Full build instructions are given at <https://gitlab.com/QEF/q-e/-/wikis/Developers/CMake-build-system>, but we will give some brief examples for various compilers. 

#### GFortran with ELPA:
```
git clone https://gitlab.com/QEF/q-e.git
mkdir q-e/build && cd q-e/build 
cmake -DCMAKE_C_COMPILER=gcc -DCMAKE_Fortran_COMPILER=mpif90 \
-DQE_ENABLE_OPENMP=ON -DQE_ENABLE_SCALAPACK=ON -DQE_ENABLE_ELPA=ON ../
make -j all
```
#### Intel Compilers with AVX512 instructions:
```
git clone https://gitlab.com/QEF/q-e.git
mkdir q-e/build && cd q-e/build 
cmake -DCMAKE_C_COMPILER=icc -DCMAKE_C_FLAGS:STRING=-xCORE-AVX512 \
-DCMAKE_CXX_COMPILER=icpc -DCMAKE_Fortran_COMPILER=mpiifort \
-DCMAKE_Fortran_FLAGS:STRING=-xCORE-AVX512 -DQE_ENABLE_OPENMP=ON \
-DQE_ENABLE_SCALAPACK=ON -DCMAKE_BUILD_TYPE:STRING=RELWITHDEBINFO ../
make -j all
```
#### Nvidia GPU Accelerated Build with GPU-aware MPI:
```
git clone https://gitlab.com/QEF/q-e.git
mkdir q-e/build && cd q-e/build 
cmake -DCMAKE_C_COMPILER=nvc -DCMAKE_Fortran_COMPILER=mpif90 \
-DQE_ENABLE_MPI_GPU_AWARE=ON -DQE_ENABLE_CUDA=ON -DQE_ENABLE_OPENACC=ON \ 
-DQE_FFTW_VENDOR=FFTW3 -DNVFORTRAN_CUDA_VERSION=11.8 -DNVFORTRAN_CUDA_CC=80 ../
make -j all
```
Many more examples for real systems are available on the QE CMake build system page. 

### Compilation with Make
Quantum Espresso also supports an older style configure/make build which has many options that mirror the CMake versions. The main instructions for this can be found in the [quantum-espresso manual](https://www.quantum-espresso.org/Doc/user_guide/node11.html).
