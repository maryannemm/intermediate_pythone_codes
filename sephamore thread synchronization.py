import threading
import time

semaphore=threading.BoundedSemaphore()
def access(thread_num):
    print(f'{thread_num} is trying to access the resource')
    time.sleep(0.8)
    semaphore.acquire()
    print(f'{thread_num} gained access to the resource')
    time.sleep(0.8)
    print(f'{thread_num} has released the resource')
    time.sleep(0.8)
    semaphore.release()

for thread_num in range(1,11):
    thread=threading.Thread(target=access, args=(thread_num,))
    thread.start()
    time.sleep(2)