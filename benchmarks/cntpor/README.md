## Full SCF of Carbon Nanotube + Porphyrins

This is a simulation of a carbon nanotube with porphyrins. 

Info             | Setting
---              | ---
Calc. type       | Standard Kohn-Sham ground state (SCF)
Pseudopotentials | Ultrasoft (USP)
XC               | PBE
No. atoms        | 1532
k-points         | 1 ($\Gamma$-point)

The test can be run using:
```
mpirun pw.x -i cnt10por8.in  > cnt10por8.out
../../bin/extract.py cnt10por8.out
```
