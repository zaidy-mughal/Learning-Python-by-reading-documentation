#Threading 
# it is very usefull in I/O bound tasks
# Due to the Global Interpreter Lock (GIL) in CPython (the standard Python implementation), threads may not run truly in parallel in CPU-bound tasks, 

import threading

def func():
    print('running this function in another thread')

thread1 = threading.Thread(target='func')

# it will start the thread task(target)
thread1.start()
# If you want your program to wait for a thread to complete before moving on, you can call the join() method on the thread. This tells the main program to wait for the thread to finish.
thread1.join()






# Example in the documentation of running the thread while writing data into files
import threading,zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')


# the threading module provides a number of synchronization primitives including locks, events, condition variables, and semaphores.