# Author: Ioannis Matzakos | Date: 25/06/2019


import sys
from automated_utilities import AutomatedUtilities


print(f"Running... {sys.argv[0]}")
main = AutomatedUtilities()
while(True):
    print("1.Add timestamp to filename")
    print("2.Backup files")
    print("0.Exit")
    choice=input("Select functionality: ")
    if int(choice) == 1:
        main.add_timestamp_zip_move()
    elif int(choice) == 2:
        main.backup()
    elif int(choice) == 0:
        print("Program will now exit!")
        exit()
