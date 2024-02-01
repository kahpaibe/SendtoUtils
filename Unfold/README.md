# Unfold.bat
"Unfold" the content of every selected folder to a common folder.

Exemple, selecting the root folders of this tree:
 \Folder1\
          \File1.txt
 \Folder2\
          \subfolder2\
                     \File3.txt
          \File2.txt
 \Folder3\
          \File4.txt

will create a new folder:
 \@Unfold\
          \File1.txt
          \File2.txt
          \File4.txt
          \subfolder2\
                     \File3.txt
