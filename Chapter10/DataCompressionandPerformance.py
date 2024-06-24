# DATA COMPRESSION

# Common data archiving and compression formats are directly supported by modules including: zlib, gzip, bz2, lzma, zipfile and tarfile.

import zlib
s = b'witch which has which witches wrist watches'
print(len(s))
c = zlib.compress(s)
print(len(c))

d = zlib.decompress(c)
print(len(d))

e = zlib.crc32(d)
print(e)


#Timeit is used to check the performance of two small approaches if we want to check the performance to Larger Modules than we will use -( pstats )- and -( profile ) Modules

from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())
print(Timer('zaid="zaidy"').timeit())


#TESTING OF A PROGRAM 
# Testing in Docstring using doctest module
# doctest.testmod() automatically validate the embedded test in the docstring of the module
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()


#Internationalization in python which makes the code available for different languages without changing the engineering of the code
import gettext

# Set up translation for a specific language
locale_path = 'path/to/locale/directory'
language = 'es'  # Spanish
gettext.bindtextdomain('myapp', locale_path)
gettext.textdomain('myapp')
_ = gettext.gettext

# Now you can use _() to wrap strings that need to be translated
print(_("Hello, World!"))