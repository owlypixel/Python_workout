from time import sleep
from threading import *

# create a simple function that counts from 1 to 5
def count():
    for x in range(5):
        print(x)
        sleep(1)

# create a thread that is targeted at our function count
thread1 = Thread(target = count)

# start thread
thread1.start()
print('END')
