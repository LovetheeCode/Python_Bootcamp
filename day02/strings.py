name = 'Python'

print(len(name))

print(name[0])
print(name [ len(name)-1 ])

print(name[-1])
print(name[2])

print('---------------------')

s = 'Java Programming' # slicing instead of substring
s2 = s[5:16] #starting from : end of the string

print(s2)

s3 = s[:4] # 0 is provided by default slicing from beginning and ending index is excluded

print(s3)

s4 = s[::-1] # slicing in reverse order

print(s4)

s = 'Python Programming'
# s5 = str(reversed(s))


s5 = s[::-1]
print(s5)

s5 = 'python Programming'

s6 = s5[7:]
print(s6)

# String methods all come from str class

print('---------------------')

s = 'python programming language'
# capatalize()
s = s.capitalize()
sa = s.title()
sb = s.strip() # remove all white spaces

print(s)
print(sa)

s = 'JAVA ABA'

print(s.index('A')) # first index of character
print(s.rindex('A')) # last index of character

s = 'Java Java'

s1 = s.replace('Java','Python')
print(s)
print(s1)

s2 = s.replace('Java','Python',1) # to change just one Java to python
print(s2)

s = 'C# C# Python'

s = s.replace(' C#',' Java')
print(s)

s = 'Java Java Java Python Python'
count_java = s.count('Java')  # to count how many 'java' in the string
count_python = s.count('Python')
print(count_java)
print(count_python)

s1 = 'java'
s2 = 'JAVA'

print(s1.lower() == s2.lower()) # to compare (case sensitive)

s = 'Java'

print(s[0].islower())
print(s[0].isupper())

# isdigit() isalpha()

s = 'a'
print(s.isalpha())
s1 = '1'
print(s1.isdigit())
