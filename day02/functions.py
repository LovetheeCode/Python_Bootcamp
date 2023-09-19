"""



Java Methods
    public static void method(parameter){
        body
    };

Python Function
    def function_name():
        statement

generic function (void)
return function need to use ->
# call function by it's name

"""
import numbers


# include indentation for the scope of function
def display_message():
    print('Hello Cydeo')
    print('Hello World')

    display_message()


# do not have give any return type, Python used dynamic typing, 'return' keyword
# and return function call in print statement or assign to a variable
def value():
    return 10


print(value())


# you can make it mandatory for a function to return a value -> create a generic function "->"

def return_int() -> int:
    return 10


print(return_int())


# passing parameters to function

def square(num):
    return num * num


print(square(10))


# def divide(num1, num2):
#    return num1/num2
# print(divide(10, 2))

# restrict the type to use, indicate that this function only takes an int argument
def square1(num: int):
    return num * num


print(square1(5))


def add(num1: int, num2: int):
    return num1 + num2


print(add(10, 20))

""" if you not sure which class to use -> numbers
    def add(num1: numbers, num2: numbers) -> numbers:
    return num1 +num2
"""

print('-----------------------')


def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid operator')
        return 0


print(calculate(10, 20, '+'))


# example of method overloading

def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:
    return n1 + n2 + n3 + n4


print(sum(10, 20))  # 30
print(sum(10, 20, 30))  # 60

"""
this is method in Python ->

class test:
    def method(self):
    pass
"""

print('--------------------------')


def concat(a: str, b, c='', d='', e=''):
    print(f'{a} {b} {c} {d} {e}')


concat('Cydeo', 'School')
concat('Python', 3, 2.5)
concat('Python', 3, 2.5, True)
concat('Python', 3, 2.5, True, False)


"""
1. Declaring
2. parameters
3. restricting parameter' data type
4. setting default value to parameter
5. restricting return type

Dynamic Typing
"""
