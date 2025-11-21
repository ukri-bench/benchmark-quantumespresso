## Au surface test 

This is a supercell representing an infinite 2d gold surface exposed to vacuum. 

The test can be run using:
`
mpirun pw.x -nk 2 -i ausurf.in  > ausurf.out
../../bin/extract.py ausurf.out
`
