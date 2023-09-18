# arithmetic: +,-,*,/,%

print(10-2)
print(10+2)

print(10*3)

print(10/3) # Datatype matters always will get back float
print(10/2)

print(10%3)

# shorthand assignment operators: =,+=,*=,/=,%=

a = 100

a = 200

print(a)

a += 100

print(a)

a -= 50

print(a)

a /= 2

print(a)

# logic operators: and, or, not
s = 'Hello World'
print('H' and 'W' in s)
print (True and True)
print(True or False)

s = 'Java Python C# C++'

print('Java' or 'Ruby' in s)

age =29
citizen_ship = 'USA'
is_eligible = age >= 18 and citizen_ship == 'USA'

print(is_eligible)

has_java = 'Java' in s
print(has_java)

# !contains()
print('Python' not in s)

print(not False)
print(not True)

print('----------------------------------')
# identity operators --> is, or

s = 'Java'
s2 = 'Java'

print(s is s2) # to verify if those are same objects, or if they are having IS A RELATIONSHIP --> returns True or False
# (referencing to the same object)




