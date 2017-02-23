from time import sleep
from threading import *

# create a function with an infinite loop that prints greeting
def greet():
    while True:
        print('Hi')
        sleep(1)

# create a daemon thread that is targeted at our function count
thread1 = Thread(target = greet, daemon = True)

# start thread
thread1.start()

input("Hello: ...")

# the program execution will be over when the main thread ends
