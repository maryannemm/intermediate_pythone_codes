lis=[1,2,3,4,5,6,7,8,9,10]
def my_function(i):
    return i**i
def is_odd(m):
    return m%2 !=0
print(list(map(my_function,lis)))
print(list(filter(is_odd, lis)))
