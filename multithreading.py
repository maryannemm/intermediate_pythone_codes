import threading

x=0
y=12
def hello():
    i = 1
    while i < 10:
        # comment: 
        print(i, ' thread 1 ')
        i += 1
    # end while
def there():
    global y
    while y>0:
        print(y, ' thread 2 ')
        y-=1
t1=threading.Thread(target=hello) 
t2=threading.Thread(target=there)
t1.start()# make them run concurrently
t2.start()

t2.join()# dont print the print statement below else until these thread 
#t1.join()# dont print anthing else until this thread  from the output this thread is still ffected by the print below



print('threads have finished running')