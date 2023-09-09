import threading

event1=threading.Event()
event2=threading.Event()

def my_first_function():
    print("waiting for the first event to be triggered")
    event1.wait()
    print('event 1 has been triggered')
def my_second_function():
    print('waiting for event 2 to be triggered')
    event2.wait()
    print('event 2 has been triggered')
event_1=threading.Thread(target=my_first_function)
event_2=threading.Thread(target=my_second_function)
event_1.start()
event_2.start()

events=event2, event1
e1=input('Do you want to trigger event? [y/n]')
e2=input('Do you want to trigger event 2 [y/n]')
e1=e1.lower()
e2=e2.lower()

if e1 == 'y':
    event1.set()
elif e1 == 'n':
    print("event wont be triggered")
else:
    print("invalid input")
if e2 == 'y':
    event2.set()
elif e2 == 'n':
    print("event wont be triggered")
else:
    print("invalid input")




