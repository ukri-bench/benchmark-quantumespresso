## Au surface test 

This is a supercell representing an infinite 2d gold surface exposed to vacuum.

Info             | Setting
---              | ---
Calc. type       | Standard Kohn-Sham ground state (SCF)
Pseudopotentials | Ultrasoft (USP)
XC               | PBE
No. atoms        | 112
k-points         | 2

The test can be run using:
```
mpirun pw.x -nk 2 -i ausurf.in  > ausurf.out
../../bin/extract.py ausurf.out
```
