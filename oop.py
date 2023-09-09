#step one:

import csv
class Item:
    def calculate_total(self, p, q, n):
        total=str(p*q)
        return total,n

item1=Item() 
item1.name='car'
item1.price=1000
item1.quantity=50
print(item1.calculate_total(item1.price, item1.quantity, item1.name))


item2=Item() 
item2.name='phone'
item2.price=1000
item2.quantity=50
print(item2.calculate_total(item2.price, item2.quantity, item2.name))# notice i cant use p, q,n to point to price, name and quantity


import os
print("Current working directory:", os.getcwd())


# another way to write the code above using __init__ magic method that is initialized whenever class's Item is used in an object below
#step 2:
class Item:
    pay_rate=0.8 #class attribute and the attributes below are
    all=[]
    def __init__(self, price:float, quantity, name:str):  #specify the datatypes i.e these paramaters can also be assigned values here
        #validate that the numbers aren't negative issung assert statement.
        assert price >=0  , f'price {price} is not greater than zero'   # assert prints this error message
        assert quantity>=0 , f'quantity {quantity} cannot be less than zero'

        #assinging values
        self.name=name       #assigns the 'name' that will be used in the item to the 'name' that is reffered to here   
        self.price=price     #assigns the 'price' that will be used in the item.price as self.price to the 'price' that is reffered to here
        self.quantity= quantity

        Item.all.append(self) #appends list all=[] whenever an object/instance is created

        return print(f"name is {name}, price is {price}, quantity is {quantity}")

    def calculate_total(self): #remove q,p,n because we can refer to attributes by their names because of item()already parsed the values alongside init
        total=str(self.price*self.quantity)
        return total, self.name
    @classmethod  #because this data is going to be used by other methods in this class
    def instanciate_file(cls):
        with open('item.cvs', 'r') as f:
            reader= csv.DictReader(f) #converts the content of csv file 'f' into a dictionary and stores the dictionary in reader
            items= list(reader)# converts the dictionary into a list
            for item in items:
                Item(
                    name=item.get('name'),
                    price=float(item.get('price')), 
                    quantity=int(item.get('quantity')), 
                )
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            #counts out floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else: 
            return False
    def __repr__(self):
        return f"Item (name {self.name}, quantity {self.quantity}, price {self.price})"

Item.instanciate_file()
print (Item.all)
print (Item.is_integer('b'))
print (Item.is_integer('b'))
print (Item.is_integer(50))
print (Item.is_integer(50.5))



##### this is a child class of the class Item and inherits all its attributes
class Phone(Item):
    pay_rate=0.8 #class attribute and the attributes below are
    def __init__(self, price:float, quantity, name:str, broken:int):  #specify the datatypes i.e these paramaters can also be assigned values here
        #validate that the 
        self.broken=broken
        super().__init__(
            name, quantity, price
        )

        return print(f"{self.__class__.__name__} {name}, price is {price}, quantity is {quantity} broken phones: {broken}")




'''item1=Item(300, 30, 'cars')
print(item1.name) #will print cars
print(item1.calculate_total())#prints the total value of item1 which are cars


item2=Item(200,20, 'phones') 
print(item2.price) #will print 200
print(item2.calculate_total())# prints the total value of item2 which is phones

item4=Item(20, 20, 'word')
print(item4.calculate_total())
print(Item.__dict__, '__dict__')#prints the attributes of a class or instance


print(Item.all)# prints the insances created



for instance in Item.all:
    print(instance.name)   '''

'''item3=Item(-2,-1, 'pens') 
print(item3.price) #will print aN ERROR because of the assert statement
print(item3.calculate_total())'''

phone1= Phone('samsung',500,10,3)
#phone1.broken=3
phone2=Phone('nokia', 400,15,2)
#phone2.broken=2
print(phone1.broken)
print(Item.all)
