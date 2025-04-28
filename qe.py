"""ReFrame benchmark for QuantumESPRESSO"""
import os
from typing import TypeVar

import reframe as rfm
import reframe.utility.sanity as sn
from reframe.core.builtins import (performance_function, run_after, run_before,
                                   sanity_function)
from reframe.core.exceptions import SanityError
from reframe.core.parameters import TestParam as parameter
from reframe.core.variables import TestVar as variable
from benchmarks.modules.utils import SpackTest
import os.path as path


R = TypeVar('R')

class QEspressoPWCheckBase(SpackTest):
    """QuantumESPRESSO benchmark test.

    `QuantumESPRESSO <https://www.quantum-espresso.org/>`__ is an integrated
    suite of Open-Source computer codes for electronic-structure calculations
    and materials modeling at the nanoscale.

    This tests aims at measuring the scalability of the pw.x executable, in
    particular the FFT and diagonalization algorithms, by running a simple
    silicon calculation with high `ecut` (increases size of FFTs) and `nbnd`
    (increases size of matrices to diagonalize) values."""

    valid_systems=['*']
    valid_prog_environs = ['default']

    # The following is a standard cpu build:
    spack_spec = 'quantum-espresso@7.3.1 +mpi'

    # This will generate a working cuda-enabled mpi build on nvidia:
    #spack_spec = 'quantum-espresso@7.3.1 %nvhpc +mpi +cuda ^openblas ^fftw' 

    time_limit = '200m'
        
    tags = {'sciapp', 'chemistry'}
    descr = 'QuantumESPRESSO pw.x benchmark'

    @run_before('setup')
    def setup_folders_and_input(self):
        self.sourcesdir = path.join(path.dirname(__file__), self.inputdir)
        self.executable_opts = ["-in", self.inputfile]

    @run_after('setup')
    def setup_num_tasks(self):
        self.env_vars['OMP_NUM_THREADS'] = 1
        self.env_vars['OMP_PLACES'] = 'cores'
    
    @staticmethod
    @sn.deferrable
    def extractsingle_or_val(*args, on_except_value: str = '0s') -> str:
        """Wrap extractsingle_or_val to return a default value if the regex is
        not found.

        Returns:
            str: The value of the regular expression
        """
        try:
            res = sn.extractsingle(*args).evaluate()
        except SanityError:
            res = on_except_value

        return res

    @staticmethod
    @sn.deferrable
    def convert_timings(timing: str) -> float:
        """Convert timings to seconds"""

        if timing is None:
            return 0

        days, timing = (['0', '0'] + timing.split('d'))[-2:]
        hours, timing = (['0', '0'] + timing.split('h'))[-2:]
        minutes, timing = (['0', '0'] + timing.split('m'))[-2:]
        seconds = timing.split('s')[0]

        return (
            float(days) * 86400 +
            float(hours) * 3600 +
            float(minutes) * 60 +
            float(seconds)
        )

    @performance_function('s')
    def extract_report_time(self, name: str = None, kind: str = None) -> float:
        """Extract timings from pw.x stdout

        Args:
            name (str, optional): Name of the timing to extract.
                                  Defaults to None.
            kind (str, optional): Kind ('cpu' or 'wall) of timing to extract.
                                  Defaults to None.

        Raises:
            ValueError: If the kind is not 'cpu' or 'wall'

        Returns:
            float: The timing in seconds
        """
        if kind is None:
            return 0
        kind = kind.lower()
        if kind == 'cpu':
            tag = 1
        elif kind == 'wall':
            tag = 2
        else:
            raise ValueError(f'unknown kind: {kind}')

        # Possible formats
        #       PWSCF        :   4d 6h19m CPU  10d14h38m WALL
        # --> (Should also catch spaces)
        return self.convert_timings(
            self.extractsingle_or_val(
                fr'{name}\s+:\s+(.+)\s+CPU\s+(.+)\s+WALL',
                self.stdout, tag, str
            ))

    @run_before('performance')
    def set_perf_variables(self):
        """Build a dictionary of performance variables"""

        timings = [
            'PWSCF', 'electrons', 'c_bands', 'cegterg', 'calbec',
            'fft', 'ffts', 'fftw'
        ]
        for name in timings:
            for kind in ['cpu', 'wall']:
                res = self.extract_report_time(name, kind)
                self.perf_variables[f'{name}_{kind}'] = res

    @sanity_function
    def assert_job_finished(self):
        """Check if the job finished successfully"""
        return sn.assert_found(r'JOB DONE', self.stdout)

# Specification for tests to run
    
@rfm.simple_test    
class QEspressoPWcheckBasic(QEspressoPWCheckBase):
    """
    The basic 2 atom Si2 test. This does not scale up at all, but is useful for testing"
    """
    tags = {'quick','sciapp', 'chemistry'}
    descr = 'QuantumESPRESSO pw.x benchmark'
    inputfile = "Si.scf.in"
    inputdir = "Si-basic"
    executable = 'pw.x'
    num_tasks = 2
    
@rfm.simple_test    
class QEspressoPWcheckZrO(QEspressoPWCheckBase):
    """
    Big ZrO test
    """
    tags = {'sciapp', 'chemistry'}
    descr = 'QuantumESPRESSO pw.x benchmark'
    inputfile = "ZrO2.in"
    inputdir = "ZrO2"
    executable = 'pw.x'
    num_tasks = 256
