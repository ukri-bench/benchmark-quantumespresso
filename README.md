# Living Benchmark for Quantum Espresso

## Introduction
This set of benchmarks tests the performance of the core program "PWSCF" of the materials modelling suite Quantum Espresso. Quantum Espresso uses density functional theory with a plane-wave (Fourier) basis, and iteratively solves the Kohn-Sham equations with a matrix-free method.

Key computational kernels are 3D FFTs and dense linear algebra (matrix-matrix multiplication, inversion and diagonalisation). When run in parallel, the 3D FFTs may be implemented as 2D and/or 1D FFTs, depending on the decomposition.

Parallel communication between nodes/devices uses MPI, including all-to-all communications. GPU offloading is via OpenACC.

This repo is part of the UKRI Living Benchmarks project. These tests should cover FFTs, MPI and linear algebra. 

## Maintainers

[@pjpbyrne](https://github.com/pjpbyrne),
[@pjh503](https://www.github.com/pjh503)

## Overview

### Main code/library

[Quantum Espresso](https://www.quantum-espresso.org/download/software/)

### Architectures

CPU, GPU.

### Languages and programming models

Fortran, OpenACC, MPI.

### Seven 'dwarfs'

- [x] Dense linear algebra
- [ ] Sparse linear algebra
- [x] Spectral methods
- [ ] N-body methods
- [ ] Structured grids
- [ ] Unstructured grids
- [ ] Monte Carlo

## Building

The benchmark can be built using Spack or manually using CMake. The full instructions to compile Quantum Espresso are covered in the [compilation instructions](COMPILE.md), but in brief, it can be compiled easily with spack:

`spack install quantum-espresso+openmp+mpi+scalapack`

will give a basic QE built with somewhat sensible options. 

## Usage

Each of the folders in benchmark contains one test and these can generally be run with

```
mpirun -np <number of processors> pw.x -i <input file> > <output file>
../../bin/extract.py <output file>
```

Further instructions are in the [benchmarks folder](benchmarks/README.md)

## Results
At the end of the run, a set of timings will be presented for each calculation:
```
P: PWSCF_cpu: 6.39 s (r:0, l:None, u:None)
P: PWSCF_wall: 6.45 s (r:0, l:None, u:None)
P: electrons_cpu: 5.75 s (r:0, l:None, u:None)
P: electrons_wall: 5.8 s (r:0, l:None, u:None)
P: c_bands_cpu: 4.61 s (r:0, l:None, u:None)
P: c_bands_wall: 4.65 s (r:0, l:None, u:None)
P: cegterg_cpu: 4.32 s (r:0, l:None, u:None)
P: cegterg_wall: 4.36 s (r:0, l:None, u:None)
P: calbec_cpu: 0.16 s (r:0, l:None, u:None)
P: calbec_wall: 0.16 s (r:0, l:None, u:None)
P: fft_cpu: 0.21 s (r:0, l:None, u:None)
P: fft_wall: 0.21 s (r:0, l:None, u:None)
P: ffts_cpu: 0.0 s (r:0, l:None, u:None)
P: ffts_wall: 0.0 s (r:0, l:None, u:None)
P: fftw_cpu: 3.63 s (r:0, l:None, u:None)
P: fftw_wall: 3.66 s (r:0, l:None, u:None)
```

The first numbers are the total seconds of CPU and wallclock time. 
