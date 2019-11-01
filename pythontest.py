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



# print('Interest Calculator:')
# amount = float(input('Principal amount ?'))
# roi = float(input('Rate of Interest ?'))
# years = int(input('Duration (no. of years) ?'))
# total = (amount * pow(1 + (roi/100), years))
# interest = total - amount
# print('\nInterest = %0.2f' %interest)

import keyword
print(keyword.iskeyword("keyword"))
print(keyword.iskeyword("try"))

try:
    print(keyword.iskeyword("keyword"))
except Exception as ex:
    print(ex)
