# CrI3 supercell

This is calculation in two stages:
  1. Collinear spin-polarized SCF calculation 
  2. One shot non-collinear + spin-orbit total energy calculation with density of previous step. 

## Steps to run

mpirun pw.x -nk 3 -i cri3-small_collinear.in  > out_collinear
mpirun pw.x -nk 3 -i cri3-small.in  > out_nc