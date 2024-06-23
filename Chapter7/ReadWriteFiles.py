#topic 7.2 
#Opening reading and writing from a file and Serialization and Deserialization

#2nd argument tells us the use of file ... w for write only... r for read only... r+ for both reading and writing... a for appending data to a file. If we leave this argument then r is assumed.
file = open('Chapter7/zaid.txt','w',encoding='UTF-8')


#if we want to open a file in Binary mode than we write 'b' with the file mode like('wb') and we must node specity encoding with the binary mode.
file2 = open('Chapter7/zaid1.txt','a')

with open('Chapter7/zaid3.txt','a') as file3:
    file3.write('My name is Muhammad Zaid Amjad\n')

#we always convert the other types into string before writing them.
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
file.write(s)
file.close()

#it returns the current position of file's object
print(file2.tell())


#seek() method alter the position of file's objects
#1st argument tells offset-means shift the position how far from reference point
#2nd argument tells whence-means reference point (0 is for file starting, 1 is for file current position, 2 is for end of file)

#whence 1 and 2 is only supported in binary mode of file...
# file2.write('I am shifting the current position of file.\n')
# print(file2.seek(3,0))

#tells that if the file is connected to terminal
file2.isatty()



#SERIALIZING AND DESERIALIZING
import json
file5 = open('Chapter7/serial.json','w',encoding='utf-8')
x = [1, 'simple', 'list']
#dumps funtions return the converted string.
print(json.dumps(x))

#json.dump() is used to write the serialized object into file
#use utf-8 encoding for serializing and deserializing in opening file
json.dump(x,file5)
file5.close()
# this will deserialize and return the deserialized object from a file
file5 = open('Chapter7/serial.json','r',encoding='utf-8')
file6 = json.load(file5)
print(file6)
file2.close()