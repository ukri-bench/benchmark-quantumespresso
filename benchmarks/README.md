# Benchmarks
This folder contains 5 benchmarks testing common density functional theory calculation types. These are taken from real scientific applications and are representative of calculations that people will perform.

Each of the benchmark folders contains instructions on how to run it, as well as to run the analysis script to check the answer and report the QE wallclock time.

There are also reference output files (.ref) in each folder with the expected output of these calculations.

## List of tests:
- [ausurf](ausurf/README.md) - Gold surface, 112 atoms (Au). Standard PBE SCF calculation, USP potentials, with 2 k-points.
- [cntpor](cntpor/README.md) - Carbon nanotube with porphyrins, 1532 atoms (C,N,O,H). Standard PBE SCF calculation, USP potentials, with 1 k-point (Gamma-point).
- [cri3](cri3/README.md) - CrI3, a 2d spintronics material, 960 atoms (Cr,I). Two-stage calculation, LDA, USP potentials, with 3 k-points.
- [grir33](grir33/README.md) - Graphene on an iridium slab, 443 atoms (C,Ir). Standard PBE SCF calculation, PAW potentials, with 4 k-points.
- [water_scan](water_scan/README.md) - Water molecules using the SCAN functional, 192 atoms (H,O). Standard SCAN SCF calculation, USP potentials, with 1 k-point (Gamma-point)..

