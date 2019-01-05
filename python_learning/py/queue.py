#!/usr/local/bin/python

import queue
import threading
import time


exitFlag = 0 

class mythread(threading.Thread):
    def __init__(self, ThreadID, name, q):
        threading.Thread.__init__(self)
        self.ThreadID = ThreadID
        self.name = name
        self.q = q
    def run(self):
        print ("线程开始: {}".format(self.name))
        process_data(self.name, self.q)
        print ("线程结束: {}".format(self.name))

def process_data(ThreadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("{} processing {}".format(ThreadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["thread-1", "thread-2", "thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

#create new thread
for tname in threadList:
    thread = mythread(threadID, tname, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# waiting queue clear
while not workQueue.empty():
    pass

#inotifor exit
exitFlag = 1

for i in threads:
    i.join()

print ("线程结束: {}".format(threads))
