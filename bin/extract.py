import argparse
import re
from collections import namedtuple
from pathlib import Path

parser = argparse.ArgumentParser(
    prog='extract.py',
    description='Extracts the total energy and some timing information from a Quantum Espresso run. Verifies the total energy against an expected value. ')
parser.add_argument("filename", help="Output file to parse")
parser.add_argument("-r", "--reference", help="Reference file to compare against and validate output")
parser.add_argument("-s", "--short", action='store_true', help="Only print the time in seconds and nothing else.")
args = parser.parse_args()


# Generate regexes
energy_re = re.compile(r"! *total energy *= *(\S*) Ry")
time_re = re.compile(r" *PWSCF *: *(\S+)s CPU *(\S+)s WALL *")
input_re = re.compile(r" *Reading input from (\S+)")

QERun = namedtuple("QERun", ["filename", "total_energy", "wall_time", "input_file"])

def parse_file(filename: str) -> QERun:
    # Scan file
    with open(filename) as fd:
        for line in fd:
            if m := energy_re.match(line):
                energy_str = m.group(1)
                total_energy = float(energy_str)
            elif m := time_re.match(line):
                time_str = m.group(2)
                wall_time = float(time_str)
            elif m := input_re.match(line):
                input_file = m.group(1)
    return QERun(filename=filename, total_energy=total_energy, wall_time=wall_time, input_file=input_file)

# Verify output file exists
if not Path(args.filename).is_file():
    msg = f"{args.filename} does not exist!"
    raise FileNotFoundError(msg)

# Parse the file
calc_values = parse_file(args.filename)

# Find a reference file
if args.reference:
    ref_file = args.reference
else:
    ref_file = calc_values.input_file + ".ref"

# Check it exists
if not Path(ref_file).is_file():
    msg = f"Reference file {ref_file} does not exist! Specify it manually with --reference"
    raise FileNotFoundError(msg)

# Parse it
ref_values = parse_file(ref_file)

# Check energy values are "close"
delta_energy = (calc_values.total_energy-ref_values.total_energy) / ref_values.total_energy

if abs(delta_energy) > 1e-6:
    msg = f"Calculated total energy ({calc_values.total_energy} Ry) did not match reference total energy value ({ref_values.total_energy} Ry). The difference in values was {100.*abs(delta_energy):.4f}% > 1e-4"
    raise ValueError(msg)

if args.short:
    print(calc_values.wall_time)
else:
    print(f"Passed verification test with a total time {calc_values.wall_time} s")