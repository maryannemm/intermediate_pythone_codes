import threading

def  function_one():
    for i in range(10):
        print ('one ', flush=True)

def function_two():
    for t in range(20):
        print('Two ' ,flush=True)

th1= threading.Thread(target=function_one)
th2= threading.Thread(target=function_two)

th1.start()
th2.start()