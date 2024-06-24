#output Formatting using different libraries


# The reprlib module provides a version of repr() customized for abbreviated displays of large or deeply nested containers:
import reprlib
print(reprlib.repr(set('supercalifragilisticexpialidocious')))


# The pprint (pretty printer) module offers more sophisticated control over printing both built-in and user defined objects in a way that is readable by the interpreter. 
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint.pprint(t, width=30)


# The textwrap module formats paragraphs of text to fit a given screen width

import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=35))


# The locale module accesses a database of culture specific data formats. 
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')

conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
locale.format("%d", x, grouping=True)

locale.format_string("%s%.*f", (conv['currency_symbol'],conv['frac_digits'], x), grouping=True)


#Templating in Python allows users to customize their applications without having to alter the application.
# we write $ sign to use template variables to alter to write $ in string we use $$ symbol
# The substitute() method raises a KeyError when a placeholder is not supplied in a dictionary or a keyword argument. 


from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')


# For mail-merge style applications, user supplied data may be incomplete and the safe_substitute() — it will leave placeholders unchanged if data is missing:

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
#t.substitute(d)

print(t.safe_substitute(d))

# we can use custom delimiter(like %) in the subclasses of Template
import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'
fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))


