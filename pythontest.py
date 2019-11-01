print('Hello, World!')

#single line comments are a # symbol
""" multi line comments are surrounded by 3 " symbols
"""
#numbers
12
#do some math
print(1+1)
print(5-2)
print(12*12)
print(111/11)

#integer division with 2 /
print(7//2) # is 3
print(14//5) # is 2
#normal division will give decimals
print(8.0/3)
#modulo, same as JS
print(11%3) # will be 2
#exponents are **
print(3**2, 'is 9') # add a string, comma separates
#parenthesis works for math
print(2+4) * 3 # is 18

#BOOLEANS - capitalize
True
False
#not is not, just like ! in JS
print(not True) # False
print(not False) # True
#and and or
print(True and False) # false
print(True or False, 'will be true')

#equals is ==, != for not equal
print(0==2, 'is False')
print(2!=2, 'is False')

#< and <= work as expected
print(3>2,'is True')
print(2<1,'is False')
print(3>=3,'is True')

#len is length
print(len('length'),'is 6')

#string interpolation
print("{0} is great, {0} is the best, {0} is super {1}".format('mike', 'amazing'))

#this is an interest calculator, takes inputs and spits out total interest:
# print('Interest Calculator:')
amount = float(input('Principal amount ?'))
roi = float(input('Rate of Interest ?'))
years = int(input('Duration (no. of years) ?'))
total = (amount * pow(1 + (roi/100), years))
interest = total - amount
print('\nInterest = %0.2f' %interest)

import keyword
print(keyword.iskeyword("keyword"))
print(keyword.iskeyword("try"))

try:
    print(keyword.iskeyword("keyword"))
except Exception as ex:
    print(ex)
