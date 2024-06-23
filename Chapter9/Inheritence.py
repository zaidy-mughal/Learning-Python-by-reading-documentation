class parent:
    def __init__(self) -> None:
        self.name = 'zaid'
        print("it is parent class")

class child(parent):
    def __init__(self) -> None:
        super().__init__()
        print('it is child class')


x = child()
print(x.name)
# check whether it is instance of class
print(isinstance(x,child))
#check whether it is a subclass of some given class.
print(issubclass(child,parent))



#MULTIPLE INHERITENCE
#in python it works dynamically - not calls the class more than once , only search the class for instance once by order written in inheritence...
class Base1:
    def __init__(self) -> None:
        print("Base 1 class")
        pass

class Base2:
    def __init__(self) -> None:
        print("base 2 class")
        pass

class Base3:
    def __init__(self) -> None:
        print("base 3 class")
        pass

#the class comes first in order will gives the value to super() in the derived class...
class DerivedClassName(Base1, Base2, Base3):
    def __init__(self) -> None:
        super().__init__()

DerivedClassName()