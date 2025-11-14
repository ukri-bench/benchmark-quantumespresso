# 64 molecules of water clusted with SCAN functional

* 256 bands and 4.5X10^6 plane waves
* metaGGA SCAN Functional taken from libxc, in order perform the test it is necessary to compile the program 
  linking with libxc v> 5.0 compatible only with qe version > 7.3 
    

mpirun pw.x -i water_scan.in > water_scan.out