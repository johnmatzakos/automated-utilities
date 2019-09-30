# Author: Ioannis Matzakos | Date: 25/06/2019


import time
import os
import shutil
import pyperclip as pyperclip
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
        shutil.copyfile(origin + filename, origin + "_".join(self.removeExtentions(filename)))
        newfile = "_".join(self.removeExtentions(filename))
        print(f"Copied File: {newfile}")
        return newfile

    # If the origin directory exists then renames the file by adding the timestamp
    def addTimestamp(self, origin, newfile):
        if os.path.isdir(origin):
            # filename after rename by adding the current timestamp
            # new_filename = ''.join(newfile[0]) + self.getTimestamp() + ".xml"
            new_filename = self.getTimestamp().join(newfile)
            print(f"File renamed as: {new_filename}")
            os.rename(origin + ''.join(newfile), origin + new_filename)
            print(f"src: {origin + ''.join(newfile)}")
            print(f"dst: {origin + new_filename}")
            return new_filename
        else:
            print("The directory does not exist. Enter a valid directory.")
            return 0

    # If the file is renamed successfully then the file is zipped using the same filename
    def zipFile(self, origin, file_name):
        if os.path.isfile(origin + file_name):
            # zipping the file given
            zipname = ''.join(self.removeExtentions(file_name)[0]) + ".zip"
            print(f"Initial zip name: {zipname}")
            with ZipFile(zipname,  "w") as newzip:
                newzip.write(file_name)
            # renaming the zip filename to follow the convention <filename_timestamp>
            temp_str = "_" + self.getTimestamp()
            zip_file_name = temp_str.join(self.removeExtentions(zipname))
            os.rename(zipname, zip_file_name)
            print("File zipped successfully!")
            print("Zipped File: " + zip_file_name)
            return zip_file_name
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

    # Copy the resulting filename to clipboard
    def copyToClipboard(self, filename):
        pyperclip.copy(filename)
        print(f"{filename} copied to clipboard successfully.")

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
            print(f"Normalizing path: {path}")
            path = path + "\\"
        elif path[len(path) - 1] != "/" and "/" in path:
            print(f"Normalizing path: {path}")
            path = path + "/"
        return path

    def add_timestamp_zip_move(self):
        print("Function running: add_timestamp_zip_move")
        # set origin  as the current working directory
        os.chdir(self.getOrigin())
        origin = self.getOrigin()
        origin = self.normalizePath(origin)
        destination = self.getDestination()
        destination = self.normalizePath(destination)
        filename = self.getFilename()
        zippedfile = self.zipFile(origin, filename)
        self.moveFile(zippedfile, destination)
        self.copyToClipboard(zippedfile)

    # backup files in order to keep their original state
    def backup(self):
        print("Function running: backup")
        origin = self.getOrigin()
        origin = self.normalizePath(origin)
        filename = self.getFilename()
        if os.path.isdir(origin):
            shutil.copyfile(origin + filename, origin + "_Backup".join(self.removeExtentions(filename)))
            new_filename = "_Backup".join(self.removeExtentions(filename))
            print(f"File backed up as: {new_filename}")
            print(f"src: {origin + filename}")
            print(f"dst: {origin + new_filename}")
            return new_filename
        else:
            print("The directory does not exist. Enter a valid directory.")
            return 0
