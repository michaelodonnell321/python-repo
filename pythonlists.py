#no declarations, only assignments
var = "i'm a variable"
print (var)
print("print me" if 5>1 else 10) # you'll get print me string

#arrays in JS are lists here
list = [1,2,3,4]
print (list)

#append to put things on end of array, pop to remove from end
list.append(5)
print (list)
list.pop()
print (list)

#access list items just like arrays in JS

print (list[0]) # item 0
print (list[-1]) # last item

del list[0] #deletes item at index
print (list)

#concatenate lists
other_list = [5,4,3,2,1]
print (list + other_list)

#tupples look like lists, but are immutable

tupple = (1,2,3)
print(tupple)
#tupple[0] = 3 # this will be a TypeError