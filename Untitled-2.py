class Person:
    def greet(self, name):
        self.name=name
        print('hello, my name is ', name)

class Student(Person):
    def learn(self, major):
        self.major=major
        print("i am learning ", major)
person1=Person()
student1=Student()
person1.greet('anne')
print(person1.name)
student1.learn('Health')
print(student1.major)
