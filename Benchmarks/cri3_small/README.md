# CrI3 supercell

This is a supercell of CrI3 which is often used in spintronics

This is calculation in two stages:
  1. Collinear spin-polarized SCF calculation 
  2. One shot non-collinear + spin-orbit total energy calculation with density of previous step. 

## Steps to run

```
mpirun pw.x -nk 3 -i cri3-small_collinear.in  > cri3-colinnear.out
mpirun pw.x -nk 3 -i cri3-small.in  > cri3-noncollinear.out
../bin/extract cri3-noncollinear.out
```
