# Operating System Interface...
# Imports in this file: os - glob - sys - re - math - random - statictics
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
# it takes the command line arguments (sys.argv)
print(sys.argv)
# stderr is used to write error warnings
sys.stderr.write('Warning, log file not found starting a new one\n')

# The most direct way to terminate a script is to use 
# sys.exit().


# The argparse module provides a more sophisticated mechanism to process command line arguments. The following script extracts one or more filenames and an optional number of lines to be displayed
# import argparse

# parser = argparse.ArgumentParser(
#     prog='top',
#     description='Show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)

# When run at the command line with python top.py --lines=5 alpha.txt beta.txt, the script sets args.lines to 5 and args.filenames to ['alpha.txt', 'beta.txt'].


#STRING PATTERN MATCHING
# re module (Regular Expression) is used to provides regular expression tools for advanced string processing. For complex matching and manipulation, regular expressions offer succinct, optimized solutions

import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))



#MATHEMATICS 
import math
#math module provides many features of math
math.cos(math.pi/4)

#Random - is used to make random choice
import random
random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10)   # sampling without replacement
random.random()    # random float
random.randrange(6)    # random integer chosen from range(6)

#Statistics - it is used to calculate some comman Stats operations
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
statistics.median(data)
statistics.variance(data)
