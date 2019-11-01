new_var = 3

# if statement, elif is else if, 4 spaces is convention, not tab

if new_var > 4:
    print('new_var is greater than 4')
elif new_var > 6:
    print('new_var is greater than 6')
else:
    print('new_var is not greater than 4 or 6')

# for loop

for sport in ['baseball', 'basketball', 'hockey']:
    print('{} is a sport'.format(sport))

for number in range(5):
    print(number)

# will print lowest, not highest
for number in range(3, 6):
    print(number)

# loop over a list, grab index and value
new_list = ['baseball', 'basketball', 'hockey']
for sport, value in enumerate(new_list):
    print(value, sport)

# while loops
y = 10
while y > 0:
    print(y)
    y -= 1  # -= same as JS, can do += as well, etc

try:
    raise IndexError('an index error')
except IndexError as error:
    pass  # just passes, would normally do something here
except (TypeError, NameError):
    pass
else:
    print('pass!')
finally:  # this will always run in every circumstance after end of try
    print('try is done')


with open('file.txt') as file:
    for line in file:
        print(line)

# write to a file
new_lines = {"1": 1, "2": 2}
with open('file.txt', "w+") as file:
    file.write(str(new_lines))

with open('file.txt') as file:
    for line in file:
        print(line)
