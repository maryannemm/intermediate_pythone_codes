import threading
import time
 
event=threading.Event()

def function_1():
    print('waiting for an event to be triggered...')
    time.sleep(1)
    event.wait()
    print("performing an action now...")
thread=threading.Thread(target=function_1)
thread.start()

e=input('do you want to trigger an event? [y/n]')
e=e.lower()
if e == 'y':
    event.set() # triggers the event
elif e == 'n':
    print("exiting...")
else:
    print("invalid input")