#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date
# to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?)
       ((0|1)?\d)-
       ((0|1|2|3)?\d)-
       ((19|20)\d\d)
       (.*?)$
       """, re.VERBOSE)
k=re.compile()
    # Loop over the files in the working directory.
for filenames in os.listdir('../k'):
    l=datePattern.search(filenames)
    print(filenames)

   #TODO: Skip files without a date.
    if l == None:
        continue

    else:
        #TODO: Get the different parts of the filename.
        pre = l.group(1)
        month = l.group(2)
        day = l.group(3)
        year = l.group(4)
        post = l.group(5)

        #TODO: Form the European-style filename.
        new=pre+day+'-'+month+'-'+year+post
        #TODO: Rename the files.
        shutil.move(filenames,new)
