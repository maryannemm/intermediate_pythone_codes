import threading
import time

num=8140
lock=threading.Lock()
def adding():
    global num , lock
    lock.acquire()# checks if the resource is free to use wait till its free and if its free you locks it preventing another thread from using it

    while num<10000:
        print(num)
        num +=100
        time.sleep(0.1)# to slow down the print output
    print('thread 1 finished running')
    lock.release()

def subtracting():
    global num , lock
    lock.acquire()
    while num>5000:
        print(num)
        num-=100
        time.sleep(0.1)# 0.5 sec delay
    print("thread 2 finished running")
    lock.release()

th1=threading.Thread(target=adding)
th2=threading.Thread(target=subtracting)

th1.start()
th2.start()