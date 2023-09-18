if True :
    print('Python Programming')

print('Java Programming')

score = 70
if score >= 60 :
    print('Congrats! you passed the exam')

s = 'Hello World'

if 'H' and 'W' in s:
    print(s, 'has', 'H and W')

    print('--------------------------------------')

if score >= 60:
        print('Passed')
else:
        print('Failed')

print('----------------------')
age = 20
result = None

if age >= 21:
    result = 'Eligible'
else:
    result = 'Not Eligible'

print(result)

print('----------------------')

# Ternary:

age = 26
result = 'Eligible' if age >= 21 else 'Not Eligible'

print(result)

print('----------------------')

num = 100

result = None

if num > 0:
    pass # code fragments
elif num < 0: # same with else if block of Java
    pass
else:
    pass

if num > 0:
    result = 'Positive' # code fragments
elif num < 0: # same with else if block of Java
    result = 'Negative'
else:
    result = 'Zero'

print(result)

print('----------------------')

num = 200

result2 = 'Positive' if num > 0 else 'Zero'

print('----------------------')

score = -300

if score >= 60:
    print('Pass')
else:
    print('Failed')


print('----------------------')

if 0 <= score <= 100:
    if score >= 60:
        print('Passed')
    else:
        print('Failed')
else:
    print('Invalid Score')


print('----------------------')

score = 95

if 0 <= score <= 100:
    if score >= 90:
        print('A')  # pass
    elif score >= 80:
        print('B')  # pass
    elif score >= 70:
        print('C')  # pass
    elif score >= 60:
        print('D')  # pass
    else:
        print('F')  # pass
else:
    print('Invalid')    # pass


"""
A score of a student is given, write a program that can calculate the grade of the student

    Possible grades are:
        1. A ( 90 ~ 100)
        2. B ( 80 ~ 90 )
        3. C ( 70 ~ 80 )
        4. D ( 60 ~ 70 )
        5. F ( less than 60)
"""
