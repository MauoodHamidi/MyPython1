name = input('What is your name?\n')
print('Hi,%s.' % name)
fruits = ['Banana', 'Apple', 'Lime']
loud_fruits = [fruit.upper() for fruit in fruits]
print(loud_fruits)

the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")
else:
    print("Don't be crazy and enjoy bcz you will not fall")