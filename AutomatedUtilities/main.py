# Author: Ioannis Matzakos | Date: 25/06/2019

import sys
from automated_utilities import AutomatedUtilities

print(f"Running... {sys.argv[0]}")
main = AutomatedUtilities()

function = sys.argv[1]
print(f"Parameter 1: {function}")

main.setOrigin(sys.argv[2])
print(f"Parameter 2: {main.getOrigin()}")

main.setDestination(sys.argv[3])
print(f"Parameter 3: {main.getDestination()}")

main.setFilename(sys.argv[4])
print(f"Parameter 4: {main.getFilename()}")

if function == "add_zip_move":
    main.add_timestamp_zip_move()
elif function == "backup":
    main.backup()
