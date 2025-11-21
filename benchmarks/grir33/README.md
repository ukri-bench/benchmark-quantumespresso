# Graphene on Iridium slab
This is a layer of C on one side of an Ir block.

Steps to run:

```
mpirun pw.x -i grir433.in > grir.out
../bin/extract grir.out
```