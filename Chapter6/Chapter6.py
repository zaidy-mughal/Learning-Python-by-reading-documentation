#Chapter6

#A module is a file containing Python definitions and statements. 
# Within a module, the module’s name (as a string) is available as the value of the global variable __name__
#We can add modules using import modulename
import module1

module1.fib(10)
print(module1.__name__)

from module1 import *
# (*)This imports all names except those beginning with an underscore (_). 


# we can also name the import module1 directly
import module1 as fibonacci
fibonacci.fib(10)


# It can also be used when utilising from with similar effects
from module1 import fib as fibonacci
fibonacci(500)

# we can update the path of python module searching path
# import sys
# sys.path.append('/ufs/guido/lib/python')

# The built-in function dir() is used to find out which names a module defines. 
# It returns a sorted list of strings:
import sys
print(dir(module1))
print(dir(sys))


# Without arguments, dir() lists the names you have defined currently:
print(dir())

# dir() does not list the names of built-in functions and variables. 
import builtins
print(dir(builtins))


#from there all are the types and working or imports of packages and submodules...


#this is the structure of general package and subpackages and modules and submodules
# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...



#importing * from a package is a bad practice as it only gives the names of submodules stored in  __all__ attribute
#we can use this instead
# import package from submodule


# from . import echo
# from .. import formats
# from ..filters import equalizer

