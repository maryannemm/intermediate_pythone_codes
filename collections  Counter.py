from collections import Counter

c=Counter('ribashongilogasheshiakili')
b =Counter(['pen', 'book','book','book','pen','pencil', 'eraser','ink'])
f=Counter({'p':'pen','c':'cat','d':'date','y':'why'})
print(c)
print(b.most_common(2), "most common 2") #prints the second most common element and how many times they are common
print(b.most_common(1), "most common 1") #prints the second most common element and how many times they are common
print(f)
y=Counter(a=4, b=5, c=3,d=2)
m=Counter(['a',"a",'a','b','b','c'])
print(y & m, 'intersection')   #intersection (minimum value in the lists) if its less or equal to 0 it wont be shown
print(m | y, 'union')   #union (maximum value)