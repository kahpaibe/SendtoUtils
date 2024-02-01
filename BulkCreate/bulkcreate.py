"""Bulk create files or folders.
usage: 
    bulkcreate.py [root folder]
    
     root folder (optional)   path to create objects in
Options:    
    - select whether to create files or folders
    - select naming mode ([regexp,list])
        ＊ regexp mode:
            + set name template: (use ":" semicolon char to simbolize a digit to be substitued)
            + enable or not forcing "0" (TRUE: "01", FALSE: "1")
            + set number of objects to create
        ＊ list
            + set the list of names. FORMAT = "name1:name2:name3"
 """

import os
import os.path as op
import sys
import subprocess as sb
import numpy as np

args = sys.argv

# /? help
if len(args) >= 2:
    if args[1] == "/?":
        print("""Bulk create files or folders.
usage: 
    bulkcreate.py [root]
    
     root (optional)   path to create objects in
Options:    
    - select whether to create files or folders
    - select naming mode ([regexp,list])
        ＊ regexp mode:
            + set name template: (use ":" semicolon char to simbolize a digit to be substitued)
            + enable or not forcing "0" (TRUE: "01", FALSE: "1")
            + set number of objects to create (from 1 to N)
        ＊ list
            + set the list of names. FORMAT = "name1:name2:name3"
 """)
        exit()

# arg root
try:
    rootpath = op.abspath(sys.argv[1])
    if not (op.isdir(rootpath)):
        sys.exit()
    else:
        pass
except SystemExit:
    raise FileNotFoundError("Please enter a valid root path")
except:
    rootpath = op.abspath(input("Please enter a root folder: \n"))
    if not (op.isdir(rootpath)):
        raise FileNotFoundError("Please enter a valid root path")

# choose mode
while True:
    mode = input("Please select a mode: regexp, list\n")
    
    if mode in ["regexp","list"]: #if valid mode
        break
    else:
        print("Invalid mode!") #invalid mode

# choose type
while True:
    objecttype = input("Please select a type: file, folder\n")
    
    if objecttype in ["file","folder"]: #if valid mode
        break
    else:
        print("Invalid type!") #invalid mode

#creating objlist
print("Will create",objecttype+"s","in",rootpath,"using",objecttype)
if mode == "list":
    #--- list mode
    rawlist=input("Please enter a list of "+objecttype+"s: (separator=\":\")\n")
    objlist = rawlist.split(":")
if mode == "regexp":
    #--- regexp mode
    #template
    template = input("Please enter a name template: (use \":\" for numbers)\n")
    
    #force?
    while True:
        rawforce = input('Force "0"? (write "01" instead of "1"), please enter True or False\n')
        if rawforce == "True":
            boolforce = bool(rawforce)
            break
        elif rawforce == "False":
            boolforce = bool(rawforce)
            break
        else:
            print("Invalid boolean. Please try again.")
    
    # number of objects
    while True:
        rawnum = input('Please enter the number N>0 of objects to create (from 1 to N):')
        try:
            N = int(rawnum)
            if N > 0:
                pass
            else:
                raise ValueError
            break
        except:
            print("Invalid number. Please try again.")
    
    # creating the list
    objlist = []
    digofN = int( np.log10(N) ) +1
    for k in range(1,N+1):
        strnum = str(k)
        if boolforce: #if boolforce
            digofk = int( np.log10(k) ) +1
            strnum = "0"*(digofN-digofk)+str(k)
                
            
        objlist.append( template.replace(":", strnum) )
    
# creating objects
print("Creating",objecttype+"s:")
os.chdir(rootpath)
if objecttype == "file":
    for f in objlist:
        print("Creating",f)
        openfile = open(f,"a+")
        openfile.close()
elif objecttype == "folder":
    for f in objlist:
        print("Creating",f)
        try:
            os.mkdir(f)
        except:
            pass
