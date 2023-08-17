age = int(input('enter your age: '))
while age < 25:
    print('you\'re still in school')
    break
else:
    print("you're working")
money=int(input('enter amount'))
while money<500 and age>25:
    print('You\'re just too poor!!!')
    exit()
else:
    print('Perhaps You\'re rich...')