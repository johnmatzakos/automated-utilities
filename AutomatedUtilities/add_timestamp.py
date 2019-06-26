# Author: Ioannis Matzakos | Date: 25/06/2019

import sys
import os
from automated_utilities import AutomatedUtilities

print(f"Running... {sys.argv[0]}")

while(True):
    print("1.Run program")
    print("0.Exit")
    choice=input("Your choice number")
    if int(choice)==1:
        au = AutomatedUtilities()
        parent_folder=input("Please input parent folder:")
        au.setOrigin(parent_folder+"\\")
        print(f"Parameter 1: {au.getOrigin()}")
        destination_folder=input("Please input destination folder:")
        au.setDestination(destination_folder+"\\")
        print(f"Parameter 2: {au.getDestination()}")
        the_file=input("Please give the name of the file without its type")
        au.setFilename(the_file)
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
    elif int(choice)==0:
        print("Program will now exit!")
        exit()



