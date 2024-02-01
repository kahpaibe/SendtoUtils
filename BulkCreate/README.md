# bulkcreate.py
A small utility to create several files or folders with a given name scheme.

usage: 
    bulkcreate.py \[root\]
    root (optional)   path to create objects in
Options:    
    - select whether to create files or folders
    - select naming mode ([regexp,list])
        ＊ regexp mode:
            + set name template: (use ":" semicolon char to simbolize a digit to be substitued)
            + enable or not forcing "0" (TRUE: "01", FALSE: "1")
            + set number of objects to create
        ＊ list
            + set the list of names. FORMAT = "name1:name2:name3"
