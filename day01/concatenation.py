
name = 'james'
age = 26

print('My name is ' + name)
# print('My age is' + age) + is not recommended to use for concatenation --> format() method
print(str('My age is ')+ str(age))

print('My age is {}'.format(age))  # {}-> place holder

print('My name is {} and I am {} years old'.format(name,age))

print(f'My name is {name} and I am {age} years old')  # --> the easiest way to achieve concatenation in Python

print('Python', 3, 'is awersome: ', True)


