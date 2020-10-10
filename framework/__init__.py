import os

## To enable to import 'Leaky-LWE-Estimator' as a module with the instruction
#    from leaky_lwe_estimator.framework import ...

# Keep in mind the original working directory
_cname = os.getcwd()

# Define the right working directory for the module
_abspath = os.path.abspath(__file__)
_dname = os.path.dirname(_abspath)
os.chdir(_dname)

# Import the module
from sage.all_cmdline import *
_sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_2 = Integer(2); _sage_const_4 = Integer(4); _sage_const_16 = Integer(16); _sage_const_8 = Integer(8); _sage_const_3 = Integer(3)
load("instance_gen.sage")

# Come back with the original working directory
os.chdir(_cname)
