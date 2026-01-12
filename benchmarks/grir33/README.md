# Graphene on Iridium slab

This is a graphene layer on one side of an iridium slab.

Info             | Setting
---              | ---
Calc. type       | Standard Kohn-Sham ground state (SCF)
Pseudopotentials | Projector-Augmented Wave (PAW)
XC               | PBE
No. atoms        | 443
k-points         | 4 ($\Gamma$-point)

Steps to run:

```
mpirun pw.x -i grir433.in > grir.out
../bin/extract grir.out
```