# Living Benchmark for Quantum Espresso

## Introduction
This is a repo for the living benchmarks quantum espresso tests. These tests should cover FFTs, MPI and linear algebra. 

## Requirements
- Spack
- Reframe

## Usage

### Config
A reframe config should be generated for the machine in question and then set using
    export RFM_CONFIG_FILES=<path to config file>
An example for the existing UK HPC machines is given in reframe_config.example.py

You may also need to tell reframe to use login shells to correctly find the spack executable
    export RFM_USE_LOGIN_SHELL="true"

### Building and running the tests

The simple test can be run locally using
    reframe -c ./qe.py -r -t quick

The full tests can be run using
    reframe -c ./qe.py -r

The ZrO2 case can take a large amount of time to run.

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