#!/usr/local/bin/python3

import queue
import threading
import time

exitFlag = 0

class mythread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程: " + self.name, self.counter)
        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        threadLock.release()
        print ("结束线程: " + self.name, self.counter)

def print_time(threadName, delay, counter):
    print ("counter is : {}".format(counter))
    print ("delay is : {}".format(delay))
    while counter:
        if exitFlag:
            print ("exitFlag is : {}".format(exitFlag))
            threadName.exit()
        time.sleep(delay)
        print ("{}: {}".format(threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

thread1 = mythread(1, "Thread-1", 1)
thread2 = mythread(2, "Thread-2", 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for i in threads:
    i.join()

#thread1.join()
#thread2.join()
print ("exit master threading")