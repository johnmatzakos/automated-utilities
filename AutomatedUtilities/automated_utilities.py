# Author: Ioannis Matzakos | Date: 25/06/2019


import time
import os
import shutil
from zipfile import ZipFile


class AutomatedUtilities:

    # setters and getters
    def setOrigin(self, origin):
        self.origin = origin

    def getOrigin(self):
        return self.origin

    def setDestination(self, destination):
        self.destination = destination

    def getDestination(self):
        return self.destination

    def setFilename(self, filename):
        self.filename = filename

    def getFilename(self):
        return self.filename

    # Getting the current timestamp (date and time) of the system at the given moment, displays it and returns it
    def getTimestamp(self):
        timestamp = time.strftime("%Y%m%d%H%M%S")
        print(f"Current Timestamp: {timestamp}")
        return timestamp

    # removing extentions from filenames
    def removeExtentions(self, string):
        index = string.find(".")
        filename = string[:index]
        filetype = string[index:]
        print(f"Filename: {filename}, Filetype: {filetype}")
        return filename, filetype

    # copy the original in order to keep it
    def copyFile(self, origin, filename):
        shutil.copyfile(origin + filename + ".xml", origin + filename + "_.xml")
        newfile = filename + "_.xml"
        print(f"Copied File: {newfile}")
        return newfile

    # If the origin directory exists then renames the file by adding the timestamp
    def addTimestamp(self, origin, newfile):
        if os.path.isdir(origin):
            # filename after rename by adding the current timestamp
            new_filename = newfile + self.getTimestamp() + ".xml"
            print(f"File renamed as: {new_filename}")

            os.rename(origin + newfile + ".xml", origin + new_filename)
            print(f"src: {origin + newfile}.xml")
            print(f"dst: {origin + new_filename}")

            return new_filename
        else:
            print("The directory does not exist. Enter a valid directory.")
            return 0

    # If the file is renamed successfully then the file is zipped using the same filename
    def zipFile(self, origin, destination, file_name):
        if os.path.isfile(origin + file_name):
            zipname = self.removeExtentions(file_name) + ".zip"
            with ZipFile(zipname,  "w") as newzip:
                newzip.write(file_name)
            print("File zipped successfully!")
            print("Zipped File: " + zipname)
            return zipname
        else:
            print("Error! File was not zipped.")
            print("The File does not exist. Enter a valid file.")
            return 0

    # If the destination directory exists then the file is moved to that directory
    def moveFile(self, file_name, destination):
        if os.path.isdir(destination):
            shutil.move(file_name, destination)
            print(f"File {file_name} moved successfully to {destination}")
        else:
            print("The directory does not exist. Enter a valid directory.")

    # delete a file
    def deleteFile(self, file, path):
        if os.path.exists(file):
            os.remove(path + file)
            print(f"File {file} deleted from {path}")
        else:
            print("The File does not exist. Enter a valid file.")

    # Normalizing paths. Checking if the paths in the arguments have the required format, with a \ at the end
    def normalizePath(self, path):
        if path[len(path)-1] != "\\" and "\\" in path:
            print("Normalizing path...")
            path = path + "\\"
        elif path[len(path) - 1] != "/" and "/" in path:
            print("Normalizing path...")
            path = path + "/"
        return path

    def add_timestamp_zip_move(self):
        self.setOrigin(self.normalizePath(input("Please enter a parent folder: ")))
        print(f"Parameter 1: {self.getOrigin()}")

        self.setDestination(self.normalizePath(input("Please enter a destination folder: ")))
        print(f"Parameter 2: {self.getDestination()}")

        self.setFilename(input("Please enter a filename: "))
        print(f"Parameter 3: {self.getFilename()}")

        # set origin  as the current working directory
        os.chdir(self.getOrigin())

        timestamp = self.getTimestamp()

        origin = self.getOrigin()
        destination = self.getDestination()
        filename = self.getFilename()

        newfile = self.copyFile(origin, filename)
        newfile = self.removeExtentions(newfile)
        new_filename = self.addTimestamp(origin, newfile)
        zippedfile = self.zipFile(origin, destination, new_filename)
        self.moveFile(zippedfile, destination)
        self.deleteFile(new_filename, origin)

    # backup files in order to keep their original state
    def backup(self):
        self.setOrigin(self.normalizePath(input("Please enter a parent folder: ")))
        origin = self.getOrigin()
        print(f"Parameter 1: {self.getOrigin()}")
        self.setFilename(input("Please enter a filename: "))
        filename = self.getFilename()
        print(f"Parameter 2: {self.getFilename()}")

        if os.path.isdir(origin):
            filename, extention = self.removeExtentions(filename)
            new_filename = filename + "_Backup" + extention
            print(f"File renamed as: {new_filename}")

            os.rename(origin + filename + extention, origin + new_filename)
            print(f"src: {origin + filename + extention}")
            print(f"dst: {origin + new_filename}")

            return new_filename
        else:
            print("The directory does not exist. Enter a valid directory.")
            return 0
