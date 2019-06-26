# Author: Ioannis Matzakos | Date: 25/06/2019

import sys
import os
from automated_utilities import AutomatedUtilities

print(f"Running... {sys.argv[0]}")

au = AutomatedUtilities()

au.setOrigin(sys.argv[1])
print(f"Parameter 1: {au.getOrigin()}")

au.setDestination(sys.argv[2])
print(f"Parameter 2: {au.getDestination()}")

au.setFilename(sys.argv[3])
print(f"Parameter 3: {au.getFilename()}")

# set origin  as the current working directory
os.chdir(au.getOrigin())

timestamp = au.getTimestamp()

origin = au.getOrigin()
destination = au.getDestination()
filename = au.getFilename()

newfile = au.copyFile(origin, filename)
newfile = au.removeExtentions(newfile)
new_filename = au.addTimestamp(origin, newfile)
zippedfile = au.zipFile(origin, destination, new_filename)
au.moveFile(zippedfile, destination)
au.deleteFile(new_filename, origin)
