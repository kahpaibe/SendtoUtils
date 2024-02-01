import os
import sys
import os.path as op
import subprocess as sb

#-- init
filelist = []

#-- list all files
for objects in next(os.walk(".")):
    for fileordir in objects:
        filelist.append(fileordir)
filelist.pop(0) #removes "." path

#-- print file list to overwrite:
fileliststr = ""
for elem in filelist:
    fileliststr = fileliststr + elem + ":"
print(fileliststr[:-1])


newraw = input("New list= ")
newfilelist = newraw.split(":")

if len(newfilelist) != len(filelist):
    print("INVALID FORMAT: PLEASE ENTER THE SAME NUMBERS OF FILES")
else: 
    print("Renaming...")
    for index in range(len(newfilelist)):
        command = ["Ren",filelist[index],newfilelist[index]]
        process = sb.Popen(command, stdout=sb.PIPE, shell=True, universal_newlines=True)
