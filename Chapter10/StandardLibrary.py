# Operating System Interface
# these commands are offen run on shell terminal
import os
os.chdir('Chapter10')
print(os.getcwd())

# this command will make the directory in current working directory
os.system('mkdir today')   # Run the command mkdir in the system shell

dir(os)
# help(os)


# For daily file and directory management tasks, the shutil module provides a higher level interface that is easier to use:
# import shutil
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')

#this will give all the file names of .py extension in the CWD
import glob
print(glob.glob('*.py'))


import sys
# it gives the command line arguments
print(sys.argv)
# stderr is used to write error warnings
sys.stderr.write('Warning, log file not found starting a new one\n')

# The most direct way to terminate a script is to use 
# sys.exit().