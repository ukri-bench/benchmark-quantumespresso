# 64 molecules of water clusted with SCAN functional
This test looks at the performance of the latest SCAN functional on water molecules. Note, older versions of QE do not support this functionality. 

Steps to run:
```
mpirun pw.x -i water_scan.in > water_scan.out
../../bin/extract.py water_scan.out
```