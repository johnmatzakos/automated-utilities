# Author: Ioannis Matzakos | Date: 27/06/2019


import sys
import os
from automated_utilities import AutomatedUtilities


print(f"Running... {sys.argv[0]}")
backup = AutomatedUtilities()
origin = backup.setOrigin(sys.argv[1])
print(f"Parameter 1: {backup.getOrigin()}")
filename = backup.setFilename(sys.argv[2])
