import threading
import time

file_name='text.txt'
text=''
def read_file():
    global file_name, text
    countdown=4
    while countdown < 10:
        with open('text.txt', 'r')as f:
            text=f.read()
            
        print('daemon thread is running in the background')
        countdown+=1
        time.sleep(2)

def print_loop():
    for i in range(30):
        print(text)

thread1=threading.Thread(target=read_file, daemon=True)
thread2= threading.Thread(target=print_loop)

thread1.start()
thread2.start()

#thread1.join()
#thread2.join()

print('Threads completed')