print('Hello, World!')

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
