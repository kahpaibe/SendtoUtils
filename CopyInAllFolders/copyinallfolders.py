"""Puts a copy of a specified file/folder to every subfolders of a given root.

(Folders currently are not supported.)

usage: 
copyinallfolders.py src [root]

 src               path to the source file/folder to copy
 root (optional)   path to the root containing the subfolders (DEFAULT="." (current directory) )
 """

import os
import os.path as op
import sys
import subprocess as sb

args = sys.argv

# /? help
if len(args) >= 2:
    if args[1] == "/?":
        print("""Puts a copy of a specified file/folder to every subfolders of a given root.
usage: 
copyinallfolders.py src [root]

 src               path to the source file/folder to copy
 root (optional)   path to the root containing the subfolders (DEFAULT="." (current directory) )
 """)
        exit()

# arg source
try:
    print(1)
    srcpath = op.abspath(sys.argv[1])
    print(2)
    if not (op.isdir(srcpath) or op.isfile(srcpath)):
        print(3)
        sys.exit()
    else:
        print(4)
        pass
except SystemExit:
    raise FileNotFoundError("Please enter a valid source path")
except:
    print(5)
    srcpath = op.abspath(input("Please enter a source file/folder: "))
    if not (op.isdir(srcpath) or op.isfile(srcpath)):
        raise FileNotFoundError("Please enter a valid source path")
    else:
        pass

# arg root
try:
    rootpath = op.abspath(sys.argv[2])
    if not (op.isdir(rootpath)):
        sys.exit()
    else:
        pass
except SystemExit:
    raise FileNotFoundError("Please enter a valid root path")
except:
    rootpath = op.abspath(".")

#-- subfolder list
os.chdir(rootpath)
subfolderlist = []
for elem in next(os.walk(".")):
    for fileordir in elem:
        if op.isdir(fileordir) and fileordir != ".":
            subfolderlist.append(op.join(rootpath,fileordir))
    
#-- copy
for subfolder in subfolderlist:    
    process = sb.Popen(["robocopy",op.dirname(srcpath),subfolder,op.split(srcpath)[-1],"/NP","/NJH"], stdout=sb.PIPE, universal_newlines=True)
    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(output.strip())
            break

        
os.system("pause")
