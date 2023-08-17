import threading
 
event=threading.Event()

def function_1():
    print('waiting for an event to be triggered...')
    event.wait()
    print("performing an action now...")
thread=threading.Thread(target=function_1)
thread.start()