from collections import namedtuple
#syntax: namedtuple(type_name, field_names) i.e field_names could be in a list
Person = namedtuple('person',['name','age','gender'])
person1= Person(name='hanabi', age=24, gender='feamle')
person2= Person(name='kagura', age=22, gender='feamle')
person= person1, person2
for details in person: 
    print(details)

User= namedtuple('user','skills department role') #treat user like a class the spaces are treated like commas hence  field names here are treated like a list can also take a dict taking key ignoring value
u1=User('coding', 'IT', 'Programmer')
print(u1.department)
print(u1.skills)
print(u1.role)
