#Exception Handling
while True:
    try:
        num = int(input("Enter a number: "))
        break
    except (ValueError,KeyboardInterrupt):
        if(isinstance(ValueError)):
            print("Pai number chaidaa!")
        else:
            print("Pai teri mehrbani khud likh!")


#the else clause in this runs when except block cannot run...or simply when try do not raise any exception
try:
    file = open('Chapter8/file.json','w',encoding='utf-8')
except FileNotFoundError:
    print("File can't open!")
else:
    file.write("Zaid Amjad Mughal")
    file.close()


#Exceptions have instances stored in the inst.args
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)



#we can also raise exception at our own using raise keyword
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    #raise                      #this cause all the remaining code useless



#Exception Chaining can be done by using from keyword with raise
try:
    raise ValueError("Pai Number hi ha")
except ValueError as exc:
    print('Error is: ',exc)
    # raise RuntimeError("Failed to handle exception") from exc


# Exception chaining happens automatically when an exception is raised inside an except or finally section. Exception chaining can be disabled by using from None idiom:

try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None


#finally block will run in every case. If try raise an exception then finally block is executed first and then exception raised.
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')